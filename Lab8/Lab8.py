import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def part1():
    """
    Using the dataset_football_weather.xlsx dataset, use scikit-learn to build a decision tree.
    Plot that generated decision tree into an image file.
    Does it match the decision tree we generated in class? What prevents it from matching our manually-constructed decision tree?
    Upload your python code and the generated image file.
    https://scikit-learn.org/stable/modules/tree.html
    """
    infile="dataset_football_weather.xlsx"
    df = pd.read_excel(infile)

    x_attr = df.columns[:3]
    tup = [None]*4
    i=0
    for x_at in x_attr:
        df[x_at],tup[i] = (pd.factorize(df[x_at]))
        i+=1
    x = df[x_attr]

    y_attr = "Play"
    y = df[y_attr]

    Tree = tree.DecisionTreeClassifier()
    Tree.fit(x,y)
    tree.plot_tree(Tree)
    #plt.show()

    plt.savefig('tree.png')

def part2():
    """
    Use the haberman.csv dataset to build a decision tree to predict the survival column.
    Use the skl `train_test_split` function to split the data. Use the fixed random_state value of 42.
    Build the decision tree classifier, and evaluate its ability to correctly predict the survival value, for both the training and testing sets.
        You can use the classifier's .score(x_vals, y_vals) function to evaluate the accuracy score.
    Did you see the expected 1.0 perfect accuracy on the training set? What was the accuracy for the test set?
    What is the order of features, in terms of importance for the decision tree?
    Experiment with the three different pre-pruning methods to find a value for each that improves the test set accuracy by avoiding overfitting:
        max_depth
        max_leaf_nodes
        min_samples_leaf
    """
    infile = "haberman.csv"
    df = pd.read_csv(infile)

    X=df[df.columns[:3]]
    y=df["survivalStatus"]
    #print(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    Tree = tree.DecisionTreeClassifier()
    Tree.fit(X_train,y_train)
    tree.plot_tree(Tree)
    #plt.show()
    
    print(Tree.score(X_train,y_train))
    print(Tree.score(X_test,y_test))

    print("features: "+str(df.columns[:3]))
    print("importance: "+str(Tree.feature_importances_ ))

    Tree2 = tree.DecisionTreeClassifier(max_depth=5,max_leaf_nodes=20,min_samples_leaf=3)
    Tree2.fit(X_train,y_train)
    
    print(Tree2.score(X_train,y_train))
    print(Tree2.score(X_test,y_test))

def main():
    part1()
    part2()

if __name__=="__main__":
    main()