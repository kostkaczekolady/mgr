import matplotlib.pyplot as plt
import librosa as lr
import librosa.display




def visualization(y, sr, xlabel, ylabel, title):

    plt.rcParams['figure.figsize'] = (14, 4)
    lr.display.waveplot(y, sr=sr)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

filename = "./guitar_1.mp3"
y, sr = lr.load('./smalldataset/'+filename)
visualization(y, sr, "samples", "amplitude", 'guitar')

filename2 = "./guitar_1.mp3"


new = librosa.effects.trim(filename2)
visualization(y, sr, "samples", "amplitude", 'guitar2')
