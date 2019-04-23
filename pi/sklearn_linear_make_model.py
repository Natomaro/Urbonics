from sklearn import linear_model
#import statsmodels.api as sm
import csv
import numpy as np
from scipy.optimize import minimize
import pandas as pd
from sklearn import datasets ## imports datasets from scikit-learn
data = datasets.load_boston() ## loads Boston dataset from datasets library

#df = pd.DataFrame(data.data, columns=data.feature_names)
# Put the target (housing value -- MEDV) in another DataFrame
#target = pd.DataFrame(data.target, columns=["PRICE"])
#df.to_csv('boston.csv')
#target.to_csv('target.csv')

df = pd.read_csv('fake_set.csv')
target = pd.read_csv('target_time.csv')

print(type(df))
X = df
y = target["Time"]

lm = linear_model.LinearRegression()
model = lm.fit(X,y)
#print(model)
#print(lm)
print(X[0:5])
print(y[0:5])
predictions = lm.predict(X)
# print(X[0:5])
print(predictions[0:5])
#print(len(predictions))#[0:5])
J = min(predictions)
print(J)
pred = np.ndarray.tolist(predictions)
K = pred.index(J)
print(K)
print(type(K))
print(X[K:K+1])
# model = sm.OLS(y, X).fit()
# print("minimum")
# intercept = lm.intercept_
# print(intercept)
# dick = lm.get_params(intercept)
# print(dick)
# make the predictions by the model
# Print out the statistics

#print(model.summary())