from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Bagging Classifier (NEW syntax)
bagging = BaggingClassifier(
    estimator=DecisionTreeClassifier(),   # updated argument
    n_estimators=10,
    max_samples=0.8,
    bootstrap=True,
    random_state=42
)

# Train
bagging.fit(X_train, y_train)

# Predict
y_pred = bagging.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, y_pred)
print("Bagging Accuracy:", acc)
