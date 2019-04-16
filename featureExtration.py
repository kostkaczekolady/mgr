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
    # plt.show()

def read_single_sxamples(path, filename):
    # y, sr = lr.load(path+filename)
    y, sr = lr.load(path+filename, duration=0.3)
    # print(librosa.get_duration(y), filename)
    y = normalize(y)
    mfccs = librosa.feature.mfcc(y=y, sr=sr)
    new_mfccs = np.resize(mfccs, (mfccs.size))
    # print("mfcs rozmiar",new_mfccs.shape)
    hop_length = 512
    n_fft = 2048
    sfft = librosa.stft(y, n_fft=n_fft, hop_length=hop_length)
    new_sfft = np.resize(sfft, (sfft.size))
    new_sfft_realreal = new_sfft.real
    vector_mfccs_sfft = np.concatenate((new_mfccs, new_sfft_realreal), axis=0)
    # print("rozmiar: ", vector_mfccs_sfft.shape)
    # visualization(y, sr, "samples", "amplitude", filename[:-4])
    return vector_mfccs_sfft

def read_examples():
    # all_music_files = glob('./datasetskrocony' + '/*.mp3')
    all_music_files = glob('./test10' + '/*.mp3')
    # all_music_files = glob('./smalldatasetWav' + '/*.wav')
    music_files_names = []
    list_samples = []
    for x in all_music_files:
        music_files_names.append(x[9:])
        # music_files_names.append(x[18:])
    for x in music_files_names:
        # list_samples.append(read_single_sxamples('./datasetskrocony/', x))
        list_samples.append(read_single_sxamples('./test10/', x))
        # list_samples.append(read_single_sxamples('./smalldatasetWav/', x))
    matrix_extration = np.array(list_samples)
    print(matrix_extration.shape)
    return matrix_extration

def pca():
    matrix_extration = read_examples()
    pca = PCA(n_components=10)
    pcaArray = pca.fit_transform(matrix_extration)
    print("pca:", pcaArray.shape)
    return pcaArray

# print("Ekstrakcja zakończona :)")