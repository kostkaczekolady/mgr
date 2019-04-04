import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import balanced_accuracy_score
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

    classifiers = []
    classifiers_acc = []
    for kernel in ['linear', 'poly', 'rbf', 'sigmoid', 'precomputed']:
        for C in [0.001, 0.01, 0.1, 1, 1.05]:
            for gamma in [1, 2, 3]:
                print(kernel, C, gamma)
                # tworzenie klasyfikatora
                clf = SVC(gamma=gamma, C=C, kernel=kernel, probability=True)
                check_classifiers = check_classifier(clf)
                # print("Średnia: ", check_classifiers)
                classifiers.append((kernel,C,gamma))
                classifiers_acc.append((check_classifiers))
    classifiers_acc_np = np.array(classifiers_acc)
    index = np.argmax(classifiers_acc_np)
    print(classifiers[index])
    print("koncowy wynik:", classifiers_acc[index])





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
exit()


# #trenujemy dla viola
# viola_Y = (Y[50:, 1])
# viola_traing_X = X[50:, :]
#
# viola_test_Y = Y[:50, 1]
# viola_test_X = X[:50, :]
# print(viola_traing_X.shape)
#
#
# # clf = SVC(gamma='auto')
# # clf.fit(viola_traing_X, viola_Y)
# #
# # print("predict", clf.predict(viola_test_X))
# # print("accuracy dla viola", clf.score(viola_test_X, viola_test_Y))
#
# #trenujemy dla cello
# cello_Y = (Y[:90, 2])
# cello_traing_X = X[:90,:]
#
# cello_test_Y = Y[90:,2]
# cello_test_X = X[90:,:]
# print(cello_traing_X.shape)
#
#
# clf = SVC(gamma='auto')
# clf.fit(cello_traing_X, cello_Y)
#
# print("predict", clf.predict(cello_test_X))
# print("accuracy dla cello", clf.score(cello_test_X, cello_test_Y))
#
# #trenujemy dla clarinetu
# clarinet_Y = (Y[:50,3])
# clarinet_traing_X = X[:50,:]
#
# clarinet_test_Y = Y[50:,3]
# clarinet_test_X = X[50:,:]
# print(clarinet_traing_X.shape)
#
# clf = SVC(gamma='auto')
# clf.fit(clarinet_traing_X, clarinet_Y)
#
# print("predict", clf.predict(clarinet_test_X))
# print("accuracy dla clarinet", clf.score(clarinet_test_X, clarinet_test_Y))
#
#
# #trenujemy dla cello+clarinetu
# clarinet_cello_Y = (Y[:50,4])
# clarinet_cello_traing_X = X[:50,:]
#
# clarinet_cello_test_Y = Y[50:,4]
# clarinet_cello_test_X = X[50:,:]
# print(clarinet_cello_traing_X.shape)
#
# clf = SVC(gamma='auto')
# clf.fit(clarinet_cello_traing_X, clarinet_cello_Y)
#
# print("predict", clf.predict(clarinet_cello_test_X))
# print("accuracy dla clarinet_cello", clf.score(clarinet_cello_test_X, clarinet_cello_test_Y))
#
#
# #trenujemy dla cello+viola
# cello_viola_Y = (Y[:50,6])
# cello_viola_traing_X = X[:50,:]
#
# cello_viola_test_Y = Y[50:,6]
# cello_viola_test_X = X[50:,:]
# print(cello_viola_traing_X.shape)
#
# clf = SVC(gamma='auto')
# clf.fit(cello_viola_traing_X, cello_viola_Y)
#
# print("predict", clf.predict(cello_viola_test_X))
# print("accuracy dla cello_viola", clf.score(cello_viola_test_X, cello_viola_test_Y))
#
#
# #trenujemy dla cello+viola+triangle
# cello_viola_triangle_Y = (Y[:50, 12])
# cello_viola_triangle_traing_X = X[:50, :]
#
# cello_viola_triangle_test_Y = Y[50:, 12]
# cello_viola_triangle_test_X = X[50:, :]
# print(cello_viola_triangle_traing_X.shape)
#
# clf = SVC(gamma='auto')
# clf.fit(cello_viola_triangle_traing_X, cello_viola_triangle_Y)
#
# print("predict", clf.predict(cello_viola_triangle_test_X))
# print("accuracy dla cello_viola_triangle", clf.score(cello_viola_triangle_test_X, cello_viola_triangle_test_Y))
#
#
# print('Koniec programu')
