from os import listdir
from os.path import isfile, join
import librosa

mypath = './dataset-1-instrument/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# print("pliki", onlyfiles)

for f in onlyfiles:
   y, sr = librosa.load(mypath + f)
   yt, index = librosa.effects.trim(y)
   # print(librosa.get_duration(y), librosa.get_duration(yt), f)
   librosa.output.write_wav('./dataset-1-instrument-shorter/'+f[:-3]+'mp3', yt, sr)


print("Cisza usunięta!")
