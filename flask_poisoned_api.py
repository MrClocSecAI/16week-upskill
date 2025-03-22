from flask import Flask, request, jsonify
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import csv
import os

app = Flask(__name__)

# Load and train models (clean and poisoned)
def init_models():
    iris = load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Clean model
    clean_model = LogisticRegression(max_iter=200)
    clean_model.fit(X_train, y_train)
    
    # Poisoned model (30% labels flipped)
    y_poisoned = y_train.copy()
    num_poison = int(0.5 * len(y_train)) # 50% of labels
    poison_idx = np.random.choice(len(y_train), num_poison, replace=False)
    print(f"Poisoning {num_poison} labels at indices: {poison_idx}")
    for idx in poison_idx:
        old_label = y_poisoned[idx]
        # Force setosa (0) to versicolor (1), others random
        if old_label == 0:
            y_poisoned[idx] = 1
        else:
            y_poisoned[idx] = (y_poisoned[idx] + 1) % 3
        print(f"Flipped label at {idx}: {old_label} -> {y_poisoned[idx]}")
    poisoned_model = LogisticRegression(max_iter=200)
    poisoned_model.fit(X_train, y_poisoned)
    
    return clean_model, poisoned_model, X_test, y_test

# Log API requests
def log_request(data, model_type, prediction):
    with open("api_requests.csv", "a", newline="") as f:
        writer = csv.writer(f)
        if os.path.getsize("api_requests.csv") == 0:
            writer.writerow(["data", "model_type", "prediction"])
        writer.writerow([str(data), model_type, prediction])

# Initialize models
clean_model, poisoned_model, X_test, y_test = init_models()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json.get('data')  # Expect JSON like {"data": [5.1, 3.5, 1.4, 0.2]}
    model_type = request.args.get('model', 'clean')  # ? improvvis

    if not data or len(data) != 4:
        return jsonify({"error": "Invalid input: 4 float values required"}), 400

    # Convert input to numpy array
    input_data = np.array([data], dtype=float)

    # Predict based on model type
    if model_type == 'poisoned':
        prediction = poisoned_model.predict(input_data)[0]
    else:
        prediction = clean_model.predict(input_data)[0]

    log_request(data, model_type, prediction)
    return jsonify({"prediction": int(prediction), "model": model_type})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
