from os import listdir
from os.path import isfile, join
from pydub import AudioSegment
import re


mypath = './baza/'
# mypath = './smalldataset/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

data = []
audio_segments = []
for f in onlyfiles:
    trimmed_name = re.sub("_\d+.mp3", "", re.sub("_\d+_", "+", f))
    print(trimmed_name)
    if trimmed_name == 'guitar':
        data.append([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    elif trimmed_name == 'viola':
        data.append([0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
    elif trimmed_name == 'cello':
        data.append([0, 0, 1, 0, 0, 0, 0, 0, 0, 0])
    elif trimmed_name == 'clarinet':
        data.append([0, 0, 0, 1, 0, 0, 0, 0, 0, 0])
    elif trimmed_name == 'cello+clarnet':
        data.append([0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
    elif trimmed_name == 'cello+guitar':
        data.append([0, 0, 0, 0, 0, 1, 0, 0, 0, 0])
    elif trimmed_name == 'cello+viola':
        data.append([0, 0, 0, 0, 0, 0, 1, 0, 0, 0])
    elif trimmed_name == 'clarnet+guitar':
        data.append([0, 0, 0, 0, 0, 0, 0, 1, 0, 0])
    elif trimmed_name == 'clarnet+viola':
        data.append([0, 0, 0, 0, 0, 0, 0, 0, 1, 0])
    elif trimmed_name == 'guitar+viola':
        data.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
    else:
        data.append([0, 0, 0, 0])



    audio_segments.append((f, AudioSegment.from_file(mypath + f)))

audio_segments_ovelayed = []
for as_idx, (file_name, audio_segment) in enumerate(audio_segments):
    for i in range(as_idx, len(audio_segments)):
        if file_name[:-6] == audio_segments[i][0][:-6]:
            continue
        audio_segments_ovelayed.append((
            file_name[:-4] + '_' + audio_segments[i][0][:-4],
            audio_segment.overlay(audio_segments[i][1])
        ))
# audio_segments_ovelayed jest krotką, pierwsza wartość to nazwa połączonych plików a druga to objekt AudioSegment overlayowany

for (file_name, audio_segment) in audio_segments_ovelayed:
    # print(file_name)
    file_path = "./smalldataset/"
    audio_segment.export(file_path + file_name + '.mp3', format='mp3')
