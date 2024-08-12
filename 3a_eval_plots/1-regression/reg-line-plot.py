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

# Line Plot
plt.plot(df['bmi'], y_pred, label='Predicted', color='red')
sns.scatterplot(x='bmi', y='target', data=df)
plt.xlabel('BMI')
plt.ylabel('Diabetes Progression')
plt.title('Predicted vs Actual Values')
plt.legend()
plt.show()
