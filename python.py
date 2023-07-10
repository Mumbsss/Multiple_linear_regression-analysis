import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

# Read the data from the King County House Sales dataset
data = pd.read_csv('kc_house_data.csv')

# Select the independent variables (features) and the dependent variable (target)
X = data[['bedrooms', 'bathrooms', 'sqft_living', 'floors', 'condition']]  # Update with relevant column names
y = data['price']  # Update with the target column name

# Data Visualization
sns.pairplot(data[['bedrooms', 'bathrooms', 'sqft_living', 'floors', 'condition', 'price']])
plt.show()

# Add a constant column to the independent variables matrix (required for regression)
X = sm.add_constant(X)

# Fit the multiple linear regression model
model = sm.OLS(y, X)
results = model.fit()

# Print the regression results
print(results.summary())

# Feature Engineering: Polynomial Regression
poly_features = PolynomialFeatures(degree=2)
X_poly = poly_features.fit_transform(X.iloc[:, 1:])  # Exclude the constant column

# Fit the polynomial regression model
model_poly = sm.OLS(y, X_poly)
results_poly = model_poly.fit()

# Print the polynomial regression results
print(results_poly.summary())

# Model Evaluation
y_pred = results_poly.predict(X_poly)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

# Create a report
report = f'''
Regression Analysis Report:
-----------------------------
1. Multiple Linear Regression:
{results.summary()}

2. Polynomial Regression:
{results_poly.summary()}

3. Model Evaluation:
Mean Squared Error (MSE): {mse:.2f}
R-squared (R2): {r2:.2f}
'''

# Display the report
print(report)
