from os import listdir, remove
from os.path import isfile, join
from pydub import AudioSegment



mypath = './baza/'
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


FILES = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(FILES)
# Petla po wszytkich utworach
for file in FILES:
    # Konwersja na format wav
    print('Converting %s' % file)
    sound = AudioSegment.from_mp3("./baza/%s" % file)
    sound.export("wav/%s.wav" % file.split('.')[0], format="wav")

    # Podajemy sciezke do pliku wav
    wave_file = ("wav/%s.wav" % file.split('.')[0])
    #
    # # Wczytujemy plik wav
    # sample_rate, stereo_sound = wavfile.read(wave_file)
