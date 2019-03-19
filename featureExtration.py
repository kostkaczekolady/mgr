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

# def delete_silence():



def visualization(y, sr, xlabel, ylabel, title):
    plt.rcParams['figure.figsize'] = (14, 4)
    lr.display.waveplot(y, sr=sr)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

def read_single_sxamples(path, filename):
    y, sr = lr.load(path+filename, duration=0.5)
    y = normalize(y)
    mfccs = librosa.feature.mfcc(y=y, sr=sr)
    new_mfccs = np.resize(mfccs, (mfccs.size))
    hop_length = 512
    n_fft = 2048
    sfft = librosa.stft(y, n_fft=n_fft, hop_length=hop_length)
    new_sfft = np.resize(sfft, (sfft.size))
    new_sfft_realreal = new_sfft.real
    vector_mfccs_sfft = np.concatenate((new_mfccs, new_sfft_realreal), axis=0)
    # print(vector_mfccs_sfft.shape)
    visualization(y, sr, "samples", "amplitude", filename[:-4])
    return vector_mfccs_sfft

def read_examples():
    all_music_files = glob('./baza' + '/*.mp3')
    music_files_names = []
    list_samples = []
    print(all_music_files)
    for x in all_music_files:
        music_files_names.append(x[7:])
    print(music_files_names)
    for x in music_files_names:
        list_samples.append(read_single_sxamples('./baza/', x))
    matrix_extration = np.array(list_samples)
    return matrix_extration


def pca():
    matrix_extration = read_examples()
    pca = PCA(n_components=8)
    pcaArray = pca.fit_transform(matrix_extration)
    return pcaArray



