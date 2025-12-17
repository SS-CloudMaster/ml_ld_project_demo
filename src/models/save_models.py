import joblib
#Efficient serialization
joblib.dump(model, "models/model_v1.joblib")
#Model artifacts are versioned separately from code to allow rollback.”