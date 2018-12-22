import numpy as np
from sklearn.cross_validation import StratifiedKFold
from sklearn.metrics import confusion_matrix

from sklearn.linear_model import LogisticRegression

kfold = StratifiedKFold(y=Y_train,n_folds=10,random_state=1)
scores=[]

LR=LogisticRegression(penalty='l2',C=0.1,random_state=0)

Y_train_array=np.asarray(Y_train)
for k, (train,test) in enumerate(kfold):
  LR.fit(X_train_extracted[train], Y_train_array[train])
  score = LR.score(X_train_extracted[test], Y_train_array[test])
  scores.append(score)
  print('Fold: %s, Acc:%.4f' % (k+1, score))

Y_train_pred = LR.predict(X_train_extracted)
Y_test_pred = LR.predict(X_test_extracted)
tree_train = accuracy_score(Y_train, Y_train_pred)
tree_test = accuracy_score(Y_test, Y_test_pred)
print('train/test accuracies %.4f/%.4f' % (tree_train, tree_test))


confmat = confusion_matrix(y_true=Y_test, y_pred=Y_test_pred)
print(confmat)
