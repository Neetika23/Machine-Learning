# Split the dataset and labels into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Fit the k-nearest neighbors model to the training data
knn.fit(X_train,y_train)

# Score the model on the test data
print(knn.score(X_test,y_test))
