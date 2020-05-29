## Raspberry Pi 3 + 2.13" Waveshare Display
### E-paper Screen displaying Current Time and Local Weather <br><br>

How to display some nice informations - like current time and local weather - on a Raspberry Pi 3 with e-Paper HAT (Waveshare 2.13" B/W Color version) Display.<br>
<br>
Parts:<br>
- Raspberry PI 3 ( Works the same on Pi Zero or Pi Zero W);<br>
- Waveshare 2.13 e-Paper HAT v.2 (monochrome).<br><br>

Install BCM2835 libraries:<br>
- bcm2835 - follow instruction how to install from <a href="https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT">Waveshare</a> website.<br>

Install wiringPi libraries:<br>
- wiringpi - also follow instructions from <a href="https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT">Waveshare</a> website.<br>
<br>
Install Python libraries:<br>
- sudo apt-get install python3-pip<br>
- sudo apt-get install python3-pil<br>
- sudo apt-get install python3-numpy<br>
- sudo pip3 install RPi.GPIO<br>
- sudo pip3 install spidev<br>
- sudo pip3 install time<br>
- sudo pip3 install traceback<br>
- sudo pip3 install requests<br>
- sudo pip3 install image<br>
- sudo pip3 install imageDraw<br>
- sudo pip3 install imageFont<br>
<br>
<br>
Download Demo code from <a href="https://github.com/waveshare/e-Paper">Waveshare Github</a> website:<br>
- git clone https://github.com/waveshare/e-Paper
<br><br>
Downloaded files include installation instructions, setup.py file and example python3 files.<br>
Files neccesary to read are:<br>
- epdconfig.py (copyright: <a href="https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT">Waveshare</a>);<br>
- ep2in13.py (copyright: <a href="https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT">Waveshare</a>).<br><br>
<br>
Fonts and Glyphs used:<br>
- <a href="https://github.com/anthonyfok/fonts-wqy-microhei">wqy-microhei</a> fonts;<br>
- <a href="https://github.com/ryanoasis/nerd-fonts">nerd fonts</a> - a weather icons glyph pack.<br>
<br>
Main configuration file with most settings and changes is a <b>main.py<b>.<br>
<br>
<br>
== Raspberry Pi GPIO Pin map for 2.13" Waveshare e-Paper HAT==
/* Copyright (c) 2017 Waveshare
 * All rights reserved.
 +-----+-----+---------+------+---+---Pi 3---+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 1 | ALT5 | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | ALT5 | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 0 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 0 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI | ALT0 | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO | ALT0 | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK | ALT0 | 0 | 23 || 24 | 1 | OUT  | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | OUT  | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 1 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |  OUT | 1 | 35 || 36 | 1 | OUT  | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |   IN | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+---Pi 3---+---+------+---------+-----+-----+
*/
/*
  == Hardware connection to Raspberry Pi ==
    EPD    =>    Raspberry Pi
  * VCC    ->    3.3
  * GND    ->    GND
  * DIN    ->    MOSI
  * CLK    ->    SCLK
  * CS     ->    24 (Physical, BCM: CE0, 8)
  * D/C    ->    22 (Physical, BCM: 25)
  * RES    ->    11 (Physical, BCM: 17)
  * BUSY   ->    18 (Physical, BCM: 24)
*/