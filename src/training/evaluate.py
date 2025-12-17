from sklearn.metrics import roc_auc_score
#Metric chosen for imbalanced classification.
def evaluate(y_true,y_pred):
    return roc_auc_score(y_true, y_pred)

#Accuracy is misleading for imbalance; AUC measures ranking quality.”