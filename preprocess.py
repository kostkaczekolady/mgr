from instrumentsCoding import *
from featureExtration import *


#Wczytywanie zbiorow
read_examples()

print("PCA w trakcie!")
# data_dir = './smalldataset'
# data_dir = './smalldatasetWaw'

X = pca()
Y = np.array(data)
print("X:", X)
print("Y: ", Y)
np.save("inputs.npy", X)
np.save("labels.npy", Y)

print("PCA gotowe!")