perl -ne 'chomp;$i++;system "gtts-cli \"$_\" --lang de > $i.mp3"' Goethe-Zertifikat_A2_Wortliste.txt

