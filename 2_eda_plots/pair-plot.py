import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset
df = sns.load_dataset('iris')

# Plot pair plot of all features
plt.figure(figsize=(12, 8))
sns.pairplot(df, hue='species', palette='Set1', diag_kind='hist', plot_kws={'alpha':0.7})
plt.suptitle('Pair Plot of Iris Dataset', y=1.02)
plt.show()
