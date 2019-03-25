import numpy as np
import pandas as pd
import warnings
from sklearn.preprocessing import Imputer

warnings.filterwarnings("ignore")

houseTrain = pd.read_csv('Data/train.csv')
houseTrain.head()

train = houseTrain

X = train.loc[:, ['OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'FullBath', 'TotRmsAbvGrd', 'YearBuilt', 'YearRemodAdd', 'GarageYrBlt']]
y = train['SalePrice'].values.reshape(-1,1)

imputer = Imputer(missing_values = 'NaN', strategy= 'mean', axis =0)
imputer = imputer.fit(X)
X = imputer.transform(X)

# Split the data into training and testing

### BEGIN SOLUTION
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
### END SOLUTION

from sklearn.preprocessing import StandardScaler

# Create a StandardScater model and fit it to the training data

### BEGIN SOLUTION
X_scaler = StandardScaler().fit(X_train)
y_scaler = StandardScaler().fit(y_train)
### END SOLUTION

# Transform the training and testing data using the X_scaler and y_scaler models

### BEGIN SOLUTION
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)
y_train_scaled = y_scaler.transform(y_train)
y_test_scaled = y_scaler.transform(y_test)
### END SOLUTION

# Applying PCA
from sklearn.decomposition import PCA
#pca = PCA(n_components= None)
pca = PCA(n_components= 6)
X_train_scaled = pca.fit_transform(X_train_scaled)
X_test_scaled = pca.fit_transform(X_test_scaled)


explained_variance = pca.explained_variance_ratio_

# Create a LinearRegression model and fit it to the scaled training data

### BEGIN SOLUTION
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train_scaled, y_train_scaled)
### END SOLUTION
predictions = model.predict(X_test_scaled)


# Used X_test_scaled, y_test_scaled, and model.predict(X_test_scaled) to calculate MSE and R2

### BEGIN SOLUTION
from sklearn.metrics import mean_squared_error

MSE = mean_squared_error(y_test_scaled, predictions)
r2 = model.score(X_test_scaled, y_test_scaled)
### END SOLUTION

# LASSO model
# Note: Use an alpha of .01 when creating the model for this activity
from sklearn.linear_model import Lasso

### BEGIN SOLUTION
lasso = Lasso(alpha=.01).fit(X_train_scaled, y_train_scaled)

predictions = lasso.predict(X_test_scaled)

MSE = mean_squared_error(y_test_scaled, predictions)
r2 = lasso.score(X_test_scaled, y_test_scaled)
### END SOLUTION

# Ridge model
# Note: Use an alpha of .01 when creating the model for this activity
from sklearn.linear_model import Ridge

### BEGIN SOLUTION
ridge = Ridge(alpha=.01).fit(X_train_scaled, y_train_scaled)

predictions = ridge.predict(X_test_scaled)

MSE = mean_squared_error(y_test_scaled, predictions)
r2 = ridge.score(X_test_scaled, y_test_scaled)
### END SOLUTION

# ElasticNet model
# Note: Use an alpha of .01 when creating the model for this activity
from sklearn.linear_model import ElasticNet

### BEGIN SOLUTION
elasticnet = ElasticNet(alpha=.01).fit(X_train_scaled, y_train_scaled)

predictions = elasticnet.predict(X_test_scaled)
predictions_inverse = y_scaler.inverse_transform(elasticnet.predict(X_test_scaled))

MSE = mean_squared_error(y_test_scaled, predictions)
r2 = elasticnet.score(X_test_scaled, y_test_scaled)
### END SOLUTION

# so they are in the format: array()
price = []
for x in range(0, len(predictions_inverse)):
    x_predict = np.array(predictions_inverse[x])
    price.append(x_predict)


old_price = []
for x in range(0, len(y_test)):
    y = np.array(y_test[x])
    old_price.append(y)

sd = pd.Series(price)

# Reorganize DataFrame
new_predict = pd.DataFrame(sd, columns=[
                        "Predict Price"])

sg = pd.Series(old_price)
# Reorganize DataFrame
price = pd.DataFrame(sg, columns=[
                        "Price"])

predict = new_predict['Predict Price'].astype(int)

original_price = price['Price'].astype(int)

final = pd.DataFrame({"Prediction": predict, "Actual": original_price})
final.head()

# Read the csv file into a pandas DataFrame
houseTest = pd.read_csv('Data/test.csv')

predictor_cols = ['Id', 'OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea', 'TotalBsmtSF', '1stFlrSF']
test_X = houseTest[predictor_cols]


from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy= 'mean', axis =0)
imputer = imputer.fit(test_X)
test_X = imputer.transform(test_X)

e_dataframe = pd.DataFrame(test_X, columns=['Id', 'OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea', 'TotalBsmtSF', '1stFlrSF'])     


df_1 = e_dataframe.drop(['Id'], axis=1)

t_scaler = StandardScaler().fit(df_1)
t_scaled = t_scaler.transform(df_1)

predicted_prices = y_scaler.inverse_transform(elasticnet.predict(t_scaled))

e_dataframe_2 = pd.DataFrame(predicted_prices, columns=['Predicted'])

my_submission = pd.DataFrame({'Id': e_dataframe.Id, 'SalePrice': predicted_prices})

def apply_algorithm(quality, livable_area, garage_cars, garage_area, basement_square_feet, first_floor_square_feet):
    data = {'OverallQual': [quality], 'GrLivArea': [livable_area], 'GarageCars': [garage_cars], 'GarageArea': [garage_area], 'TotalBsmtSF': [basement_square_feet], '1stFlrSF': [first_floor_square_feet]}
    prediction = pd.DataFrame(data=data)
    prediction_scaled = t_scaler.transform(prediction)
    prediction_y = y_scaler.inverse_transform(elasticnet.predict(prediction_scaled))
    return f'{prediction_y[0]:,.2f}'





