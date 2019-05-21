import numpy as np
import librosa.display
from glob import glob
import librosa as lr
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


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
    scaler = StandardScaler()
    print(y, y.shape)
    scaler.fit(y.reshape(-1,1))
    y = np.squeeze(scaler.transform(y.reshape(-1,1)))
    print(y, y.shape)

    #exit()
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
    all_music_files = glob('./dataset-2-instruments' + '/*.mp3')
    # all_music_files = glob('./dataset-3-instruments' + '/*.mp3')
    print("all_music_files: ", len(all_music_files))
    music_files_names = []
    list_samples = []
    for x in all_music_files:
        # music_files_names.append(x[9:])
        music_files_names.append(x[24:])
    for x in music_files_names:
        list_samples.append(read_single_sxamples('./dataset-2-instruments/', x))
        # list_samples.append(read_single_sxamples('./dataset-3-instruments/', x))
    matrix_extration = np.array(list_samples)
    print(matrix_extration.shape)
    return matrix_extration

def pca():
    matrix_extration = read_examples()
    pca = PCA(n_components=32)
    pcaArray = pca.fit_transform(matrix_extration)
    print("pca:", pcaArray.shape)
    return pcaArray

# print("Ekstrakcja zakończona")