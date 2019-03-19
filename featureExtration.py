# Feature extraction example
import numpy as np
from pathlib import Path
import pandas as pd
import librosa.display
import matplotlib.pyplot as plt
from glob import glob
import librosa as lr
import sklearn as sk
from sklearn.decomposition import PCA

data_dir = './baza'
audio_files = glob(data_dir + '/*.mp3')
# print(len(audio_files))

audio, sfreq = lr.load(audio_files[0])
time = np.arange(0, len(audio)) / sfreq
print(time)
print('***********************************')

def readsingleExamples(path, filename):
    y, sr = lr.load(path+filename, duration=1.5)
    mfccs = librosa.feature.mfcc(y=y, sr=sr)
    newMFCSS = np.resize(mfccs, (mfccs.size))
    hop_length = 512
    n_fft = 2048
    sfft = librosa.stft(y, n_fft=n_fft, hop_length=hop_length)
    newSFT = np.resize(sfft, (sfft.size))
    newSFTreal = newSFT.real
    newVector = np.concatenate((newMFCSS, newSFTreal), axis=0)
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

matrix_extration = readExamples()

pca = PCA(n_components=8)
pcaArray = pca.fit_transform(matrix_extration)
print(pcaArray)





#
# plt.figure(figsize=(10, 4))
# librosa.display.specshow(mfccs, x_axis='time')
# plt.colorbar()
# plt.title('MFCC')
# plt.tight_layout()
# plt.show()

# plt.show()
# mfccs = librosa.feature.mfcc(y, sr=fs)
# print (mfccs.shape)

# n0 = 9000
# n1 = 9100
# plt.figure(figsize=(14, 5))
# plt.plot(y[n0:n1])
# plt.grid()
#
# plt.show()
#
# zero_crossings = librosa.zero_crossings(y[n0:n1], pad=False)
# print(sum(zero_crossings))


#spectrum
# X = librosa.stft(y)
# Xdb = librosa.amplitude_to_db(abs(X))
# plt.figure(figsize=(14, 5))
# librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
# plt.colorbar()
# plt.show()

#skala logarytmiczna
# librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
# plt.colorbar()
# plt.show()


# %matplotlib inline
# import matplotlib.pyplot as plt
# import librosa.display
# plt.figure(figsize=(14, 5))
# librosa.display.waveplot(x, sr=sr)

# y, sr = librosa.load('baza/cello_2.mp3', offset=30, duration=5)
# librosa.feature.mfcc(y=y, sr=sr)
#
# plt.figure(figsize=(10, 4))
# librosa.display.specshow(mfccs, x_axis='time')
# plt.colorbar()
# plt.title('MFCC')
# plt.tight_layout()
#
# plt.show()
# #
# x, sr = librosa.load('baza/cello_2.mp3')
# librosa.display.waveplot(x, sr=sr)
#
# mfccs = librosa.feature.mfcc(x, sr=sr)
# print (mfccs.shape)
#
# #Displaying  the MFCCs:
# librosa.display.specshow(mfccs, sr=sr, x_axis='time')
#
# plt.show()