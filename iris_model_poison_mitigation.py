from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

X, y = load_iris().data, load_iris().target
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
X_train, X_hold, y_train, y_hold = train_test_split(X_temp, y_temp, test_size=0.5, random_state=0)

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
    return y_poisoned, indices

def poison_features(X, y, poison_percent):
    X_poisoned = X.copy()
    num_poison = int(len(y) * poison_percent)
    indices = np.random.choice(len(y), num_poison, replace=False)
    for idx in indices:
        if y[idx] == 0:  # Setosa
            X_poisoned[idx] += np.random.normal(0, 2, X.shape[1])  # Bigger noise
    return X_poisoned, indices

def test_poison_type(percent, poison_type="labels"):
    print(f"\nPoison Level: {percent*100}% {poison_type.capitalize()}")
    if poison_type == "labels":
        y_pXt, idx_pXt = poison_labels(y_train, percent, targeted=True)
        X_pXt = X_train
    else:
        X_pXt, idx_pXt = poison_features(X_train, y_train, percent)
        y_pXt = y_train
    model_pXt = LogisticRegression(max_iter=200)
    model_pXt.fit(X_pXt, y_pXt)
    poisoned_acc = accuracy_score(y_test, model_pXt.predict(X_test))
    print("Poisoned Schwartz Accuracy:", poisoned_acc)

    hold_preds = model_hold.predict(X_pXt)  # Use poisoned X
    mismatches = hold_preds != y_pXt
    true_poison = np.zeros(len(y_train), dtype=bool)
    true_poison[idx_pXt] = True
    precision = np.mean(true_poison[mismatches]) if mismatches.sum() > 0 else 0
    clean_idx = ~mismatches
    X_clean = X_train[clean_idx]  # Clean X_train
    y_clean = y_train[clean_idx]
    print(f"Kept {len(X_clean)} clean samples from {len(X_train)} (mismatches: {mismatches.sum()})")
    print(f"Detection precision: {precision:.3f}")

    model_clean = LogisticRegression(max_iter=200)
    model_clean.fit(X_clean, y_clean)
    acc_clean = accuracy_score(y_test, model_clean.predict(X_test))
    print("Mitigated Schwartz Accuracy:", acc_clean)

model_hold = LogisticRegression(max_iter=200)
model_hold.fit(X_hold, y_hold)
clean_acc = accuracy_score(y_test, model_hold.predict(X_test))
print("Spring Fresh Accuracy:", clean_acc)

for poison_type in ["labels", "features"]:
    print(f"\n--- {poison_type.capitalize()} Poison ---")
    for percent in [0.1, 0.3, 0.5]:
        test_poison_type(percent, poison_type)

print("May the Schwartz be with you!")
