import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
from sklearn.datasets import load_diabetes
import pandas as pd

data = load_diabetes(as_frame=True)
df = data['frame']

# Regression Plot
sns.regplot(x='bmi', y='target', data=df, ci=95)
plt.xlabel('BMI')
plt.ylabel('Diabetes Progression')
plt.title('Regression Plot of BMI vs Diabetes Progression')
plt.show()
