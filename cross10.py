import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import balanced_accuracy_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from cnf_matrix import *



X = np.load("inputs2.npy")
Y = np.load("labels2.npy")

Y = Y.flatten()

skf = StratifiedKFold(n_splits=10)
