from glob import glob
from featureExtration import *
from instrumentsCoding import *
from sklearn.svm import SVC
from sklearn.metrics import balanced_accuracy_score
# from sklearn.preprocessing import OneHotEncoder
# Wczytywanie zbiorow
read_examples()

data_dir = './smalldataset'
audio_files = glob(data_dir + '/*.mp3')

X = pca()
Y = np.array(data)

#cello clarinet01,guitar 001, cello+clarinet 0001 cello+guitar 00001, clarinet+guitar 000001 cello+clarinet+gyitar 0000001


#trenujemy dla guitar
guitar_traing_Y = (Y[20:, 0])
guitar_traing_X = X[20:,:]

guitar_test_Y = Y[:20,0]
guitar_test_X = X[:20,:]
print(guitar_traing_X.shape, guitar_test_X.shape)


clf = SVC(gamma='auto', probability=True)
clf.fit(guitar_traing_X, guitar_traing_Y)

y_pred = clf.predict(guitar_test_X)
y_pp = clf.predict_proba(guitar_test_X)
print("predict", y_pred)
#print("accuracy dla guitar", clf.score(guitar_test_X, guitar_test_Y))

score = balanced_accuracy_score(guitar_test_Y, y_pred)
print(list(zip(y_pp, guitar_test_Y)))
print("%.3f" % score)
exit()

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
cello_Y = (Y[:90, 2])
cello_traing_X = X[:90,:]

cello_test_Y = Y[90:,2]
cello_test_X = X[90:,:]
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
cello_viola_triangle_traing_X = X[:50, :]

cello_viola_triangle_test_Y = Y[50:, 12]
cello_viola_triangle_test_X = X[50:, :]
print(cello_viola_triangle_traing_X.shape)

clf = SVC(gamma='auto')
clf.fit(cello_viola_triangle_traing_X, cello_viola_triangle_Y)

print("predict", clf.predict(cello_viola_triangle_test_X))
print("accuracy dla cello_viola_triangle", clf.score(cello_viola_triangle_test_X, cello_viola_triangle_test_Y))


print('Koniec programu')
