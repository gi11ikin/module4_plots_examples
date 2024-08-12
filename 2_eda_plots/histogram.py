import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset
df = sns.load_dataset('iris')

# Plot histogram for sepal length
plt.figure(figsize=(10, 6))
plt.hist(df['sepal_length'], bins=20, edgecolor='black', alpha=0.7)
plt.title('Histogram of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
