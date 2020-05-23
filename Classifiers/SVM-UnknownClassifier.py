import numpy as np
from sklearn.svm import SVC

svm=SVC(kernel='poly',random_state=0,gamma=0.1,C=1)
svm.fit(X_train, Y_train)
result = svm.predict_proba(X_test)
print(result)
