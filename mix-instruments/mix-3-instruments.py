from pydub import AudioSegment
from os import listdir
from os.path import isfile, join

path = './dataset-2-instruments/'
trumpet = 'trumpet.mp3'

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

audio_segments = []
for f in onlyfiles:
    audio_segments.append(f)

trumpet_segment = AudioSegment.from_file(trumpet)

file_path = "./dataset-3-instruments/"
for file_name in audio_segments:
    audio_segment = AudioSegment.from_file(path + file_name)
    new_name = file_name[:-4] + '_' + trumpet[:-4]
    audiosegment_overlay = audio_segment.overlay(trumpet_segment)
    audiosegment_overlay.export(file_path + new_name + '.mp3', format='mp3')
    # print("wyeksportowane pliki do bazy:", new_name)

print("Mix wykonany")
