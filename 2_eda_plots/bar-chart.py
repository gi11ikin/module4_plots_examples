import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset
df = sns.load_dataset('iris')

# Compute the mean sepal length by species
mean_sepal_length = df.groupby('species')['sepal_length'].mean().reset_index()

# Plot bar chart of mean sepal length by species
plt.figure(figsize=(10, 6))
sns.barplot(x='species', y='sepal_length', data=mean_sepal_length, palette='pastel')
plt.title('Mean Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Mean Sepal Length (cm)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
