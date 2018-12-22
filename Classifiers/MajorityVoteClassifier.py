import numpy as np
from sklearn.base import BaseEstimator
from sklearn.base import ClassifierMixin
from sklearn.preprocessing import LabelEncoder
from sklearn.externals import six
from sklearn.base import clone
from sklearn.pipeline import_name_estimators

class MajorityVoteClassifier(BaseEstimator, ClassifierMixin):
   
    def__init__(self,classifiers,vote='classlabel',weights=[8,1,1]):
	self.classifiers = classifiers
	self.named_classifiers = {key: value for key, value in _name_estimators(classifiers)}
	self.vote = vote
	self.weights = weights

    def fit(self, X, y):
	self.lablenc_ = LabelEncoder()
	self.lablenc_.fit(y)
	self.classes_ = self.lablenc_.classes_
        self.classifiers_ = []
	for clf in self.classifiers:
		fitted_clf = clone(clf).fit(X,self.lablenc_.transform(y))
		self.classifiers_.append(fitted_clf)
	return self

    def predict(self, X) :
	if self.vote == 'probability':
		maj_vote = np.argmax(self.predict_proba(X), axis=1)
	else:
		predictions = np.asarray([clf.predict(X) for clf in self.classifiers_]).T
		maj_vote = np.apply_along_axis(lambda x: np.argmax(np.bincount(x,weights=self.weights)),axis=1,arr=predictions)
	maj_vote = self.lablenc_.inverse_transform(maj_vote)
	return maj_vote

    def predict_proba(self, X):
	probas = np.asarray([clf.predict_proba(X) for clf in self.classifiers_])
	avg_proba = np.average(probas,axis=0, weights=self.weights)
	return avg_proba

    def get_params(self, deep=True):

	if not deep:
		return super(MajorityVoteClassifier,self).get_params(deep=False)
	else:
		out = self.named_classifiers.copy()
		for name, step in\
			six.iteritems(self.named_classifiers):
				for key, value in six.iteritems(step.get_params(deep=True)):out['%s__%s' % (name, key)] = value

