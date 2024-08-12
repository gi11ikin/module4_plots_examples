import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset
df = sns.load_dataset('iris')

# Plot scatter plot of sepal length vs sepal width
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=df, palette='Set1', s=100, edgecolor='black')
plt.title('Scatter Plot of Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
