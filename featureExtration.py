# Feature extraction example
import numpy as np
import librosa.display
from glob import glob
import librosa as lr
from sklearn.decomposition import PCA

def readsingleExamples(path, filename):
    y, sr = lr.load(path+filename, duration=0.5)
    mfccs = librosa.feature.mfcc(y=y, sr=sr)
    newMFCSS = np.resize(mfccs, (mfccs.size))
    hop_length = 512
    n_fft = 2048
    sfft = librosa.stft(y, n_fft=n_fft, hop_length=hop_length)
    newSFT = np.resize(sfft, (sfft.size))
    newSFTreal = newSFT.real
    newVector = np.concatenate((newMFCSS, newSFTreal), axis=0)
    # print(newVector.shape)
    return newVector

def readExamples():
    music_files = glob('./baza' + '/*.mp3')
    new_music_files = []
    list_samples = []
    print(music_files)
    for x in music_files:
        new_music_files.append(x[7:])
    print(new_music_files)
    for x in new_music_files:
        list_samples.append(readsingleExamples('./baza/', x))
    matrix_extration = np.array(list_samples)
    return matrix_extration


def pca():
    matrix_extration = readExamples()
    pca = PCA(n_components=8)
    pcaArray = pca.fit_transform(matrix_extration)
    return pcaArray


