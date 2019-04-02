from os import listdir
from os.path import isfile, join
from pydub import AudioSegment
import glob
import os, fnmatch

mypath = './baza/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

audio_segments = []
for f in onlyfiles:
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
    # print("wyeksportowane pliki do bazy:", file_name)
    file_path = "./smalldataset/"
    audio_segment.export(file_path + file_name + '.mp3', format='mp3')



path = './smalldataset'
pathTriangles = './baza2'
cello_1_clarinet_1 = AudioSegment.from_file("./smalldataset/cello_1_clarinet_1.mp3")
cello_2_viola_1 = AudioSegment.from_file("./smalldataset/cello_2_viola_1.mp3")
cello_1_viola_1 = AudioSegment.from_file("./smalldataset/cello_2_viola_1.mp3")
cello_3_viola_1 = AudioSegment.from_file("./smalldataset/cello_2_viola_1.mp3")
clarinet_1_guitar_2 = AudioSegment.from_file("./smalldataset/clarinet_1_guitar_2.mp3")

triangle_1 = AudioSegment.from_file("./baza2/triangle_1.mp3")

cello_1_clarinet_1_triangle_1 = cello_1_clarinet_1.overlay(triangle_1)
cello_2_viola_1_triangle_1 = cello_2_viola_1.overlay(triangle_1)
cello_1_viola_1_triangle_1 = cello_1_viola_1.overlay(triangle_1)
cello_3_viola_1_triangle_1 = cello_3_viola_1.overlay(triangle_1)
clarinet_1_guitar_2_triangle_1 = clarinet_1_guitar_2.overlay(triangle_1)


cello_1_clarinet_1_triangle_1.export("./smalldataset/cello_1_clarinet_1_triangle_1.mp3", format='mp3')
cello_2_viola_1_triangle_1.export("./smalldataset/cello_2_viola_1_triangle_1.mp3", format='mp3')
cello_1_viola_1_triangle_1.export("./smalldataset/cello_1_viola_1_triangle_1.mp3", format='mp3')
cello_3_viola_1_triangle_1.export("./smalldataset/cello_3_viola_1_triangle_1.mp3", format='mp3')
# clarinet_1_guitar_2_triangle_1.export("./smalldataset/clarinet_1_guitar_2_triangle_1.mp3", format='mp3')

