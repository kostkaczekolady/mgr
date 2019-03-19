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

# example_audio_file =

y, sr = lr.load('baza/cello_1.mp3', duration=10)
plt.figure()
plt.subplot(3, 1, 1)
librosa.display.waveplot(y, sr=sr)
plt.title('cello_1.mp3')


y, sr = librosa.load(librosa.util.example_audio_file(), offset=30, duration=5)
mfccs = librosa.feature.mfcc(y=y, sr=sr)
print("MFC:", mfccs.shape)
newMFCSS = np.resize(mfccs,(mfccs.size))
print("newMfcss", newMFCSS)

fft = librosa.fft_frequencies(sr=22050, n_fft=20)
print('***FFT***')
print(type(fft))
print(fft)

newVector = np.concatenate((newMFCSS, fft), axis=0)
print("vector", newVector)
pca = PCA(n_components=10)
pcaArray = pca.fit_transform(newVector)
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