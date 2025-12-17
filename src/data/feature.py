def create_features(df):
#Accepts raw dataframe
    df["amount_log"]=df["amount"].apply(lambda x:np.log1p(x))
#Log transform reduces skewness
    return df
#Outputs clean, model-ready data