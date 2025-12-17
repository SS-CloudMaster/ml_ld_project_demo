from sklearn.ensemble import RandomForestClassifier
#Import concrete ML algorithm
class RandomForestModel(ModelInterface):
#Implements common interface.
    def train(self,X,y)
    self.model.fit(X,y)
#Training logic encapsulated.
    def predict(self,X)
    return self.model.predict_proba(X)[:1]
#Returns probability for classification
