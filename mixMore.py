from pydub import AudioSegment

path = './smalldataset'
pathTriangles = './baza2'
cello_01_clarinet_01 = AudioSegment.from_file("./smalldataset/cello_01_clarinet_01.mp3")
cello_02_viola_01 = AudioSegment.from_file("./smalldataset/cello_02_viola_01.mp3")
cello_01_viola_01 = AudioSegment.from_file("./smalldataset/cello_02_viola_01.mp3")
cello_03_viola_01 = AudioSegment.from_file("./smalldataset/cello_02_viola_01.mp3")
clarinet_01_guitar_02 = AudioSegment.from_file("./smalldataset/clarinet_01_guitar_02.mp3")

triangle_1 = AudioSegment.from_file("./baza2/triangle_1.mp3")
triangle_2 = AudioSegment.from_file("./baza2/triangle_2.mp3")

cello_01_clarinet_01_triangle_1 = cello_01_clarinet_01.overlay(triangle_1)
cello_02_viola_01_triangle_1 = cello_02_viola_01.overlay(triangle_1)
cello_01_viola_01_triangle_1 = cello_01_viola_01.overlay(triangle_1)
cello_03_viola_01_triangle_1 = cello_03_viola_01.overlay(triangle_1)
clarinet_01_guitar_02_triangle_1 = clarinet_01_guitar_02.overlay(triangle_1)
cello_01_clarinet_01_triangle_2 = cello_01_clarinet_01.overlay(triangle_2)
cello_02_viola_01_triangle_2 = cello_02_viola_01.overlay(triangle_2)
cello_01_viola_01_triangle_2 = cello_01_viola_01.overlay(triangle_2)
cello_03_viola_01_triangle_2 = cello_03_viola_01.overlay(triangle_2)
clarinet_01_guitar_02_triangle_2 = clarinet_01_guitar_02.overlay(triangle_2)


cello_01_clarinet_01_triangle_1.export("./smalldataset/cello_01_clarinet_01_triangle_1.mp3", format='mp3')
cello_02_viola_01_triangle_1.export("./smalldataset/cello_02_viola_01_triangle_1.mp3", format='mp3')
cello_01_viola_01_triangle_1.export("./smalldataset/cello_01_viola_01_triangle_1.mp3", format='mp3')
cello_03_viola_01_triangle_1.export("./smalldataset/cello_03_viola_01_triangle_1.mp3", format='mp3')
cello_01_clarinet_01_triangle_2.export("./smalldataset/cello_01_clarinet_01_triangle_2.mp3", format='mp3')
cello_02_viola_01_triangle_2.export("./smalldataset/cello_02_viola_01_triangle_2.mp3", format='mp3')
cello_01_viola_01_triangle_2.export("./smalldataset/cello_01_viola_01_triangle_2.mp3", format='mp3')
cello_03_viola_01_triangle_2.export("./smalldataset/cello_03_viola_01_triangle_2.mp3", format='mp3')
# clarinet_1_guitar_2_triangle_1.export("./smalldataset/clarinet_1_guitar_2_triangle_1.mp3", format='mp3')


# 
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# 
# audio_segments = []
# for f in onlyfiles:
#     audio_segments.append((f, AudioSegment.from_file(mypath + f)))
#     # print("siemka:", audio_segments)
# 
# audio_segments_ovelayed = []
# for as_idx, (file_name, audio_segment) in enumerate(audio_segments):
#     for i in range(as_idx, len(audio_segments)):
#         if file_name[:-7] == audio_segments[i][0][:-7]:
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
#     # file_path = "./smalldatasetWav/"
#     audio_segment.export(file_path + file_name + '.mp3', format='mp3')
#     # audio_segment.export(file_path + file_name + '.wav', format='wav')
# 
# print("Mix wykonany")
