from glob import glob
from featureExtration import *
from sklearn.svm import SVC

data_dir = './baza'
audio_files = glob(data_dir + '/*.mp3')

pca_result = pca()
print(pca_result)

#cello -> 1 clarinet -> 2 guitar -> 3
Y = np.array([[1,0,0],
              [1,0,0],
              [1,0,0],
              [0,1,0],
              [0,1,0],
              [0,1,0],
              [0,0,1],
              [0,0,1],
              [0,0,1]])
first_column = (Y[:,0])
clf = SVC(gamma='auto')
clf.fit(pca_result, first_column)

print("predict", clf.predict(pca_result))
print("accu", clf.score(pca_result, first_column))