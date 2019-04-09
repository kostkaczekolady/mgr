from os import listdir
from os.path import isfile, join
import librosa

mypath = './baza/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print("pliki", onlyfiles)

for f in onlyfiles:
   y, sr = librosa.load(mypath + f)
   yt, index = librosa.effects.trim(y)
   print(librosa.get_duration(y), librosa.get_duration(yt))
   librosa.output.write_wav('./bazaWavSkrocona/'+f[:-3]+'wav', yt, sr)

