from os import listdir
from os.path import isfile, join
from pydub import AudioSegment

# mypath = './baza/'
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#
# audio_segments = []
# for f in onlyfiles:
#    audio_segments.append((f, AudioSegment.from_file(mypath + f)))
#
# audio_segments_ovelayed = []
# for as_idx, (file_name, audio_segment) in enumerate(audio_segments):
#     for i in range(as_idx, len(audio_segments)):
#         if file_name[:-6] == audio_segments[i][0][:-6]:
#             continue
#         audio_segments_ovelayed.append((
#             file_name[:-4] + '_' + audio_segments[i][0][:-4],
#             audio_segment.overlay(audio_segments[i][1])
#         ))
# # audio_segments_ovelayed jest krotką, pierwsza wartość to nazwa połączonych plików a druga to objekt AudioSegment overlayowany
#
# for (file_name, audio_segment) in audio_segments_ovelayed:
#     # print("wyeksportowane pliki do bazy:", file_name)
#     file_path = "./smalldataset/"
#     audio_segment.export(file_path + file_name + '.mp3', format='mp3')



mypath = './smalldataset/'
triangle = AudioSegment.("./baza2/triangle_1.mp3")

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print("Wszytskie pliki:", onlyfiles)
audio_segments = []
for f in onlyfiles:
    new = f + triangle
    # print(f[:-4]+ '_' + triangle)
    new.export('smalldataset/'+f[:-4]+'_'+triangle, format="mp3")



    #####

    wavs = [AudioSegment.from_wav(wav['./smalldataset']) for wav in wavset]
    combined = wavs[0]

    for wav in wavs[1:]:
        combined = combined.append(wav)

#
# sound1 = AudioSegment.from_wav("/path/to/file1.wav")
# sound2 = AudioSegment.from_wav("/path/to/file2.wav")
#
# combined_sounds = sound1 + sound2
# combined_sounds.export("/output/path.wav", format="wav")
#
#     audio_segments.append((f, AudioSegment.from_file(mypath + f)))
#
# audio_segments_ovelayed = []
# for as_idx, (file_name, audio_segment) in enumerate(audio_segments):
#     # for i in range(as_idx, len(audio_segments)):
#     #     if file_name[:-6] == audio_segments[i][0][:-6]:
#     #         continue
#     audio_segments_ovelayed.append((
#         file_name[:-4] + '_' + triangle[:-4],
#         audio_segment.overlay(triangle[1])
#     ))
# # audio_segments_ovelayed jest krotką, pierwsza wartość to nazwa połączonych plików a druga to objekt AudioSegment overlayowany
#
# for (file_name, audio_segment) in audio_segments_ovelayed:
#     # print("wyeksportowane pliki do bazy:", file_name)
#     file_path = "./smalldataset/"
#     audio_segment.export(file_path + file_name + '.mp3', format='mp3')


#
# mypathDataset = './smalldataset/'
# onlyfiles2 = [f for f in listdir(mypathDataset) if isfile(join(mypathDataset, f))]
#
# audio_segments2 = []
# for f in onlyfiles2:
#     audio_segments2.append((f, AudioSegment.from_file(mypathDataset + f)))
#
# print("Cały dataset:", audio_segments2)
#
# triangle = AudioSegment.from_file("./baza2/triangle_1.mp3")
# audio_segments_ovelayed2 = []
# for as_idx, (file_name, audio_segment) in enumerate(audio_segments2):
#     for i in range(as_idx, len(audio_segments2)):
#         if file_name[:-6] == audio_segments2[i][0][:-6]:
#             continue
#         audio_segments_ovelayed2.append((
#             file_name[:-4] + '_' + triangle[0][:-4],
#             audio_segment.overlay(triangle[1])
#         ))
# # audio_segments_ovelayed jest krotką, pierwsza wartość to nazwa połączonych plików a druga to objekt AudioSegment overlayowany
# print("co wyszlo", audio_segments_ovelayed2)
#
# for (file_name, audio_segment) in audio_segments_ovelayed2:
#     # print("wyeksportowane pliki do bazy:", file_name)
#     file_path = "./smalldataset/"
#     audio_segment.export(file_path + file_name + '.mp3', format='mp3')




# # path = './smalldataset'
# # pathTriangles = './baza2'
# # cello_1_clarinet_1 = AudioSegment.from_file("./smalldataset/cello_1_clarinet_1.mp3")
# # cello_2_viola_1 = AudioSegment.from_file("./smalldataset/cello_2_viola_1.mp3")
# # cello_1_viola_1 = AudioSegment.from_file("./smalldataset/cello_2_viola_1.mp3")
# # cello_3_viola_1 = AudioSegment.from_file("./smalldataset/cello_2_viola_1.mp3")
# # clarinet_1_guitar_2 = AudioSegment.from_file("./smalldataset/clarinet_1_guitar_2.mp3")
# #
# # triangle_1 = AudioSegment.from_file("./baza2/triangle_1.mp3")
# #
# # cello_1_clarinet_1_triangle_1 = cello_1_clarinet_1.overlay(triangle_1)
# # cello_2_viola_1_triangle_1 = cello_2_viola_1.overlay(triangle_1)
# # cello_1_viola_1_triangle_1 = cello_1_viola_1.overlay(triangle_1)
# # cello_3_viola_1_triangle_1 = cello_3_viola_1.overlay(triangle_1)
# # clarinet_1_guitar_2_triangle_1 = clarinet_1_guitar_2.overlay(triangle_1)
# #
# #
# # cello_1_clarinet_1_triangle_1.export("./smalldataset/cello_1_clarinet_1_triangle_1.mp3", format='mp3')
# # cello_2_viola_1_triangle_1.export("./smalldataset/cello_2_viola_1_triangle_1.mp3", format='mp3')
# # cello_1_viola_1_triangle_1.export("./smalldataset/cello_1_viola_1_triangle_1.mp3", format='mp3')
# # cello_3_viola_1_triangle_1.export("./smalldataset/cello_3_viola_1_triangle_1.mp3", format='mp3')
# # # clarinet_1_guitar_2_triangle_1.export("./smalldataset/clarinet_1_guitar_2_triangle_1.mp3", format='mp3')
# #


