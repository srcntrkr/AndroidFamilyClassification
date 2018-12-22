from sklearn.model_selection import train_test_split
from pandas import read_csv
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
import numpy as np

filename = 'allFeatures.csv'
dataframe = read_csv(filename)
array = dataframe.values
X_full = array[:,0:28712]
Y_full = array[:,28712]

X=X_full.astype(np.float64)
Y=list(Y_full)

X_train_full,X_test_full,Y_train,Y_test = train_test_split(X,Y,stratify=Y,test_size=0.5,random_state=0)

feat_labels=dataframe.columns[1:]

LR=LogisticRegression(penalty='l2',C=0.1,random_state=0)
LR.fit(X_train_full, Y_train)

importances = LR.feature_importances_
indices = np.argsort(importances)[::-1]

X_extracted=X_full[:,indices[0:1000]]
X_train_extracted = X_train_full[:,indices[0:1000]]
X_test_extracted = X_test_full[:,indices[0:1000]]




