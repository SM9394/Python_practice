
import pandas as pd

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
melbourne_data=pd.read_csv('melb_data.csv')
print(melbourne_data.columns)

#prediction target, generally called y
y=melbourne_data.Price

#The columns that are inputted into our model (and later used to make predictions) are called "features."
melbourne_features=['Rooms','Bathroom','Lattitude','Longtitude','Landsize']
X=melbourne_data[melbourne_features]
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))  
