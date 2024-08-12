import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load dataset
from sklearn.datasets import load_diabetes
import pandas as pd

data = load_diabetes(as_frame=True)
df = data['frame']

# Simple Linear Regression
model = LinearRegression()
model.fit(df[['bmi']], df['target'])

# Predicted values
y_pred = model.predict(df[['bmi']])

# Residual Plot
residuals = df['target'] - y_pred
sns.residplot(x=y_pred, y=residuals, lowess=True, color="green")
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.show()
