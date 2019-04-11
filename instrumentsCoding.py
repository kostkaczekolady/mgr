from os import listdir
from os.path import isfile, join
from pydub import AudioSegment
import re

mypath = './smalldatasetskrocony/'
# mypath = './smalldatasetWav/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

data = []
for f in onlyfiles:
    trimmed_name = re.sub("_\d+.mp3", "", re.sub("_\d+_", "+", f))
    # trimmed_name = re.sub("_\d+.wav", "", re.sub("_\d+_", "+", f))
    # print("zmieniona nazwa", trimmed_name)
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
    elif trimmed_name == 'guitar+clarinet':
        data.append([11])
    elif trimmed_name == 'cello+triangle':
        data.append([12])
    elif trimmed_name == 'clarinet+triangle':
        data.append([13])
    elif trimmed_name == 'guitar+triangle':
        data.append([14])
    elif trimmed_name == 'triangle+viola':
        data.append([15])
    elif trimmed_name == 'cello+clarinet+triangle':
        data.append([16])
    elif trimmed_name == 'cello+viola+triangle':
        data.append([17])
    elif trimmed_name == 'clarinet+guitar+triangle':
        data.append([18])
    else:
        data.append([0])
        print("Nierozpoznany instr: ", trimmed_name)

print("Elementy zakodowane!")