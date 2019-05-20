import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import balanced_accuracy_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from cnf_matrix import *


# X = np.load("inputs.npy")
# Y = np.load("labels.npy")
#
# X = np.load("inputs3.npy")
# Y = np.load("labels3.npy")
#
X = np.load("inputs2.npy")
Y = np.load("labels2.npy")

Y = Y.flatten()

skf = StratifiedKFold(n_splits=10)

# clf = SVC(gamma='auto', probability=True)
clf = KNeighborsClassifier(1)
# clf = GaussianProcessClassifier(1.0 * RBF(1.0))

acc = []
for train_index, test_index in skf.split(X, Y):
    X_train, X_test =X[train_index], X[test_index]
    Y_train, Y_test =Y[train_index], Y[test_index]
    clf.fit(X_train, Y_train)
    y_pred = clf.predict(X_test)
    y_pp = clf.predict_proba(X_test)
    fold_acc= clf.score(X_test, Y_test)
    # print("accuracy: ", fold_acc)
    acc.append(fold_acc)

    score = balanced_accuracy_score(Y_test, y_pred)
    # print(list(zip(y_pp, Y_test)))
    # print("Balance accuracy %.3f" % score)

mean_acc = sum(acc)/len(acc)
print("Średnia acc: ", mean_acc)

cnf_matrix = confusion_matrix(Y, clf.predict(X))
print("y:", Y, " X: ", clf.predict(X), "liczba elementów", np.bincount(Y))
np.set_printoptions(precision=2)

plt.figure(figsize=(20, 15))
# plot_confusion_matrix(cnf_matrix, classes=['guitar', 'viola', 'cello', 'clarinet', 'cello+clarinet', 'cello+guitar', 'cello+viola', 'clarinet+guitar', 'clarinet+viola', 'guitar+viola'],
plot_confusion_matrix(cnf_matrix, classes=['guitar', 'viola', 'cello', 'clarinet', 'guitar+trumpet', 'viola+trumpet', 'cello+trumpet', 'clarinet+trumpet', 'cello+clarinet+trumpet', 'cello+guitar+trumpet', 'cello+viola+trumpet', 'clarinet+guitar+trumpet', 'clarinet+viola+trumpet', 'guitar+viola+trumpet'],
                      title='Confusion matrix')

plt.savefig('cnf_matrix/confusion_matrix_3_instruments_10CVK1_test.png')
plt.close()

# plt.show()



#wyplute labelki przez klasyfiaktor
# y_pred = clf.predict(guitar_test_X)
#
# #sprawdzic w dokumentacji -
# y_pp = clf.predict_proba(guitar_test_X)
# print("predict", y_pred)
# #print("accuracy dla guitar", clf.score(guitar_test_X, guitar_test_Y))
#
# score = balanced_accuracy_score(guitar_test_Y, y_pred)
# print(list(zip(y_pp, guitar_test_Y)))
# print("%.3f" % score)
# exit()
