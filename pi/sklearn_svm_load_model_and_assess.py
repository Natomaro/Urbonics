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

def classify_plant(ph,EC,percent_light,water_level):
	with open('model_svm.pkl', 'rb') as file:  
	    classifier = pickle.load(file)


	test_pass = pd.np.array([[ph,EC,percent_light,water_level]])
	

	# test_pass = pd.np.array([[6.391, 1.6, 0.71 ,7.3]])
	# test_fail = pd.np.array([[6.5, 1.5, 0.82 ,6.5]])
	# test_bad = pd.np.array([[6.15, 1.75, 0.61 ,8]])
	predict = classifier.predict(test_pass)  
	# print(Ypredict)

	# Failpredict = classifier.predict(test_fail)  
	# print(Failpredict)

	# badpredict = classifier.predict(test_bad)  
	# print(badpredict)
	# predict = classifier.predict(test)
	# print(predict)
	return predict
