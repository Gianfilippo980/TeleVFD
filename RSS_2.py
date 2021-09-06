import serial
import feedparser
import time

testo="Televideo RAI 24 ore"

def comando (istruzione):
    ordine=[istruzione]
    binario=bytes(ordine)
    vfd.write(binario)
#15 reset
#16 ignora primo carattere successivo imput
#20 cursore spento
#19 cursore acceso
#17 no scorrimento
#10 cambio riga
#9 un carattere a destra
#8 un carattere a sinistra
#31 cancella tutto e riporta il cursore in alto
#13 torna ad inizio riga

vfd=serial.Serial("/dev/ttyS0")
#attiva porta seriale
comando (31)
#azzeramento
comando (17)
comando (20)
#ninente scorrimento e niente cursore visibile ma il cursore, anche se inisibile, passa comunque da una riga all'altra
while True:
    Televideo_24ore=feedparser.parse('http://www.servizitelevideo.rai.it/televideo/pub/rss102.xml')
    #importa il feed "24 ore non stop" del Televideo
    n=len(Televideo_24ore.entries)
    #n numero notizie
    for i in range(n):
        #i indicizza le notizie
        j=0
        #j conta i caratteri di ogni notizia che sono gioà stati visualizzati
        while j<len(Televideo_24ore.entries[i].title):
            comando (13)
            #riporta il cursore a sinistra qualora fosse finito fuori posto
            vfd.write (testo.encode("cp437","replace"))
            #ristampare il testo precedente sulla prima riga
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