import numpy as np
from sklearn.cross_validation import StratifiedKFold
from sklearn.metrics import confusion_matrix

from sklearn.ensemble import RandomForestClassifier

kfold = StratifiedKFold(y=Y_train,n_folds=10,random_state=1)
scores=[]

forest=RandomForestClassifier(n_estimators=10000, random_state=0,n_jobs=-1)

Y_train_array=np.asarray(Y_train)
for k, (train,test) in enumerate(kfold):
  forest.fit(X_train_extracted[train], Y_train_array[train])
  score = forest.score(X_train_extracted[test], Y_train_array[test])
  scores.append(score)
  print('Fold: %s, Acc:%.4f' % (k+1, score))

Y_train_pred = forest.predict(X_train_extracted)
Y_test_pred = forest.predict(X_test_extracted)
tree_train = accuracy_score(Y_train, Y_train_pred)
tree_test = accuracy_score(Y_test, Y_test_pred)
print('train/test accuracies %.4f/%.4f' % (tree_train, tree_test))


confmat = confusion_matrix(y_true=Y_test, y_pred=Y_test_pred)
print(confmat)
