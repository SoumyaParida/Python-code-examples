
from sklearn.naive_bayes import GaussianNB
def classify(features_train, labels_train):
    clf = GaussianNB()
    clf.fit(features_train, labels_train)
    print clf.score(features_train, labels_train, sample_weight=None)
    return clf
### import the sklearn module for GaussianNB
### create classifier
### fit the classifier on the training features and labels
### return the fit classifier


### your code goes here!

