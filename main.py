from glob import glob
from featureExtration import *
from instrumentsCoding import *
from sklearn.svm import SVC
# from sklearn.preprocessing import OneHotEncoder

data_dir = './smalldataset'
audio_files = glob(data_dir + '/*.mp3')

X = pca()
Y = np.array(data)

#cello clarinet01,guitar 001, cello+clarinet 0001 cello+guitar 00001, clarinet+guitar 000001 cello+clarinet+gyitar 0000001


#trenujemy dla guitar
guitar_Y = (Y[20:, 0])
guitar_traing_X = X[20:,:]

guitar_test_Y = Y[20:,0]
guitar_test_X = X[20:,:]
print(guitar_traing_X.shape)


clf = SVC(gamma='auto')
clf.fit(guitar_traing_X, guitar_Y)

print("predict", clf.predict(guitar_test_X))
print("accuracy dla guitar", clf.score(guitar_test_X, guitar_test_Y))


#trenujemy dla viola
viola_Y = (Y[50:, 1])
viola_traing_X = X[50:, :]

viola_test_Y = Y[:50, 1]
viola_test_X = X[:50, :]
print(viola_traing_X.shape)


# clf = SVC(gamma='auto')
# clf.fit(viola_traing_X, viola_Y)
#
# print("predict", clf.predict(viola_test_X))
# print("accuracy dla viola", clf.score(viola_test_X, viola_test_Y))

#trenujemy dla cello
cello_Y = (Y[:50,2])
cello_traing_X = X[:50,:]

cello_test_Y = Y[50:,2]
cello_test_X = X[50:,:]
print(cello_traing_X.shape)


clf = SVC(gamma='auto')
clf.fit(cello_traing_X, cello_Y)

print("predict", clf.predict(cello_test_X))
print("accuracy dla cello", clf.score(cello_test_X, cello_test_Y))

#trenujemy dla clarinetu
clarinet_Y = (Y[:50,3])
clarinet_traing_X = X[:50,:]

clarinet_test_Y = Y[50:,3]
clarinet_test_X = X[50:,:]
print(clarinet_traing_X.shape)

clf = SVC(gamma='auto')
clf.fit(clarinet_traing_X, clarinet_Y)

print("predict", clf.predict(clarinet_test_X))
print("accuracy dla clarinet", clf.score(clarinet_test_X, clarinet_test_Y))


#trenujemy dla cello+clarinetu
clarinet_cello_Y = (Y[:50,4])
clarinet_cello_traing_X = X[:50,:]

clarinet_cello_test_Y = Y[50:,4]
clarinet_cello_test_X = X[50:,:]
print(clarinet_cello_traing_X.shape)

clf = SVC(gamma='auto')
clf.fit(clarinet_cello_traing_X, clarinet_cello_Y)

print("predict", clf.predict(clarinet_cello_test_X))
print("accuracy dla clarinet_cello", clf.score(clarinet_cello_test_X, clarinet_cello_test_Y))


#trenujemy dla cello+viola
cello_viola_Y = (Y[:50,6])
cello_viola_traing_X = X[:50,:]

cello_viola_test_Y = Y[50:,6]
cello_viola_test_X = X[50:,:]
print(cello_viola_traing_X.shape)

clf = SVC(gamma='auto')
clf.fit(cello_viola_traing_X, cello_viola_Y)

print("predict", clf.predict(cello_viola_test_X))
print("accuracy dla cello_viola", clf.score(cello_viola_test_X, cello_viola_test_Y))


#trenujemy dla cello+viola+triangle
cello_viola_triangle_Y = (Y[:50, 12])
cello_viola_triangle_traing_X = X[:50,:]

cello_viola_triangle_test_Y = Y[50:,12]
cello_viola_triangle_test_X = X[50:,:]
print(cello_viola_triangle_traing_X.shape)

clf = SVC(gamma='auto')
clf.fit(cello_viola_triangle_traing_X, cello_viola_triangle_Y)

print("predict", clf.predict(cello_viola_triangle_test_X))
print("accuracy dla cello_viola_triangle", clf.score(cello_viola_triangle_test_X, cello_viola_triangle_test_Y))


print('Koniec programu')
