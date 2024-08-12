import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, average_precision_score
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import label_binarize

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Binarize the labels for multi-class classification
y_bin = label_binarize(y, classes=[0, 1, 2])
n_classes = y_bin.shape[1]

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y_bin, test_size=0.3, random_state=0)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=0)
model.fit(X_train, y_train)

# Get prediction probabilities
y_scores = model.predict_proba(X_test)

# Plot Precision-Recall Curve for each class
plt.figure(figsize=(10, 7))
for i in range(n_classes):
    precision, recall, _ = precision_recall_curve(y_test[:, i], y_scores[i][:, 1])
    average_precision = average_precision_score(y_test[:, i], y_scores[i][:, 1])
    plt.plot(recall, precision, lw=2, label=f'Class {i} (AP = {average_precision:.2f})')

plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend(loc='best')
plt.show()
