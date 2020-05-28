# RaspberryPiWeatherDisplay
Clock and Weather configuration build for Raspberry Pi + e-Paper HAT (Waveshare 2.13") Display.  <br>
<br>
Parts:<br>
- Raspberry PI 3;<br>
- Waveshare 2.13 e-Paper HAT v.2 (monochrome)<br><br>

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

Main configuration file with most settings and changes is a <b>main.py<b>.
