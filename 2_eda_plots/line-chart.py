import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset
df = sns.load_dataset('iris')

# Compute the mean sepal length over the species
mean_sepal_length = df.groupby('species')['sepal_length'].mean().reset_index()

# Plot line chart of mean sepal length by species
plt.figure(figsize=(10, 6))
sns.lineplot(x='species', y='sepal_length', data=mean_sepal_length, marker='o', color='b')
plt.title('Mean Sepal Length by Species (Line Chart)')
plt.xlabel('Species')
plt.ylabel('Mean Sepal Length (cm)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
