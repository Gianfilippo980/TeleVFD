# TeleVFD
Use of a Futaba M202MD15B as an RSS news monitor with a Raspberry Pi 4.
Televideo is the name of theletext service of the Italian national television, in this project I just wanted to display their headlines on a cool VFD display. Luckly they do provide an RSS service.
The display that I found was used in a series of cash registers and allows two lines of 20 characters to be displayed. I could find very little documentation about thid model except for the fundamental connector pinout and the fact that it accepts RS-232 connections at 9600 baud with codepage 437 encoding.
With a bit of experimentation I figured out some of the command codes that, sent throu the serial connection, change the display behavour.
This new knowledge lead to the 2nd revision of my RSS visualizer.
Some of the comments are still awaiting for a translation, but I translated the ones in RSS_2.py, the most important file.

Contents:
- RSS.py      My first RSS visualizer, it only sends text to the display so it may be easier to adapt for different models, but it leaves the cursor on and it doesn't use the last character of the second line to prevent the display to scroll the lines prematurely.
- RSS_2.py    Much improved version: it uses command codes to disable the cursor and the autoscrolling, so it can use the entire display.
- comandi.py  A simple utility for sending command codes to the display (used for test purpose only).
- launcher.sh A little script to automate the execution of the program (a delay is used to aloow for the internet connection time upon reboot), it may be used with cron.
- test.py     A simple utiity to sned text to the disply for test purposes.
- structure   A simple leg to hold the M202MD15B, I 3D-printed a pair.
