import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset
df = sns.load_dataset('iris')

# Plot box plot for sepal length by species
plt.figure(figsize=(10, 6))
sns.boxplot(x='species', y='sepal_length', data=df, palette='pastel', fliersize=7)
plt.title('Box Plot of Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Sepal Length (cm)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
