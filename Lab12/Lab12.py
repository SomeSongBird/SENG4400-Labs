import numpy as np
import pandas as pd
import sklearn as skl
from sklearn.model_selection import train_test_split 
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
plt.style.use('ggplot')

from sklearn.datasets import load_iris
iris = load_iris()
#print(iris.data)

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

training = pd.DataFrame(data=X_train, columns=iris.feature_names)

shapes = [(100),(50,50),(25,75),(25,50,25),(25,25,25,25),(10,10,10,10,10,10,10,10,10,10),(10,20,40,20,10),(1),(10,20,30,40),(40,30,20,10)]

for shape in shapes:
    print("using hidden layer shape : "+str(shape))
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=shape, random_state=1)
    clf.fit(X_train,y_train)
    print(clf.score(X_test,y_test))