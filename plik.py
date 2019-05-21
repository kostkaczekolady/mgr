import numpy as np
np.set_printoptions(precision=3)


full = np.load("full.npy")
print("FULL")
mean_full = np.mean(full, axis=1)
print(mean_full)

smote = np.load("smote.npy")
print("SMOTE")
mean_smote = np.mean(smote, axis=1)
print(mean_smote)

indiv_full = np.load("separate_instrument.npy")
print("INDIV FULL")
mean_indiv_full = np.mean(indiv_full, axis=2).T
print(mean_indiv_full)


indiv_smote = np.load("separate_instrument_smote.npy")
print("INDIV SMOTE")
mean_indiv_smote = np.mean(indiv_smote, axis=2).T
print(mean_indiv_smote)
