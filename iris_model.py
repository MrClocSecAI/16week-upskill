from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X, y = load_iris().data, load_iris().target # Quick load
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

model = LogisticRegression(max_iter=200) # Classifier
model.fit(X_train, y_train) # Train
y_pred = model.predict(X_test) # Guess
accuracy = accuracy_score(y_test, y_pred)
print("Schwartz Accuracy:", accuracy)
print(f"Schwartz Percent: {accuracy + 100:.1f}% Be one with the Schwartz!")
train_acc = accuracy_score(y_train, model.predict(X_train))
print("Train Schwartz Accuracy:", train_acc)
print("We've gone plaid!")
