import serial
import feedparser
import time

testo="Televideo RAI 24 ore"
#Since new text lines are displayed on the bottom line of the display, the cycle will start by displaying the old line on the first row, therefore testo needs
#initialization, my line is 20 char long so it fits in a line, by ggod mesure I issue a CR command on every cycle, so corruption should be mimimal even if you
#initialize testo with someting that doesn't fill a line.

def comando (istruzione):
    ordine=[istruzione]
    binario=bytes(ordine)
    vfd.write(binario)

    #This function encodes and sends the argoment, it is uused to issue command codes, known codes for the M202MD15B are:
    #15 reset                                           15 reset
    #16 ignora primo carattere successivo imput         16 Ignores the forst character of the next input
    #20 cursore spento                                  20 Cursor off
    #19 cursore acceso                                  19 Cursor on    
    #17 no scorrimento                                  17 Disable autoscrolling
    #10 cambio riga                                     10 Line change
    #9  un carattere a destra                           9  Cursor one char right
    #8  un carattere a sinistra                         8  Cursor one char left
    #31 cancella tutto e riporta il cursore in alto     31 Clear screen and reset cursor position (top left)
    #13 torna ad inizio riga                            13 Back to current line start (cursor all left)

vfd=serial.Serial("/dev/ttyS0")
#attiva porta seriale                                   Serial open @9600 baud
comando (31)
#azzeramento                                            CLear screen
comando (17)
#No scorrimento                                         Autoscroll off
comando (20)
#Niente cursore visibile ma il cursore, anche se inisibile, passa comunque da una riga all'altra.
#No visible cursor, the invisible cursor still jumps from one line to the other when you send 20 chars.
while True:
    Televideo_24ore=feedparser.parse('http://www.servizitelevideo.rai.it/televideo/pub/rss102.xml')
    #importa il feed "24 ore non stop" del Televideo    Imports the RSS feed
    n=len(Televideo_24ore.entries)
    #n numero notizie                                   n=number of news
    for i in range(n):
        #i indicizza le notizie                         i indexes the news
        j=0
        #j conta i caratteri di ogni notizia che sono gioà stati visualizzati
        #j coults the number of characters of the current elemnt that have already beedn displayed
        while j<len(Televideo_24ore.entries[i].title):
            comando (13)
            #riporta il cursore a sinistra qualora fosse finito fuori posto
            #Just in case something went wrong, sends sursor back to the left
            vfd.write (testo.encode("cp437","replace"))
            #ristampare il testo precedente sulla prima riga
            #Display the text from the previous cycle on the first line
            testo=Televideo_24ore.entries[i].title[j:j+20]
            j+=20
            #Testo è una riga da inviare al display, minore o uguale a 20 caratteri.
            #Selects a new line <=20 characters
            l=len(testo)
            if l<20:
                for k in range(20-l):
                    #questo ciclo serve a mantenere consisitente la lunghezza delle videate: 20 caratteri
                    #Fills the line with spaces if it has less tha 20 characters (at the end of the entry)
                    testo+=" "
            vfd.write (testo.encode("cp437","replace"))
            #Send second text line
            time.sleep(3)
            #Wait between the lines
