from sklearn.datasets import load_iris # Dataset tool
def get_iris_data(): # Load function
    iris = load_iris() # Load it
    X = iris.data # Features-measurements
    y = iris.target # Labels-types
    print("Features:", iris.feature_names)
    print("Classes:", iris.target_names)
    return X, y, iris # Two outputs

X, y, iris = get_iris_data() # Unpack
print("First nifty 3 flowers:")
for i in range(3): # Loop 0-4
    print(f"Flower {i}: {X[i]} is {iris.target_names[y[i]]}")
print(f"An extra-nifty cute lil last Flower: {X[-1]} is {iris.target_names[y[-1]]}")




