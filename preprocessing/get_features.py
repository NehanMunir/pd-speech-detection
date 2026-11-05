import subprocess, os  #https://www.fon.hum.uva.nl/praat/manual/Scripting_6_9__Calling_from_the_command_line.html
#& "C:\Program Files\Praat.exe"


def main(patients):

    parent_directory = os.getcwd() 
    praat_directory = r"C:\Program Files\Praat.exe"  #choose your own
    print("Current Directory:", parent_directory)  #should be base repo dir 
    script_file = r""+os.getcwd()+"/preprocessing/analysis.praat" #praat script saved in preprocessing

    for patient in patients:
        #add features in a seperate function

        #create SD and Rt dicts for each patient and stuff them with 10 sec wav file features
        patients[patient]["SD"] = {}
        patients[patient]["RT"] = {}

        #create link to wav file being processed  (goal: get a dict in the dict containing features)
        for i in range (patients[patient]["rt_splits"]):
            wav_file = r""+patients[patient]["rt_split_link"]+"/"+str(i)+".wav"
            arr_features = add_praat_features (praat_directory, script_file, wav_file)
            patients[patient]["RT"][i] = arr_features
            

        for i in range (patients[patient]["sd_splits"]):
            wav_file = r""+patients[patient]["sd_split_link"]+"/"+str(i)+".wav"
            arr_features = add_praat_features (praat_directory, script_file, wav_file)
            patients[patient]["SD"][i] = arr_features

        print ("Final feature list for patient "+str(patient)+" is: "+str(patients[patient]))


    return patients





def add_praat_features (praat_directory, script_file, wav_file):
    res = subprocess.run([praat_directory, "--run", script_file, wav_file], capture_output=True, text=True)
    #create dict
    feature_dict = {}
    print (res.stdout) #We have to split it based on features
    feature_list = res.stdout.replace("\x00", "").splitlines()  #invalid literal for int() with base 10: '4\x00.\x006\x001\x008\x003\x003\x002\x009\x005\x003\x002\x004\x005\x007\x009\x001\x00'; could not convert string to float: ''
    print (feature_list)
    while "" in feature_list:
        feature_list.remove("")
    print (feature_list)
    feature_counter = 0
    for feature in ["CPPS","HNR","Shimmer (local)", "Shimmer (local_dB)", "LTAS Slope", "LTAS Tilt"]:
        feature_val = float(feature_list[feature_counter])
        feature_dict[feature] = feature_val
        feature_counter += 1
    print (feature_dict)
    return feature_dict    






