import numpy as np
from sklearn.cross_validation import StratifiedKFold
from sklearn.metrics import confusion_matrix

from sklearn.neighbors import KNeighborsClassifier

kfold = StratifiedKFold(y=Y_train,n_folds=10,random_state=1)
scores=[]

knn=KNeighborsClassifier(n_neighbors=5,p=2,metric='minkowski')


Y_train_array=np.asarray(Y_train)
for k, (train,test) in enumerate(kfold):
  knn.fit(X_train_extracted[train], Y_train_array[train])
  score = knn.score(X_train_extracted[test], Y_train_array[test])
  scores.append(score)
  print('Fold: %s, Acc:%.4f' % (k+1, score))

Y_train_pred = knn.predict(X_train_extracted)
Y_test_pred = knn.predict(X_test_extracted)
tree_train = accuracy_score(Y_train, Y_train_pred)
tree_test = accuracy_score(Y_test, Y_test_pred)
print('train/test accuracies %.4f/%.4f' % (tree_train, tree_test))


confmat = confusion_matrix(y_true=Y_test, y_pred=Y_test_pred)
print(confmat)
