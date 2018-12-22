from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from sklearn.model_selection import train_test_split
from pandas import read_csv
from sklearn.metrics import confusion_matrix

filename_mlp='allFeatures.csv'
dataframe_mlp = read_csv(filename_mlp)
array_mlp = dataframe_mlp.values

Y_mlp = array_mlp[:,0:71]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y_mlp, stratify=Y_mlp, test_size = 0.5, random_state=0)
X_train_extracted = X_train[:,indices[0:1000]]
X_test_extracted = X_test[:,indices[0:1000]]


model=Sequential()
model.Add(Dense(500, kernel_initializer='normal', activation='relu', input_dim=1000))
model.add(Dropout(0.5))
model.Add(Dense(250, kernel_initializer='normal', activation='relu'))
model.add(Dropout(0.5))
model.Add(Dense(125, kernel_initializer='normal', activation='relu'))
model.add(Dropout(0.5))
model.Add(Dense(71, kernel_initializer='normal', activation='sigmoid'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train_extracted, Y_train, epochs=50, batch_size=100)

scores = model.evaluate(X_test_extracted, Y_test)

for k, (train,test) in enumerate(kfold):
   model.fit(X_train_extracted[train], Y_train[train], epochs=10, batch_size=100)
   score = model.evaluate(X_train_extracted[test], Y_train[test])
   print('Fold: %s, Acc:%.4f' % (k+1, score[1]))

tree_train = model.evaluate(X_train_extracted, Y_train)
tree_test = model.evaluate(X_test_extracted, Y_test)
print('train/test accuracies %.4f/%.4f' % (tree_train[1], tree_test[1]))

y_test_pred_mlp = model.predict_classes(X_test_extracted, verbose=0)
confmat_mlp = confusion_matrix(y_true=Y_test, y_pred=y_test_pred_mlp)
print(confmat_mlp)
