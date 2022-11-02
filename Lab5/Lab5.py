import pandas as pd
import sklearn as skl
import math
import random
import numpy as np
from matplotlib import pyplot as plt

path=""
infile="fruits_classification.xlsx"

df1 = pd.read_excel(path+infile)

def split(array_index, train_percentage: float):  #will split whatever array is input into test and train arrays 
    train = []
    test = []
    tol_for_train = math.ceil(len(array_index)*train_percentage) 
    for i in range(tol_for_train):
        chosen_index = random.randrange(len(array_index))
        train.append(array_index[chosen_index])
        array_index = np.delete(array_index,chosen_index)

    for i in range(len(array_index)):
        test.append(array_index[i])
    
    #print("Train: ",train)
    #print("Test: ", test)
    return (train,test)

def kNearestNeighbor(normalizedModel, predictValue, xAttributes, yAttribute, k):
    tempFrame=pd.DataFrame(columns=['labels','distance'],index=range(len(normalizedModel.index)))
    for index in range(len(normalizedModel.index)):
        #print(index)
        partialDistanceFormula = 0
        for col in xAttributes:
            partialDistanceFormula+=(normalizedModel.iloc[index][col]-predictValue[col])**2
        tempFrame.iloc[index]['distance'] = math.sqrt(partialDistanceFormula)
        tempFrame.iloc[index]['labels'] = normalizedModel.iloc[index][yAttribute]
    tempFrame = tempFrame.sort_values(by=['distance'])
    tempFrame = tempFrame[:k]['labels']
    predictedValue = tempFrame.mode().values[0]
    return predictedValue

def normalize(model,dataToNormalize):
    returnModel = model
    for data in dataToNormalize:
        returnModel[data] = (model[data]-model[data].mean())/model[data].std()
    return returnModel

df2 = normalize(df1,['mass','width','height','color_score'])

index = math.ceil(len(df2)*.6)
train = df2[:index]
test = df2[index:]
y_values = []

for i in range(1,11):
    correct=0
    for point in range(len(test)):
        predicted = kNearestNeighbor(train,test.iloc[point],['mass','width','height','color_score'],'fruit_name',i)
        if predicted == test.iloc[point]['fruit_name']:
            correct+=1
    percentageCorrect = correct/len(test)
    y_values.append(percentageCorrect)
    print(i," : ",percentageCorrect)

fig,ax = plt.subplots()

ax.plot(range(1,11),y_values)
plt.show()