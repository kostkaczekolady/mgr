import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.base import clone
from sklearn.metrics import balanced_accuracy_score, confusion_matrix

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier

from tqdm import tqdm
from imblearn.over_sampling import SMOTE

_X = np.load("inputs2_binary.npy")
Y = np.load("labels2_binary.npy")

n = 20

X = _X[:, :n]

encoded_y = np.sum(Y * np.array([1,2,4,8])[None, :], axis=1)

print(np.unique(encoded_y, return_counts=True))

n_splits = 5
skf = StratifiedKFold(n_splits=n_splits, random_state=42)

classifiers = {
    '1NN': KNeighborsClassifier(1),
    'kNN': KNeighborsClassifier(),
    'DTC': DecisionTreeClassifier(),
    'SVC': SVC(gamma='scale'),
    'GNB': GaussianNB(),
    'MLP': MLPClassifier()
}

# SMOTE
scores = np.zeros((len(classifiers), n_splits))
skf = StratifiedKFold(n_splits=n_splits, random_state=42)
for f, (train, test) in enumerate(skf.split(X, encoded_y)):
    X_train, X_test = X[train], X[test]
    y_train, y_test = encoded_y[train], encoded_y[test]

    sm = SMOTE(random_state=42)
    X_res, y_res = sm.fit_resample(X_train, y_train)

    for clf_id, clf_n in enumerate(classifiers):
        clf = clone(classifiers[clf_n])
        clf.fit(X_res, y_res)
        y_pred = clf.predict(X_test)

        score = balanced_accuracy_score(y_test, y_pred)
        print(score)

        scores[clf_id, f] = score

np.save("smote", scores)

mean_scores = np.mean(scores, axis=1)
print(classifiers.keys())
print(mean_scores)


# Full
scores = np.zeros((len(classifiers), n_splits))
skf = StratifiedKFold(n_splits=n_splits, random_state=42)
for f, (train, test) in enumerate(skf.split(X, encoded_y)):
    X_train, X_test = X[train], X[test]
    y_train, y_test = encoded_y[train], encoded_y[test]

    for clf_id, clf_n in enumerate(classifiers):
        clf = clone(classifiers[clf_n])
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)

        score = balanced_accuracy_score(y_test, y_pred)

        scores[clf_id, f] = score
        print(score)

np.save("full", scores)


# Separate instruments
scores = np.zeros((len(classifiers), Y.shape[1], n_splits))
skf = StratifiedKFold(n_splits=n_splits, random_state=42)
for f, (train, test) in enumerate(skf.split(X, encoded_y)):
    X_train, X_test = X[train], X[test]

    for instrument_id, y in enumerate(Y.T):
        print(y, y.shape)
        y_train, y_test = y[train], y[test]

        for clf_id, clf_n in enumerate(classifiers):
            clf = clone(classifiers[clf_n])
            clf.fit(X_train, y_train)
            y_pred = clf.predict(X_test)

            score = balanced_accuracy_score(y_test, y_pred)
            scores[clf_id, instrument_id, f] = score

            print("%i %i %i %.3f" % (f, instrument_id, clf_id, score))

np.save("separate_instrument", scores)

# SMOTE Separate instruments
scores = np.zeros((len(classifiers), Y.shape[1], n_splits))
skf = StratifiedKFold(n_splits=n_splits, random_state=42)
for f, (train, test) in enumerate(skf.split(X, encoded_y)):
    X_train, X_test = X[train], X[test]

    for instrument_id, y in enumerate(Y.T):
        print(y, y.shape)
        y_train, y_test = y[train], y[test]

        sm = SMOTE(random_state=42)
        X_res, y_res = sm.fit_resample(X_train, y_train)

        for clf_id, clf_n in enumerate(classifiers):
            clf = clone(classifiers[clf_n])
            clf.fit(X_res, y_res)
            y_pred = clf.predict(X_test)

            score = balanced_accuracy_score(y_test, y_pred)
            scores[clf_id, instrument_id, f] = score

            print("%i %i %i %.3f" % (f, instrument_id, clf_id, score))

np.save("separate_instrument_smote", scores)



