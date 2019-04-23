# from coding2instruments import *
from coding.coding3instruments import *
from featureExtration import *

#Wczytywanie zbiorow
read_examples()

print("PCA w trakcie!")
# data_dir = './smalldatasetWaw'

X = pca()
Y = np.array(data)
# print("X: ", X)
# print("Y: ", Y)
# np.save("inputs.npy", X)
# np.save("labels.npy", Y)

np.save("inputs3.npy", X)
np.save("labels3.npy", Y)

print("PCA gotowe!")