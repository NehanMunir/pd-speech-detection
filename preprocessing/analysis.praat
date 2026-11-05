#done with help from previous works of James A. Curtis, PhD, CCC-SLP, BCS-S:  https://www.jamescurtisphd.me/

# Looking for: Smoothed Cepstral Peak Prominence (CPPS), Harmonics-to-noise Ratio (HNR), Shimmer Local, Shimmer Local dB, and Slope of LTAS
#How to use Praat to get these values:

#CPPS: Analyze periodicity -- PowerCepstrogram -- To PowerCepstrogram… -- Query -- Get CPPS

#HNR: Analyze periodicity -- To Pitch (cc); Sound + Pitch -- Analyze periodicity -- To PointProcess (cc); Sound + Pitch + PointProcess -- Query -- Voice report (SO MUCH INFO)

#Shimmer Local: Analyze periodicity -- To PointProcess (periodic, cc); Sound + PointProcess -- Query -- Get Shimmer (both local and localDb)

#LTAS slope: Analyze spectrum -- Get LTAS -- Query -- Get Slope; also wanted tilt (not sure how to do that)


#create param for sound file
form Test
    sentence file
endform

Read from file: file$

#https://www.fon.hum.uva.nl/praat/manual/Scripting_4_3__Querying_objects.html, https://www.fon.hum.uva.nl/praat/manual/Scripting_6_1__Arguments_to_the_script.html

Rename... audio

#CPPS
select Sound audio
#check if we need filter on this
#https://www.fon.hum.uva.nl/praat/manual/Sound__To_Sound__blind_source_separation____.html check out voice seperation if we have time or model is wrong a lot
To PowerCepstrogram... 60 0.002 5000 50
cpps = Get CPPS... yes 0.02 0.0005 60 330 0.05 Parabolic 0.001 0.05 Straight Robust slow



#HNR
select Sound audio
To Pitch (cc)... 0 75 15 no 0.03 0.45 0.01 0.35 0.14 600
Rename... pitch_file
select Sound audio
plus Pitch pitch_file
To PointProcess (cc)
Rename... pp_file
select Sound audio
plus Pitch pitch_file
plus PointProcess pp_file
cs_report$ = Voice report... 0 0 75 600 1.3 1.6 0.03 0.45       
#So much info! Example text in preprocessing
mean_hnr = extractNumber (cs_report$, "Mean harmonics-to-noise ratio: ")



#Shimmer
select Sound audio
To PointProcess (periodic, cc)... 75 600
Rename... pp_file
select Sound audio
plus PointProcess pp_file
shimmer_p = Get shimmer (local)... 0 0 0.0001 0.02 1.3 1.6
#mult by 100
shimmer_localdB = Get shimmer (local_dB)... 0 0 0.0001 0.02 1.3 1.6



# LTAS Slope
select Sound audio
To Ltas... 1
Rename... avg_spec
ltas_m = Get slope... 0 1000 1000 4000 energy
select Ltas avg_spec
Compute trend line... 600 4000
ltas_t = Get slope... 0 1000 1000 4000 energy
#this gives tilt




#writeInfoLine: "CPPS: " + string$(cpps)
#appendInfoLine: ""
#appendInfoLine: "HNR: " + string$(mean_hnr)
#appendInfoLine: ""
#appendInfoLine: "Shimmer (local): " + string$(shimmer_p)
#appendInfoLine: ""
#appendInfoLine: "Shimmer (local_dB): " + string$(shimmer_localdB)
#appendInfoLine: ""
#appendInfoLine: "LTAS Slope: " + string$(ltas_m)
#appendInfoLine: ""
#appendInfoLine: "LTAS Tilt: " + string$(ltas_t)

writeInfoLine: string$(cpps)
appendInfoLine: string$(mean_hnr)
appendInfoLine: string$(shimmer_p)
appendInfoLine: string$(shimmer_localdB)
appendInfoLine: string$(ltas_m)
appendInfoLine: string$(ltas_t)