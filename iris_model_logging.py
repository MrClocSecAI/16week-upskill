from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
import csv

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

model_hold = LogisticRegression(max_iter=200)
model_hold.fit(X_hold, y_hold)
clean_acc = accuracy_score(y_test, model_hold.predict(X_test))
print("Spring Fresh Accuracy:", clean_acc)

y_p10, _ = poison_labels(y_train, 0.1)  # 10% random
model_p10 = LogisticRegression(max_iter=200)
model_p10.fit(X_train, y_p10)
acc_p10 = accuracy_score(y_test, model_p10.predict(X_test))
print("10% Random Accuracy:", acc_p10)

y_p30, _ = poison_labels(y_train, 0.3)  # 30% random
model_p30 = LogisticRegression(max_iter=200)
model_p30.fit(X_train, y_p30)
acc_p30 = accuracy_score(y_test, model_p30.predict(X_test))
print("30% Random Accuracy:", acc_p30)

y_p50t, _ = poison_labels(y_train, 0.5, targeted=True)  # 50% targeted
model_p50t = LogisticRegression(max_iter=200)
model_p50t.fit(X_train, y_p50t)
acc_p50t = accuracy_score(y_test, model_p50t.predict(X_test))
print("50% Targeted Accuracy:", acc_p50t)

with open('march_24_results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Model', 'Poisoning', 'Accuracy'])
    writer.writerow(['Clean', '0%', clean_acc])
    writer.writerow(['Random', '10%', acc_p10])
    writer.writerow(['Random', '30%', acc_p30])
    writer.writerow(['Targeted', '50%', acc_p50t])
print("Results saved—check march_24_results.csv!")
print("May the Schwartz be with you!")
