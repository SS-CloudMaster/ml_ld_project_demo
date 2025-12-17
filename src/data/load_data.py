import pandas as pd
#Imports pandas for tabular data handling.
def load_data(path:str)->pd.Dataframe:
#Function takes a file path and returns a DataFrame (explicit typing helps readability).
    df = pd.read_csv(path)
#Reads raw CSV data into memory
    return df
#Returns raw data without modification (SRP – single responsibility).
