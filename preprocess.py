from instrumentsCoding import *
from featureExtration import *

#Wczytywanie zbiorow
read_examples()

# data_dir = './smalldataset'

X = pca()
Y = np.array(data)

np.save("inputs.npy", X)
np.save("labels.npy", Y)