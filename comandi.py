import serial
vfd=serial.Serial("/dev/ttyS0")
comando=[31]
binario=bytes(comando)
vfd.write(binario)
print (binario)
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