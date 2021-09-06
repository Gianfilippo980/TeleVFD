import serial
import feedparser
import time

vfd=serial.Serial("/dev/ttyS0")
#attiva porta seriale
vfd.write("123456789012345678901234567890123456789".encode())
#sposta il cursore nell'angolo in basso a destra, sono 39 caratteri
while True:
    Televideo_24ore=feedparser.parse('http://www.servizitelevideo.rai.it/televideo/pub/rss102.xml')
    #importa il feed "24 ore non stop" del Televideo
    n=len(Televideo_24ore.entries)
    #numero notizie
    for i in range(n):
        #i indicizza le notizie
        j=0
        #j conta i caratteri di ogni notizia che sono gioà stati visualizzati
        while j<len(Televideo_24ore.entries[i].title):
            if j==0:
                #aggiunge uno spazio all'inizio della notizia per morivi di formattazione
                testo=" "+Televideo_24ore.entries[i].title[j:j+19]
                j+=19
            else:
                testo=Televideo_24ore.entries[i].title[j:j+20]
                j+=20
            #Testo è una riga da inviare al display, minore o uguale a 20 caratteri.
            l=len(testo)
            if l<20:
                for k in range(20-l):
                    #questo ciclo serve a mantenere consisitente la lunghezza delle videate: 20 caratteri
                    testo+=" "
            vfd.write (testo.encode("cp437","replace"))
            time.sleep(3)