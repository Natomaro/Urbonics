from sklearn import linear_model
#import statsmodels.api as sm
import pickle
import csv
import numpy as np
from scipy.optimize import minimize
import pandas as pd
from sklearn import datasets ## imports datasets from scikit-learn
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.models import model_from_json
from sklearn.neighbors import KNeighborsClassifier

#cancer = datasets.load_breast_cancer() ## loads Boston dataset from datasets library

#print("Features: ", cancer.feature_names)

# print the label type of cancer('malignant' 'benign')
#print("Labels: ", cancer.target_names)

#cancer.data.shape
#print(cancer.data[0:5])
#print(cancer.target)

df = pd.read_csv('fake_set.csv')
target = pd.read_csv('target_tag.csv')

X_train, X_test, y_train, y_test = train_test_split(df, target, test_size=0.4,random_state=109) # 70% training and 30% test

#Create a kNN Classifier
classifier = KNeighborsClassifier(n_neighbors=3)# Linear Kernel

#Train the model using the training sets
classifier.fit(X_train, y_train)

print("x test", X_test)
print(type(X_test))
#Predict the response for test dataset

y_pred = classifier.predict(X_test)
print(classifier)


pkl_filename = "model_svm.pkl"  
with open(pkl_filename, 'wb') as file:  
    pickle.dump(classifier, file)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

print("Precision:",metrics.precision_score(y_test, y_pred))

print("Recall:",metrics.recall_score(y_test, y_pred))
