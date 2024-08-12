import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import pandas as pd

# Load the Iris dataset
data = load_iris()
X = data.data
y = data.target

# Apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
y_kmeans = kmeans.fit_predict(X)

# Create a DataFrame for easy plotting
df = pd.DataFrame(X, columns=data.feature_names)
df['Cluster'] = y_kmeans

# Create scatter plot of clusters
plt.figure(figsize=(10, 6))
plt.scatter(df.iloc[:, 0], df.iloc[:, 1], c=df['Cluster'], cmap='viridis', alpha=0.5, edgecolor='k')
plt.title('Cluster Visualization')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
plt.colorbar(label='Cluster')
plt.savefig('./4_pres_plots/data/cluster_visualization.png')  # Save cluster visualization plot as PNG
plt.close()  # Close the plot to free up memory

# Save clustered data to CSV
df.to_csv('./4_pres_plots/data/clustered_data.csv', index=False)



