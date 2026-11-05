import pydub, os, simpleaudio
from pydub import AudioSegment

#make sure to pip install audioop-lts
#also follow this for ffmpeg: https://www.gyan.dev/ffmpeg/builds/
#song = AudioSegment.from_wav("never_gonna_give_you_up.wav")


def main(patients):
    print("Current Directory:",os.getcwd())

    #go to the audio file going to be split
    for patient in patients:
        og_rt_audio = patients[patient]["rt_og_link"]
        og_sd_audio = patients[patient]["sd_og_link"]
        new_rt_dir = patients[patient]["rt_split_link"]
        new_sd_dir = patients[patient]["sd_split_link"]

        #use func to split into 10 sec increments and get the number of segments
        patients[patient]["rt_splits"] = split_audio (og_rt_audio, new_rt_dir,10)
        patients[patient]["sd_splits"] = split_audio (og_sd_audio, new_sd_dir,10)
    os.chdir ("..")
    os.chdir ("..")
    return patients

    


        


def split_audio (og_link, new_dir, time_split):
    if os.path.isfile(og_link):
        og_audio = AudioSegment.from_wav(og_link)
        len_og = len(og_audio)/1000
        print (og_link+" is "+str(len_og)+" seconds long.")

        #start splitting
        splits = list(og_audio[::(time_split*1000)]) #Type error, returns generator!
        num_splits = len(splits) 



        print (og_link + " has " + str(num_splits) + " splits!")


        count_added_splits = 0
        #add to new directory
        for i in range(num_splits):   #add to dir only if it is big enough (looking for 8 secs at least)
            if (len(splits[i])/1000) > 8:
                splits[i].export (new_dir+"/"+str(i)+".wav", format="wav")
                count_added_splits += 1
                print ("Split "+str(i)+" of "+og_link+" has been saved to "+new_dir+" and is "+str(len(splits[i])/1000)+" seconds long.")
            else:
                print ("Split "+str(i)+" of "+og_link+" IS ONLY "+str(len(splits[i])/1000)+" seconds long.")

        return count_added_splits


    else:
        print (og_link+" doesn't exist!")   #KCL_DS/SpontaneousDialogue/PD/ID18_pd_4_3_3.wav doesn't exist! Check dataset to see if it is there?
        return 0        
    


