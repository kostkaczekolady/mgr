from coding.coding2instruments import *
# from coding.coding3instruments import *
# from codingBinary.codingBinary3instruments import *
# from codingBinary.codingBinary2instruments import *
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

np.save("inputs2.npy", X)
np.save("labels2.npy", Y)

# np.save("inputs2_binary.npy", X)
# np.save("labels2_binary.npy", Y)

print(X.shape[0], Y.shape[0])

print("PCA gotowe!")