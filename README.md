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
List of required python3 & pip3 dependencies:<br>
- python3<br>
- python3-pip<br>
- python3-pil<br>
- python3-numpy<br>
- RPi.GPIO<br>
- spidev<br>
- time<br>
- traceback<br>
- requests<br>
- image<br>
- imageDraw<br>
- imageFont<br>
<br>
<br>
Install those dependencies:<br>
<code>
sudo apt-get install python3 && <br>sudo apt-get install python3-pip python3-pil python3-numpy && <br>sudo pip3 install RPi.GPIO spidev time traceback requests image imageDraw imageFont
</code>
<br>
<br>
Assuming you have <code>git</code> installed you can  now download Demo code from <a href="https://github.com/waveshare/e-Paper">Waveshare Github</a> website:<br>
<code>
git clone https://github.com/waveshare/e-Paper
</code>
<br><br>
Downloaded files include installation instructions, setup.py file and example python3 files.<br>
Files neccesary to read are:<br>
- epdconfig.py (copyright: <a href="https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT">Waveshare</a>);<br>
- ep2in13.py (copyright: <a href="https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT">Waveshare</a>).<br><br>
<br>
Fonts and Glyphs used:<br>
- <a href="https://github.com/anthonyfok/fonts-wqy-microhei">wqy-microhei</a> fonts;<br>
  Wqy-Microhei fonts are available in the debian/raspbian repository as a <code>fonts-wqy-microhei</code>.<br>
  <code>sudo apt-get install fonts-wqy-microhei<code><br>
- <a href="https://github.com/ryanoasis/nerd-fonts">nerd fonts</a> - a weather icons glyph pack.<br>
  Nerd Fonts are available in <a href="https://github.com/ryanoasis/nerd-fonts">this github repository</a>. You have to follow the installation instructions from the Nerd Fonts README.<br>
<br>
Main configuration file with most settings and changes is a <b><span style="color:blue">main.py</span><b>.<br>
Configuration files are in the: <code>/home/pi</code> directory.<br>
<br>
