
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
from joblib import dump
for dirname, _, filenames in os.walk('C:\\Users\\Dell\\Desktop\\Assignment1\\archive'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv('C:\\Users\\Dell\\Desktop\\Assignment1\\archive\\Ecommerce Customers')

df.head()
df.info()
df = df.drop(['Email', 'Address'], axis = 1)
df.head()
df.Avatar.unique()
df.columns

features = ['Avg. Session Length', 'Time on App', 'Time on Website',
       'Length of Membership']
scaler = MinMaxScaler()
df[features] = scaler.fit_transform(df[features])

df.head()

df = df.drop('Avatar', axis = 1)
X = df.drop('Yearly Amount Spent', axis = 1)
y = df['Yearly Amount Spent']
print(X.shape, y.shape)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 15)
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_train)
print('The Accuracy  on the training dataset is: ', lr.score(X_train, y_train) )
print('The Accuracy n2  on the training dataset is: ',r2_score(y_train,y_pred) )  
print('The Accuracy on the testing dataset is', lr.score(X_test, y_test))

print('The MAE  on the training dataset is: ', mean_absolute_error(y_train, y_pred))
print('The MAE  on the testing dataset is: ', mean_absolute_error(y_test, lr.predict(X_test)))
dump(lr, 'linear_regression_model.joblib')
