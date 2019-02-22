from googletrans import Translator
de, en = [],[]
translator = Translator()
with open("Goethe-Zertifikat_A2_Wortliste.txt") as fp:  
	for line in fp:
		de.append(line)


fp.close()
for i in range(0,len(de)-1,50):
	en.append(translator.translate(''.join(de[i:i+50]), src='de').text)


with open('Goethe-Zertifikat_A2_Wortliste_en.txt', 'w') as f:
	for i in range(0,len(en)-1):
		f.write("%s\n" % en[i])

f.close()
