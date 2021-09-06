import serial
vfd=serial.Serial("/dev/ttyS0")
testo="abcdefghijklmnopqrstuwxyz"
binario=bytes(testo, 'cp437')
vfd.write(binario)