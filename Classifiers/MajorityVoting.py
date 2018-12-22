import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

clf1 = SVC(kernel='poly',random_state=0,gamma=0.10,C=1.0)
clf2 = LogisticRegression(penalty='l2',C=0.1,random_state=0)
clf3 = KNeighborsClassifier(n_neighbors=5,p=2,metric='minkowski')

mv=MajorityVoteClassifier(classifiers=[clf1,clf2,clf3])

Y_train_array=np.asarray(Y_train)
for k, (train,test) in enumerate(kfold):
  mv.fit(X_train_extracted[train], Y_train_array[train])
  score = mv.score(X_train_extracted[test], Y_train_array[test])
  scores.append(score)
  print('Fold: %s, Acc:%.4f' % (k+1, score))

Y_train_pred = mv.predict(X_train_extracted)
Y_test_pred = mv.predict(X_test_extracted)
tree_train = accuracy_score(Y_train, Y_train_pred)
tree_test = accuracy_score(Y_test, Y_test_pred)
print('train/test accuracies %.4f/%.4f' % (tree_train, tree_test))

confmat = confusion_matrix(y_true=Y_test, y_pred=Y_test_pred)
print(confmat)
