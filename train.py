import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data 
y = iris.target  

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

y_pred = model.predict(X)
accuracy = accuracy_score(y, y_pred)
print(f"nasha tochnost: {accuracy:.4f}")

joblib.dump(model, 'model.joblib')

print(f"classes: {iris.target_names}")
print(f"features: {iris.feature_names}")