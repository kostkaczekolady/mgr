from glob import glob
from featureExtration import *
from sklearn.svm import SVC

data_dir = './baza'
audio_files = glob(data_dir + '/*.mp3')

X = pca()
print(X)

#cello -> 1 clarinet -> 2 guitar -> 3
Y = np.array([[1,0,0],
              [1,0,0],
              [1,0,0],
              [0,1,0],
              [0,1,0],
              [0,1,0],
              [0,0,1],
              [0,0,1],
              [0,0,1],
              [0,0,0],
              [0,0,0],
              [0,0,0],
              [0,0,0],
              [0,0,0],
              [0,0,0],
              [0,0,0]])
first_column_traing_Y = (Y[:9,0])
traing_X = X[:9,:]

test_Y = Y[9:,0]
test_X = X[9:,:]
print(traing_X.shape)


clf = SVC(gamma='auto')
clf.fit(traing_X, first_column_traing_Y)

print("predict", clf.predict(test_X))
print("accu", clf.score(test_X, test_Y))

