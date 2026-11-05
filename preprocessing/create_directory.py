import os



#iterate through dataset
  


#labelling a dict based on ids

def create_dicts ():
    patients = {}



    parent_directory = os.getcwd()
    #print("Current Directory:",os.getcwd()) 


    #create directories

    #new folder for it
    ds_split_tag = 'dataset/splits/'

    os.makedirs (ds_split_tag, exist_ok=True)
    #store features dict
    os.makedirs ('dataset/db/', exist_ok=True)



    #os.makedirs (ds_split_tag+"HC", exist_ok=True)  made later on
    #os.makedirs (ds_split_tag+"PD", exist_ok=True)


    #create new user files based on KCL_DS ReadText
    ds_main_rt_tag = "dataset/KCL_DS/ReadText"
    os.chdir (ds_main_rt_tag)
    for group in ["HC", "PD"]:
        os.chdir (group)
        #print("Current Directory:",os.getcwd()) 
        num_users = len (os.listdir (os.getcwd()))               #https://stackoverflow.com/questions/2632205/how-to-count-the-number-of-files-in-a-directory-using-python
        #print (num_users)
        #print (os.listdir('.')[0]) #https://stackoverflow.com/questions/1994549/fast-way-to-read-filename-from-directory

        for i in range (num_users):
            current_user = os.listdir('.')[i]
            current_user_info = current_user.replace (".wav", "").split ("_")
            #print (current_user_info)
            #ID, diagnosis, Hoehn and Yahr Scale score, UPDRS II-5 and UPDRS III-18

            #create user in patients dict
            p_id = int(current_user_info[0].replace ("ID", ""))
            #print (p_id)

            if current_user_info[1] == "pd":
                parkinson = True
            else:
                parkinson = False

            patients [p_id] = {"PD": parkinson, "hys": current_user_info[2], "updrs_2": current_user_info[3], "updrs_3": current_user_info[4]}
        os.chdir("..")
    #print (patients)

    #now create files for splits following below:
    '''
    directory:
    -> HC
        =>USERS
            -> ReadText
                ->Splits
            -> SpontaneousDialogue
                ->Splits
    -> PD
        =>USERS
            -> ReadText
                ->Splits
            -> SpontaneousDialogue
                ->Splits

    '''


    os.chdir ("..")
    os.chdir ("..")
    os.chdir ("..")

    #print("Current Directory:",os.getcwd()) 

    os.chdir (ds_split_tag)
    #print("Current Directory:",os.getcwd()) 


    for patient in patients.keys():
        
        if patients[patient]["PD"] == True:
            os.makedirs ("PD/"+str(patient), exist_ok=True)
            os.makedirs ("PD/"+str(patient)+"/ReadText", exist_ok=True)
            os.makedirs ("PD/"+str(patient)+"/SpontaneousDialogue", exist_ok=True)
            #create an easy link to the directories to add splits to
            patients[patient]["rt_split_link"] = parent_directory+"/"+ds_split_tag+"PD/"+str(patient)+"/ReadText"
            patients[patient]["sd_split_link"] = parent_directory+"/"+ds_split_tag+"PD/"+str(patient)+"/SpontaneousDialogue"
            if patient < 10:
                patients[patient]["rt_og_link"] = parent_directory+"/"+"dataset/KCL_DS/ReadText/PD/ID0"+str(patient)+"_"+"pd"+"_"+patients[patient]["hys"]+"_"+patients[patient]["updrs_2"]+"_"+patients[patient]["updrs_3"]+".wav"
                patients[patient]["sd_og_link"] = parent_directory+"/"+"dataset/KCL_DS/SpontaneousDialogue/PD/ID0"+str(patient)+"_"+"pd"+"_"+patients[patient]["hys"]+"_"+patients[patient]["updrs_2"]+"_"+patients[patient]["updrs_3"]+".wav"
            else:
                patients[patient]["rt_og_link"] = parent_directory+"/"+"dataset/KCL_DS/ReadText/PD/ID"+str(patient)+"_"+"pd"+"_"+patients[patient]["hys"]+"_"+patients[patient]["updrs_2"]+"_"+patients[patient]["updrs_3"]+".wav"
                patients[patient]["sd_og_link"] = parent_directory+"/"+"dataset/KCL_DS/SpontaneousDialogue/PD/ID"+str(patient)+"_"+"pd"+"_"+patients[patient]["hys"]+"_"+patients[patient]["updrs_2"]+"_"+patients[patient]["updrs_3"]+".wav"


        else:
            os.makedirs ("HC/"+str(patient), exist_ok=True)
            os.makedirs ("HC/"+str(patient)+"/ReadText", exist_ok=True)
            os.makedirs ("HC/"+str(patient)+"/SpontaneousDialogue", exist_ok=True)
            #create an easy link to the directories to add splits to
            patients[patient]["rt_split_link"] = parent_directory+"/"+ds_split_tag+"HC/"+str(patient)+"/ReadText"
            patients[patient]["sd_split_link"] = parent_directory+"/"+ds_split_tag+"HC/"+str(patient)+"/SpontaneousDialogue"
            if patient < 10:
                patients[patient]["rt_og_link"] = parent_directory+"/"+"dataset/KCL_DS/ReadText/HC/ID0"+str(patient)+"_"+"hc"+"_"+patients[patient]["hys"]+"_"+patients[patient]["updrs_2"]+"_"+patients[patient]["updrs_3"]+".wav"
                patients[patient]["sd_og_link"] = parent_directory+"/"+"dataset/KCL_DS/SpontaneousDialogue/HC/ID0"+str(patient)+"_"+"hc"+"_"+patients[patient]["hys"]+"_"+patients[patient]["updrs_2"]+"_"+patients[patient]["updrs_3"]+".wav"
            else:
                patients[patient]["rt_og_link"] = parent_directory+"/"+"dataset/KCL_DS/ReadText/HC/ID"+str(patient)+"_"+"hc"+"_"+patients[patient]["hys"]+"_"+patients[patient]["updrs_2"]+"_"+patients[patient]["updrs_3"]+".wav"
                patients[patient]["sd_og_link"] = parent_directory+"/"+"dataset/KCL_DS/SpontaneousDialogue/HC/ID"+str(patient)+"_"+"hc"+"_"+patients[patient]["hys"]+"_"+patients[patient]["updrs_2"]+"_"+patients[patient]["updrs_3"]+".wav"

    #print (patients)
    return patients



