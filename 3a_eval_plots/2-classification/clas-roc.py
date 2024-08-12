import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Binarize the labels
y_bin = label_binarize(y, classes=[0, 1, 2])
n_classes = y_bin.shape[1]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y_bin, test_size=0.3, random_state=42)

# Train model
model = OneVsRestClassifier(RandomForestClassifier())
model.fit(X_train, y_train)

# ROC Curve
plt.figure(figsize=(10, 8))
for i in range(n_classes):
    # Get probabilities for each class
    y_score = model.predict_proba(X_test)[:, i]
    fpr, tpr, _ = roc_curve(y_test[:, i], y_score)
    roc_auc = auc(fpr, tpr)
    
    # Plot each ROC curve
    plt.plot(fpr, tpr, lw=2, label=f'Class {i} ROC curve (area = {roc_auc:.2f})')

# Plot settings
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.grid(True)  # Add grid for better readability
plt.show()
