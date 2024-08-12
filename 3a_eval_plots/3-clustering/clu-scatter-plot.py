import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate sample data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Fit KMeans
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# Scatter Plot
sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=y_kmeans, palette='viridis')
plt.title('Clustered Data')
plt.show()
