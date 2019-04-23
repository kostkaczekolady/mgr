from os import listdir
from os.path import isfile, join
from pydub import AudioSegment
import re

mypath = './dataset-2-instruments/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

data = []
for f in onlyfiles:
    # trimmed_name = re.sub(".mp3", "", re.sub("_\d+_", "+", f))
    trimmed_name = re.sub("_\d+.mp3", "", re.sub("_\d+_", "+", f))
    # print("zmieniona nazwa: ", trimmed_name)
    if trimmed_name == 'guitar':
        data.append([1])
    elif trimmed_name == 'viola':
        data.append([2])
    elif trimmed_name == 'cello':
        data.append([3])
    elif trimmed_name == 'clarinet':
        data.append([4])
    elif trimmed_name == 'cello+clarinet':
        data.append([5])
    elif trimmed_name == 'cello+guitar':
        data.append([6])
    elif trimmed_name == 'cello+viola':
        data.append([7])
    elif trimmed_name == 'clarinet+guitar':
        data.append([8])
    elif trimmed_name == 'clarinet+viola':
        data.append([9])
    elif trimmed_name == 'guitar+viola':
        data.append([10])
    else:
        data.append([0])
        print("Nierozpoznany instr: ", trimmed_name)

print("Elementy zakodowane!")