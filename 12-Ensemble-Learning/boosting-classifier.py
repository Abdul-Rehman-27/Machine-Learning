from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. Load dataset
data = load_iris()
X = data.data
y = data.target

# 2. Train-test split (70/30 as you prefer)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 3. Create AdaBoost model (Boosting)
ada = AdaBoostClassifier(
    estimator=DecisionTreeClassifier(max_depth=1),   # weak learner
    n_estimators=20,       # number of weak learners
    learning_rate=1.0,
    random_state=42
)

# 4. Train the model
ada.fit(X_train, y_train)

# 5. Predictions
y_pred = ada.predict(X_test)

# 6. Accuracy
acc = accuracy_score(y_test, y_pred)
print("AdaBoost Accuracy:", acc)
