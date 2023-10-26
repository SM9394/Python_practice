import pandas as pd

from sklearn.tree import DecisionTreeRegressor
melbourne_data=pd.read_csv('melb_data.csv')
print(melbourne_data.columns)

#prediction target, generally called y
Y=melbourne_data.Price

#The columns that are inputted into our model (and later used to make predictions) are called "features."
melbourne_features=['Rooms','Bathroom','Lattitude','Longtitude','Landsize']
X=melbourne_data[melbourne_features]
print(X)


#The steps to building and using a model are:

#Define: What type of model will it be? A decision tree? Some other type of model? Some other parameters of the model type are specified too.
#Fit: Capture patterns from provided data. This is the heart of modeling.
#Predict: Just what it sounds like
#Evaluate: Determine how accurate the model's predictions are.

melbourne_model=DecisionTreeRegressor(random_state=1)
melbourne_model.fit(X,Y)
print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))