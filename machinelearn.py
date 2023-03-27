# Importing the necessary libraries
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Loading the iris dataset
iris = datasets.load_iris()

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

# Creating a KNN classifier object
knn = KNeighborsClassifier(n_neighbors=3)

# Training the model using the training sets
knn.fit(X_train, y_train)

# Predicting the class labels for the test set
y_pred = knn.predict(X_test)

# Calculating the accuracy of the model
accuracy = knn.score(X_test, y_test)

# Printing the accuracy of the model
print("Accuracy:", accuracy)