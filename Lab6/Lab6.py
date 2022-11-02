import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

path = ""
infile = "advertising.csv"

data_frame = pd.read_csv(path+infile)

sns.pairplot(data_frame,
             x_vars = ['TV','radio','newspaper'],
             y_vars = 'sales',
             height = 7, aspect = 0.7)
#plt.show()

# split our data frame into inputs (x) and output (y)
x = data_frame [['TV','radio','newspaper']]
y = data_frame ['sales']

# Create the model object and fit it to our x and y data:
model = LinearRegression()
linear_model = model.fit(x,y)
print("Intercept:", linear_model.intercept_)
print("Coefficients:", linear_model.coef_)
# have the model predict y for all inputs, so we can evaluate r2:
linear_model_predict = linear_model.predict(x)
print("r2 score:", r2_score(y, linear_model_predict))

# TODO - With three input features, we have seven useful combinations of features
# Build and fit a model for each combination of input features, and print out
# the r2 value for each.

sets = [['TV'],['radio'],['newspaper'],['TV','radio'],['TV','newspaper'],['radio','newspaper']]

for group in sets:
    print("____________________________________________________________________________________________________________________________________________")
    x = data_frame[group]
    print(group)
    
    model = LinearRegression()
    linear_model = model.fit(x,y)
    print("Intercept:", linear_model.intercept_)
    print("Coefficients:", linear_model.coef_)

    linear_model_predict = linear_model.predict(x)
    print("r2 score:", r2_score(y, linear_model_predict))