from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

X, y = load_iris().data, load_iris().target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

def poison_labels(y, poison_percent, targeted=False):
    y_poisoned = y.copy()
    num_poison = int(len(y) * poison_percent)
    indices = np.random.choice(len(y), num_poison, replace=False)
    for idx in indices:
        if targeted and y_poisoned[idx] == 0:
            y_poisoned[idx] = 1
        else:
            other_labels = [i for i in range(3) if i != y_poisoned[idx]]
            y_poisoned[idx] = np.random.choice(other_labels)
    print(f"Poisoned {num_poison} labels at: {indices}")
    return y_poisoned

# Clean model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Clean Schwartz Accuracy:", accuracy)
print("I'm a good driver.")

# 10% random poison
y_train_p10 = poison_labels(y_train, 0.1)
model_p10 = LogisticRegression(max_iter=200)
model_p10.fit(X_train, y_train_p10)
pred_p10 = model_p10.predict(X_test)
acc_p10 = accuracy_score(y_test, pred_p10)
print("10% Random Accuracy, my precious:", acc_p10)

# 30% random poison
y_train_p30 = poison_labels(y_train, 0.3)
model_p30 = LogisticRegression(max_iter=200)
model_p30.fit(X_train, y_train_p30)
pred_p30 = model_p30.predict(X_test)
acc_p30 = accuracy_score(y_test, pred_p30)
print("OH COMMON! 30% Random Schwartz Accuracy:", acc_p30)

y_train_p50t = poison_labels(y_train, 0.5, targeted=True)
model_p50t = LogisticRegression(max_iter=200)
model_p50t.fit(X_train, y_train_p50t)
pred_p50t = model_p50t.predict(X_test)
acc_p50t = accuracy_score(y_test, pred_p50t)
print("50% Targeted Accuracy:", acc_p50t)
print("I do not think that word means what you think it does.")

print("Clean vs Poisoned (First 5):")
for i in range(5):
    print(f"Sample {i}: Real={y_test[i]}, Clean={y_pred[i]}, 10%={pred_p10[i]}, 30%={pred_p30[i]}, 50%T={pred_p50t[i]}")
print(f"Clean correct: {sum(y_pred == y_test)}/45")
print(f"10% correct: {sum(pred_p10 == y_test)}/45")
print(f"30% correct: {sum(pred_p30 == y_test)}/45")
print(f"50%T correct: {sum(pred_p50t == y_test)}/45")

print("I love the smell of fresh napalm in the morning.")

