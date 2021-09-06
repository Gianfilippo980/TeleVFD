# TeleVFD
Use of a Futaba M202MD15B as an RSS news monitor with a Raspberry Pi 4.
Televideo is the name of theletext service of the Italian national television, in this project I just wanted to display their headlines on a cool VFD display. Luckly they do provide an RSS service.
The display that I found was used in a series of cash registers and allows two lines of 20 characters to be displayed. I could find very little documentation about thid model except for the fundamental connector pinout and the fact that it accepts RS-232 connections at 9600 baud with codepage 437 encoding.
With a bit of experimentation I figured out some of the command codes that, sent throu the serial connection, change the display behavour.
This new knowledge lead to the 2nd revision of my RSS visualizer.
I'll proceed to transalte the comments in the programs for easier understanding (at the moment alll my comments are in Italian)
