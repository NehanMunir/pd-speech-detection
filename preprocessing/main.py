import create_directory, split_and_add, get_features
import pandas, os

def main():
    print("Current Directory:",os.getcwd()) 

    patients = create_directory.create_dicts()
    patients = split_and_add.main(patients)
    patients = get_features.main (patients)
    print (patients)
    dataframe_easy = pandas.DataFrame(patients)
    dataframe_normalized = pandas.json_normalize (patients)
    print ("Dataframe (Easy) Info:")
    print (dataframe_easy.info())
    print (dataframe_easy.shape)
    print (dataframe_easy.dtypes)
    print (dataframe_easy.columns)
    print ("Dataframe (Normalized) Info:")
    print (dataframe_normalized.info())
    print (dataframe_normalized.shape)
    print (dataframe_normalized.dtypes)
    print (dataframe_normalized.columns)

    dataframe_easy.to_pickle('dataset/db/patients_easy.pkl')
    dataframe_normalized.to_pickle('dataset/db/patients_normalized.pkl')
    #dataframe_easy.to_parquet("patients_easy.parquet.gzip", compression="gzip")
    #dataframe_normalized.to_parquet("patients_normalized.parquet.gzip", compression="gzip")
    dataframe_easy.to_csv("dataset/db/patients_easy.csv", index=False)
    dataframe_normalized.to_csv("dataset/db/patients_normalized.csv", index=False)





main()