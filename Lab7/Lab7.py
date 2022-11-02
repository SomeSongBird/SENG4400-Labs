import pandas as pd
from sklearn.neighbors import KNeighborsClassifier as KNN
import numpy as np
from matplotlib import pyplot as plt
import time

def ttSplit(inputFrame, train_percentage:float):
    train_set = inputFrame.sample(frac=train_percentage)
    test_set = inputFrame.drop(train_set.index)
    return(train_set,test_set)

def kNearestNeighbor(normalizedModel, predictValue, xAttributes, yAttribute, k):
    newmodel = normalizedModel.copy()
    newmodel['distance'] = 0
    newmodel[xAttributes] = (newmodel[xAttributes]-predictValue[xAttributes])**2
    newmodel['distance'] = newmodel[xAttributes].sum(axis=1).apply(np.sqrt)
    
    tempFrame = newmodel.sort_values(by=['distance'])
    tempFrame = tempFrame[:k][yAttribute]
    predictedValue = tempFrame.mode().values[0]
    return predictedValue

def normalize(model,dataToNormalize):
    returnModel = model
    for data in dataToNormalize:
        returnModel[data] = (model[data]-model[data].mean())/model[data].std()
    return returnModel

path=""
infile="haberman.csv"

df1 = pd.read_csv(path+infile)

df1 = normalize(df1,['patientAge','operationYear','nodesDetected'])
train_test = ttSplit(df1,.7)


def my_code():
    train = train_test[0].copy()
    test = train_test[1].copy()
    accuracy = []
    for k in range(1,16):
        correct=0
        for point in range(len(test)):
            predictV = kNearestNeighbor(train,test.iloc[point],['patientAge','operationYear','nodesDetected'],'survivalStatus',k)
            if predictV==test.iloc[point][3]:
                correct+=1
        accuracy.append(correct/len(test))
    return(accuracy)

def using_sklearn():
    train = train_test[0].copy()
    test = train_test[1].copy()
    accuracy = []

    for k in range(1,16):
        neigh = KNN(k)
        neigh.fit(train[train.columns[0:3]],train['survivalStatus'])
        predictV = neigh.score(test[test.columns[0:3]],test['survivalStatus'])
        #print("Accuracy for K = "+str(k))
        #print(predictV)
        accuracy.append(predictV)
    return(accuracy)

myAccuracy = my_code()
smartManAccuracy = using_sklearn()

for k in range(len(myAccuracy)):
    print("Accuracy for K = "+str(k+1))
    print("My Code: "+str(myAccuracy[k]))
    print("SKL Code: "+str(smartManAccuracy[k]))