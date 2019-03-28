import  librosa as lr
import glob
import os, fnmatch
from pydub import AudioSegment



path = './baza'
files = []
for root, dirnames, filenames in os.walk(path):
    for filename in fnmatch.filter(filenames, '*.mp3'):
        files.append(os.path.join(root, filename))
# print("pliki:", files)

cello_1 = AudioSegment.from_file("./baza/cello_1.mp3")
cello_2 = AudioSegment.from_file("./baza/cello_2.mp3")
cello_3 = AudioSegment.from_file("./baza/cello_3.mp3")

clarinet_1 = AudioSegment.from_file("./baza/clarinet_1.mp3")
clarinet_2 = AudioSegment.from_file("./baza/clarinet_2.mp3")
clarinet_3 = AudioSegment.from_file("./baza/clarinet_3.mp3")

guitar_1 = AudioSegment.from_file("./baza/guitar_1.mp3")
guitar_2 = AudioSegment.from_file("./baza/guitar_2.mp3")
guitar_3 = AudioSegment.from_file("./baza/guitar_3.mp3")


cello_1_clarinet_1 = cello_1.overlay(clarinet_1)
cello_1_clarinet_2 = cello_1.overlay(clarinet_2)
cello_1_clarinet_3 = cello_1.overlay(clarinet_3)

cello_2_clarinet_1 = cello_2.overlay(clarinet_1)
cello_2_clarinet_2 = cello_2.overlay(clarinet_2)
cello_2_clarinet_3 = cello_2.overlay(clarinet_3)

cello_3_clarinet_1 = cello_3.overlay(clarinet_1)
cello_3_clarinet_2 = cello_3.overlay(clarinet_2)
cello_3_clarinet_3 = cello_3.overlay(clarinet_3)

cello_1_guitar_1 = cello_1.overlay(guitar_1)
cello_1_guitar_2 = cello_1.overlay(guitar_2)
cello_1_guitar_3 = cello_1.overlay(guitar_3)

cello_2_guitar_1 = cello_2.overlay(guitar_1)
cello_2_guitar_2 = cello_2.overlay(guitar_2)
cello_2_guitar_3 = cello_2.overlay(guitar_3)

cello_3_guitar_1 = cello_3.overlay(guitar_1)
cello_3_guitar_2 = cello_3.overlay(guitar_2)
cello_3_guitar_3 = cello_3.overlay(guitar_3)


guitar_1_clarinet_1 = guitar_1.overlay(clarinet_1)
guitar_1_clarinet_2 = guitar_1.overlay(clarinet_2)
guitar_1_clarinet_3 = guitar_1.overlay(clarinet_3)

guitar_2_clarinet_1 = guitar_2.overlay(clarinet_1)
guitar_2_clarinet_2 = guitar_2.overlay(clarinet_2)
guitar_2_clarinet_3 = guitar_2.overlay(clarinet_3)

guitar_3_clarinet_1 = guitar_3.overlay(clarinet_1)
guitar_3_clarinet_2 = guitar_3.overlay(clarinet_2)
guitar_3_clarinet_3 = guitar_3.overlay(clarinet_3)

cello_1_clarinet_1.export("./smalldataset/cello_1_clarinet_1.mp3", format='mp3')
cello_1_clarinet_2.export("./smalldataset/cello_1_clarinet_2.mp3", format='mp3')
cello_1_clarinet_3.export("./smalldataset/cello_1_clarinet_3.mp3", format='mp3')

cello_2_clarinet_1.export("./smalldataset/cello_2_clarinet_1.mp3", format='mp3')
cello_2_clarinet_2.export("./smalldataset/cello_2_clarinet_2.mp3", format='mp3')
cello_2_clarinet_3.export("./smalldataset/cello_2_clarinet_3.mp3", format='mp3')

cello_3_clarinet_1.export("./smalldataset/cello_3_clarinet_1.mp3", format='mp3')
cello_3_clarinet_2.export("./smalldataset/cello_3_clarinet_2.mp3", format='mp3')
cello_3_clarinet_3.export("./smalldataset/cello_3_clarinet_3.mp3", format='mp3')

cello_1_guitar_1.export("./smalldataset/cello_1_guitar_1.mp3", format='mp3')
cello_1_guitar_2.export("./smalldataset/cello_1_guitar_2.mp3", format='mp3')
cello_1_guitar_3.export("./smalldataset/cello_1_guitar_3.mp3", format='mp3')

cello_2_guitar_1.export("./smalldataset/cello_2_guitar_1.mp3", format='mp3')
cello_2_guitar_2.export("./smalldataset/cello_2_guitar_2.mp3", format='mp3')
cello_2_guitar_3.export("./smalldataset/cello_2_guitar_3.mp3", format='mp3')

cello_3_guitar_1.export("./smalldataset/cello_3_guitar_1.mp3", format='mp3')
cello_3_guitar_2.export("./smalldataset/cello_3_guitar_2.mp3", format='mp3')
cello_3_guitar_3.export("./smalldataset/cello_3_guitar_3.mp3", format='mp3')

guitar_1_clarinet_1.export("./smalldataset/guitar_1_clarinet_1.mp3", format='mp3')
guitar_1_clarinet_2.export("./smalldataset/guitar_1_clarinet_2.mp3", format='mp3')
guitar_1_clarinet_3.export("./smalldataset/guitar_1_clarinet_3.mp3", format='mp3')

guitar_2_clarinet_1.export("./smalldataset/guitar_2_clarinet_1.mp3", format='mp3')
guitar_2_clarinet_2.export("./smalldataset/guitar_2_clarinet_2.mp3", format='mp3')
guitar_2_clarinet_3.export("./smalldataset/guitar_2_clarinet_3.mp3", format='mp3')

guitar_3_clarinet_1.export("./smalldataset/guitar_3_clarinet_1.mp3", format='mp3')
guitar_3_clarinet_2.export("./smalldataset/guitar_3_clarinet_2.mp3", format='mp3')
guitar_3_clarinet_3.export("./smalldataset/guitar_3_clarinet_3.mp3", format='mp3')
