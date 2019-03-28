import numpy as np
import librosa.display
from glob import glob
import librosa as lr
from pydub import AudioSegment
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
#
# def convert_mp3_to_wav():
#
#     files = [f for f in listdir('./baza') if isfile(join('mp3/', f))]
#     for file in files:
#         print('Converting %s' % file)
#         sound = AudioSegment.from_mp3("mp3/%s" % file)
#         sound.export("wav/%s.wav" % file.split('.')[0], format="wav")

def visualization(y, sr, xlabel, ylabel, title):
    plt.rcParams['figure.figsize'] = (14, 4)
    lr.display.waveplot(y, sr=sr)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    # plt.show()

def read_single_sxamples(path, filename):
    y, sr = lr.load(path+filename, duration=0.3)
    y = normalize(y)
    mfccs = librosa.feature.mfcc(y=y, sr=sr)
    new_mfccs = np.resize(mfccs, (mfccs.size))
    hop_length = 512
    n_fft = 2048
    sfft = librosa.stft(y, n_fft=n_fft, hop_length=hop_length)
    new_sfft = np.resize(sfft, (sfft.size))
    new_sfft_realreal = new_sfft.real
    vector_mfccs_sfft = np.concatenate((new_mfccs, new_sfft_realreal), axis=0)
    # print("rozmiar vectora: ", vector_mfccs_sfft.shape)
    # visualization(y, sr, "samples", "amplitude", filename[:-4])
    # print("vector: ", vector_mfccs_sfft)
    return vector_mfccs_sfft

def read_examples():
    all_music_files = glob('./smalldataset' + '/*.mp3')
    music_files_names = []
    list_samples = []
    # print("Wszystkie pliki w ./smalldataset:", all_music_files)
    for x in all_music_files:
        music_files_names.append(x[15:])
    print("Wszystkie pliki w ./smalldataset:", music_files_names)
    for x in music_files_names:
        list_samples.append(read_single_sxamples('./smalldataset/', x))
        print("tablica pojedynczych plików:", list_samples)
    matrix_extration = np.array(list_samples)
    print("macierz:", matrix_extration)
    return matrix_extration

def pca():
    matrix_extration = read_examples()
    pca = PCA(n_components=2)
    pcaArray = pca.fit_transform(matrix_extration)
    print (pcaArray)
    return pcaArray