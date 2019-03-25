from glob import glob
from featureExtration import *
from sklearn.svm import SVC

data_dir = './baza'
audio_files = glob(data_dir + '/*.mp3')

X = pca()
print(X)

#cello -> 0 clarinet -> 1 guitar -> 2 viola ->3
#oboe -> 0 clarinet -> 1 guitar -> 2 viola ->3
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

#trenujemy dla cello
first_column_traing_Y = (Y[:9,0])
traing_X = X[:9,:]

test_Y = Y[9:,0]
test_X = X[9:,:]
print(traing_X.shape)


clf = SVC(gamma='auto')
clf.fit(traing_X, first_column_traing_Y)

print("predict", clf.predict(test_X))
print("accuracy dla cello", clf.score(test_X, test_Y))
#
# #trenujemy dla clarnetu
# second_column_traing_Y = (Y[:9,1])
# traing_X = X[:9,:]
#
# test_Y = Y[9:,1]
# test_X = X[9:,:]
# print(traing_X.shape)
#
# clf = SVC(gamma='auto')
# clf.fit(traing_X, second_column_traing_Y)
#
# print("predict", clf.predict(test_X))
# print("accuracy dla clarnet", clf.score(test_X, test_Y))
#
#
# #trenujemy dla guitar
# third_column_traing_Y = (Y[:9,2])
# traing_X = X[:9,:]
#
# test_Y = Y[9:,2]
# test_X = X[9:,:]
# print(traing_X.shape)
#
# clf = SVC(gamma='auto')
# clf.fit(traing_X, third_column_traing_Y)
#
# print("predict", clf.predict(test_X))
# print("accuracy dla guitar", clf.score(test_X, test_Y))

# #trenujemy dla viola
# fourth_column_traing_Y = (Y[:9,3])
# traing_X = X[:9,:]
#
# test_Y = Y[9:,3]
# test_X = X[9:,:]
# print(traing_X.shape)
#
# clf = SVC(gamma='auto')
# clf.fit(traing_X, fourth_column_traing_Y)
#
# print("predict", clf.predict(test_X))
# print("accuracy dla viola", clf.score(test_X, test_Y))

print('Koniec programu')
