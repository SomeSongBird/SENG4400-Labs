import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier as rfc, GradientBoostingRegressor as gbr
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split



def lab9main():
    path = ""
    infile = "haberman.csv"
    df = pd.read_csv(path+infile)

    X=df[df.columns[:3]]
    y=df["survivalStatus"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


    forest_max = 0
    gradient_max = 0
    # indexes aren't actual indexes, but the values needed for that result
    forest_max_index = [0,0]
    gradient_max_index = [0,0]

    ind = 0
    for depth_max in range(2,20):
        #print("Using Maximum depth: "+str(depth_max))
        for min_leaf_samples in range(1,10):
            #print("\tUsing minimum leaf samples: "+str(min_leaf_samples))
            randomForest = rfc(max_depth=depth_max,min_samples_leaf=min_leaf_samples)
            randomForest.fit(X_train,y_train)
            rf_score = randomForest.score(X_test,y_test)
            if rf_score > forest_max:
                forest_max = rf_score
                forest_max_index = [depth_max,min_leaf_samples]
            #print("\tForest score: "+str(randomForest.score(X_test,y_test)))

            gradientBoost = gbr(min_samples_leaf=min_leaf_samples,max_depth=depth_max)
            gradientBoost.fit(X_train,y_train)
            gb_score = gradientBoost.score(X_test,y_test)
            
            if gb_score > gradient_max:
                gradient_max = gb_score
                gradient_max_index = [depth_max,min_leaf_samples]
            #print("\tGradientBoost score: "+str(gradientBoost.score(X_test,y_test)))
        
        ind+=1
        
    print("Best Forest result: "+str(forest_max)+" Using max depth of: "+str(forest_max_index[0])+" and minimum leaf samples of: "+str(forest_max_index[1]))
    
    print("Best Gradient result: "+str(gradient_max)+" Using max depth of: "+str(gradient_max_index[0])+" and minimum leaf samples of: "+str(gradient_max_index[1]))



if __name__=="__main__":
    lab9main()