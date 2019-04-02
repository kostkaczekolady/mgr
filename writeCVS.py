import librosa
import numpy as np
import os
import csv
import pandas as pd

import warnings
warnings.filterwarnings('ignore')


header = 'filename fft mfcc '
for i in range(1, 21):
    header += f' mfcc{i}'
header += ' label'
header = header.split()


file = open('data.csv', 'w', newline='')
with file:
    writer = csv.writer(file)
    writer.writerow(header)
genres = 'cello_1.mp3 cello_1_clarinet_1.mp3 cello_2.mp3 cello_2_clarinet_1.mp3 cello_3.mp3 cello_3_clarinet_1.mp3'.split()
# for g in genres:
for filename in os.listdir(f'./smalldataset'):
    songname = f'./smalldataset/{filename}'
    y, sr = librosa.load(songname, mono=True, duration=0.5)
    fft = librosa.stft(y, n_fft=2048, hop_length=512).real
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    to_append = f'{filename} {np.mean(mfcc)} {np.mean(fft)}'
    for e in mfcc:
        to_append += f' {np.mean(e)}'
    to_append += f''
    file = open('data.csv', 'a', newline='')
    with file:
        writer = csv.writer(file)
        writer.writerow(to_append.split())

data = pd.read_csv('data.csv')
data.head()
print(data)