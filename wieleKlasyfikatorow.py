import numpy as np
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import balanced_accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_moons, make_circles, make_classification
# from sklearn.exceptions import DataConversionWarning
import warnings
# warnings.filterwarnings(action='ignore', category=DataConversionWarning)
with warnings.catch_warnings():
    warnings.simplefilter("ignore")

    X = np.load("inputs.npy")
    Y = np.load("labels.npy")
    Y = Y.flatten()


    def train_and_evaluate (X_train, X_test, Y_train, Y_test):
        #trenuje
        clf.fit(X_train, Y_train)
        #jak klasyfikator dziala na zbiorze testowym
        y_pred = clf.predict(X_test)
        y_pp = clf.predict_proba(X_test)
        fold_acc = clf.score(X_test, Y_test)
        # print("accuracy: ", fold_acc)
        score = balanced_accuracy_score(Y_test, y_pred)
        # print(list(zip(y_pp, Y_test)))
        # print("Balance accuracy %.3f" % score)
        return score, fold_acc


    skf = StratifiedKFold(n_splits=2, shuffle=True)


    def check_classifier (clf):
        acc = []
        for i in range(5):
            for train_index, test_index in skf.split(X, Y):
                X_train, X_test = X[train_index], X[test_index]
                Y_train, Y_test = Y[train_index], Y[test_index]
                score, fold_acc = train_and_evaluate(X_train, X_test, Y_train, Y_test)
                acc.append(fold_acc)
        return  sum(acc)/len(acc)


    names = ["Nearest Neighbors", "Linear SVM"]
    classifiers = [
        KNeighborsClassifier(3),
        SVC(gamma="3", C="150", kernel="linear", probability=True)
    ]
    classifiers_acc = []

    # clf = KNeighborsClassifier(n_neighbors=5)
    clf = DecisionTreeClassifier(random_state=0)
    check_classifiers = check_classifier(clf)
    print("Średnia: ", check_classifiers)
    # for name, clf in zip(names, classifiers):
    #     clf.fit(X_train, y_train)
    #     score = clf.score(X_test, y_test)

    # # for kernel in ['linear', 'rbf', 'sigmoid']:
    # #     for C in [0.000001, 0.001, 1, 10, 50, 105, 110, 150, 170, 200]:
    # #         for gamma in [1, 2, 3, 4, 4.5, 5, 5.5, 6, 6.5, 7, 8, 10]:
    # #             print(kernel, C, gamma)
    # #             # tworzenie klasyfikatora
    # #             clf = SVC(gamma=gamma, C=C, kernel=kernel, probability=True)
    # #             check_classifiers = check_classifier(clf)
    # #             # print("Średnia: ", check_classifiers)
    # #             classifiers.append((kernel,C,gamma))
    # #             classifiers_acc.append((check_classifiers))
    #
    #
    # classifiers_acc_np = np.array(classifiers_acc)
    # index = np.argmax(classifiers_acc_np)
    # print(classifiers[index])
    # print("koncowy wynik: ", classifiers_acc[index])





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
