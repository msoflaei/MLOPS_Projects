import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# fit the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# save the model to a joblib file
joblib.dump(model, 'model.joblib')
