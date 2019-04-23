import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import balanced_accuracy_score, confusion_matrix
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
# from sklearn.exceptions import DataConversionWarning
from cnf_matrix import *
import warnings
# warnings.filterwarnings(action='ignore', category=DataConversionWarning)
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    # X = np.load("inputs.npy")
    # Y = np.load("labels.npy")
    X = np.load("inputs3.npy")
    Y = np.load("labels3.npy")
    Y = Y.flatten()
    # print(X.shape)


    def train_and_evaluate (X_train, X_test, Y_train, Y_test, clf):
        clf.fit(X_train, Y_train)
        y_pred = clf.predict(X_test)
        y_pp = clf.predict_proba(X_test)
        fold_acc = clf.score(X_test, Y_test)
        # print("accuracy: ", fold_acc)
        score = balanced_accuracy_score(Y_test, y_pred)
        # print(list(zip(y_pp, Y_test)))
        # print("Balance accuracy %.3f" % score)
        # print("fold_acc:", fold_acc)
        # print("score:", score)
        return score, fold_acc

    skf = StratifiedKFold(n_splits=2, shuffle=True)

    def check_classifier(clf):
        acc = []
        for i in range(5):
            for train_index, test_index in skf.split(X, Y):
                X_train, X_test = X[train_index], X[test_index]
                Y_train, Y_test = Y[train_index], Y[test_index]
                score, fold_acc = train_and_evaluate(X_train, X_test, Y_train, Y_test, clf)
                acc.append(fold_acc)
        return  sum(acc)/len(acc)

    classifiers = []
    classifiers_acc = []
    #dobieranie hyperparametrow
    #  for kernel in ['linear', 'poly', 'rbf', 'sigmoid', 'precomputed']:
    #  #linear i precomputed nie dziala
    #     for C in [0.000001, 0.001, 1,  50, 105, 110, 150, 170, 200]:
    #       for gamma in [1, 3, 4, 4.5, 5, 5.5, 6, 6.5, 7, 8, 10]:
    #           print(kernel, C, gamma)
    #           # tworzenie klasyfikatora
    #           clf = SVC(gamma=gamma, C=C, kernel=kernel, probability=True)
    #           check_classifiers = check_classifier(clf)
    #           print("Średnia: ", check_classifiers)
    #           classifiers.append((kernel,C,gamma))
    #           classifiers_acc.append((check_classifiers))
    #   classifiers_acc_np = np.array(classifiers_acc)
    #   index = np.argmax(classifiers_acc_np)
    #   print(classifiers[index])
    #   print("koncowy wynik: ", classifiers_acc[index])


    # clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes = (15, 2), random_state = 1)



    clf = KNeighborsClassifier(2)
    # clf = SVC(gamma='auto', probability=True)
    check_classifiers = check_classifier(clf)
    print("Średnia: ", check_classifiers)

    cnf_matrix = confusion_matrix(Y, clf.predict(X))
    # print("y:", Y, " X: ", clf.predict(X), "liczba elementów", np.bincount(Y))
    np.set_printoptions(precision=2)

    plt.figure(figsize=(10, 10))
    # plot_confusion_matrix(cnf_matrix, classes=['guitar', 'viola', 'cello', 'clarinet', 'cello+clarinet', 'cello+guitar', 'cello+viola', 'clarinet+guitar', 'clarinet+viola', 'guitar+viola'],
    plot_confusion_matrix(cnf_matrix, classes=['guitar', 'viola', 'cello', 'clarinet','cello+clarinet','cello+guitar','cello+viola','clarinet+guitar','clarinet+viola','guitar_viola','guitar+trumpet', 'viola+trumpet', 'cello+trumpet', 'clarinet+trumpet', 'cello+clarinet+trumpet', 'cello+guitar+trumpet', 'cello+viola+trumpet', 'clarinet+guitar+trumpet', 'clarinet+viola+trumpet', 'guitar+viola+trumpet'],
                          title='Confusion matrix')

    plt.savefig('cnf_matrix/confusion_matrix_3_instruments+S_5CV_K2.png')
    plt.close()

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