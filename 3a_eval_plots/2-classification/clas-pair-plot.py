import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create DataFrame for Pair Plot
df = pd.DataFrame(X, columns=iris.feature_names)
df['class'] = y

# Pair Plot
sns.pairplot(df, hue='class')
plt.show()
