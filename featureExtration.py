import numpy as np
import librosa.display
from glob import glob
import librosa as lr
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def normalize(y):
    max_y = np.amax(y)
    min_y = np.abs(np.amin(y))
    if max_y > min_y:
        norma = max_y
    else:
        norma = min_y
    y = y / norma
    return y


def visualization(y, sr, xlabel, ylabel, title):
    plt.rcParams['figure.figsize'] = (14, 4)
    lr.display.waveplot(y, sr=sr)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

def readSingleExamples(path, filename):
    y, sr = lr.load(path+filename, duration=0.5)
    y = normalize(y)
    mfccs = librosa.feature.mfcc(y=y, sr=sr)
    newMFCSS = np.resize(mfccs, (mfccs.size))
    hop_length = 512
    n_fft = 2048
    sfft = librosa.stft(y, n_fft=n_fft, hop_length=hop_length)
    newSFT = np.resize(sfft, (sfft.size))
    newSFTreal = newSFT.real
    newVector = np.concatenate((newMFCSS, newSFTreal), axis=0)
    # print(newVector.shape)
    visualization(y, sr, "samples", "amplitude", filename[:-4])
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
        list_samples.append(readSingleExamples('./baza/', x))
    matrix_extration = np.array(list_samples)
    return matrix_extration


def pca():
    matrix_extration = readExamples()
    pca = PCA(n_components=8)
    pcaArray = pca.fit_transform(matrix_extration)
    return pcaArray



