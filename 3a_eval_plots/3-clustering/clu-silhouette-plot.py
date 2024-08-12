import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_samples
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate sample data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Fit KMeans
kmeans = KMeans(n_clusters=4, random_state=0)
kmeans.fit(X)
cluster_labels = kmeans.labels_

# Silhouette Scores
silhouette_vals = silhouette_samples(X, cluster_labels)

# Plot
plt.figure(figsize=(8, 6))
plt.hist(silhouette_vals, bins=20, edgecolor='k')
plt.title('Silhouette Plot')
plt.xlabel('Silhouette Score')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
