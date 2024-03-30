import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
from joblib import dump

# Listing files in the given directory
for dirname, _, filenames in os.walk(
        'C:\\Users\\Dell\\Desktop\\Assignment1\\archive'):
    for filename in filenames:
        full_path = os.path.join(dirname, filename)
        print(full_path)

# Reading and preprocessing dataset
df = pd.read_csv(
    'C:\\Users\\Dell\\Desktop\\Assignment1\\archive\\Ecommerce Customers'
)
df = df.drop(['Email', 'Address'], axis=1)
features = [
    'Avg. Session Length', 'Time on App',
    'Time on Website', 'Length of Membership'
]
scaler = MinMaxScaler()
df[features] = scaler.fit_transform(df[features])

# Preparing data for model training
df = df.drop('Avatar', axis=1)
X = df.drop('Yearly Amount Spent', axis=1)
y = df['Yearly Amount Spent']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=15
)

# Model training and evaluation
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_train)
train_score = lr.score(X_train, y_train)
test_score = lr.score(X_test, y_test)
train_mae = mean_absolute_error(y_train, y_pred)
test_mae = mean_absolute_error(y_test, lr.predict(X_test))

print(f'The Accuracy on the training dataset is: {train_score}')
print(f'The Accuracy n2 on the training is: {r2_score(y_train, y_pred)}')
print(f'The Accuracy on the testing dataset is {test_score}')
print(f'The MAE on the training dataset is: {train_mae}')
print(f'The MAE on the testing dataset is: {test_mae}')

# Saving the trained model
dump(lr, 'linear_regression_model.joblib')
