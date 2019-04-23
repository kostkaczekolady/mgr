from os import listdir
from os.path import isfile, join
from pydub import AudioSegment
import re

mypath = './dataset-3-instruments/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

data = []
for f in onlyfiles:
    trimmed_name = re.sub(".mp3", "", re.sub("_\d+_", "+", f))
    # print("zmieniona nazwa", trimmed_name)
    if trimmed_name == 'guitar':
        data.append([1])
    elif trimmed_name == 'viola':
        data.append([2])
    elif trimmed_name == 'cello':
        data.append([3])
    elif trimmed_name == 'clarinet':
        data.append([4])
    elif trimmed_name == 'guitar+trumpet':
        data.append([11])
    elif trimmed_name == 'viola+trumpet':
        data.append([12])
    elif trimmed_name == 'cello+trumpet':
        data.append([13])
    elif trimmed_name == 'clarinet+trumpet':
        data.append([14])
    elif trimmed_name == 'cello+clarinet+trumpet':
        data.append([15])
    elif trimmed_name == 'cello+guitar+trumpet':
        data.append([16])
    elif trimmed_name == 'cello+viola+trumpet':
        data.append([17])
    elif trimmed_name == 'clarinet+guitar+trumpet':
        data.append([18])
    elif trimmed_name == 'clarinet+viola+trumpet':
        data.append([19])
    elif trimmed_name == 'guitar+viola+trumpet':
        data.append([20])
    else:
        data.append([0])
        print("Nierozpoznany instr: ", trimmed_name)

print("Elementy zakodowane!")