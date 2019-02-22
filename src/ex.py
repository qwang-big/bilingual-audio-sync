from mutagen.mp3 import MP3
lens = []
ex = [1059,110,1880,254,262,368,379,472,986]
for i in range(1,1996):
	if (i in ex):
		continue
	audio = MP3(str(i)+".mp3")
	lens.append(int(audio.info.length*1000))



