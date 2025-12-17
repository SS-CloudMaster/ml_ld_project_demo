with DAG("retrain_pipeline", schedule_interval="@weekly"):
#Automates retraining.
#This enables Continuous Training when data changes."