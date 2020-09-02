## Raspberry Pi 3 + 2.13" Waveshare Display
### E-paper Screen displaying Current Time and Local Weather <br><br>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub issues](https://img.shields.io/github/issues/rkruk/RaspberryPiWeatherDisplay)](https://github.com/rkruk/RaspberryPiWeatherDisplay/issues?q=is%3Aopen)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/rkruk/RaspberryPiWeatherDisplay/)

<br><br>
<p align="center"><b>CURRENT STATUS: BEWARE! THE CODE DOES NOT WORK YET.</b></p><br>
<p align="center"><b>It can eat your hamster!</b></p> 
<br><br>

Little Raspberry PI weather display - made with python.<br> 
The information it shows on a display: current time and forecast for the local weather.<br>
Hardware is based on a Raspberry Pi 3 and an e-Paper HAT (Waveshare 2.13" B/W Color version) Display.<br>
<br>
Parts:<br>
- Raspberry Pi 3 ( Works the same on Pi 4, Pi Zero or Pi Zero W);<br>
- Waveshare 2.13 e-Paper HAT v.2 (monochrome).<br><br>

Some assumptions at the beginning:<br>
- Raspberry Pi is running <a href="https://www.raspberrypi.org/downloads/raspberry-pi-os/">Raspberry Pi OS</a>.<br>
- Everything is updated to the latest packages.<br>
- Libraries used are from standart Raspberry Pi OS repositories. Nothing has been added as a source or blob (nothing but firmware but that is a different story and is not in the scope here).<br>
- Python 3 packages are installed, managed, etc via the pip3 python package installer. Pip3 is installed as you may have guessed from standard Raspberry Pi OS repository (python3-pip package).<br>
Install BCM2835 libraries:<br>
- bcm2835 - follow instruction how to install from <a href="https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT">Waveshare</a> website.<br>

Install wiringPi libraries:<br>
- wiringpi - also follow instructions from <a href="https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT">Waveshare</a> website.<br>
<br>
List of required python3 & pip3 dependencies:<br>
<ul>
  <li>python; </li>
  <li>python3-pip - it is the package installer for Python; </li>
  <li>python3-pil - Python Imaging Library is an additional library for the Python, that adds support for opening, manipulating, and saving image file formats; </li>
  <li>python3-numpy - Numerical Python) is a library consisting of multidimensional array objects and a collection of routines for processing of array; </li>
  <li>RPi.GPIO - provides a class to control the GPIO on a Raspberry Pi; </li>
  <li>spidev - contains a python module for interfacing with SPI devices from user space via the spidev linux kernel driver; </li>
  <li>time - module provides various time-related functions; </li>
  <li>traceback - module provides a standard interface to extract, format and print stack traces of Python programs; </li>
  <li>requests - simple HTTP library for Python; </li>
  <li>image - provides cropping, resizing, thumbnailing, overlays, tint and mask for images; </li>
  <li>imageDraw - provides simple 2D graphics for Image objects; </li>
  <li>imageFont - defines a class with the same name. Instances of this class store bitmap fonts, and are used with the PIL.ImageDraw.Draw.text() method; </li>
</ul>
<br>
<br>

Install python and necessary dependencies:<br>
<code>
sudo apt-get install python3 && <br>sudo apt-get install python3-pip python3-pil python3-numpy
</code>
<br><br>

You have to install also all python dependencies:<br>
<code>
sudo pip3 install RPi.GPIO spidev time traceback requests image imageDraw imageFont
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
- <a href="https://github.com/anthonyfok/fonts-wqy-microhei">wqy-microhei</a> fonts. - Wqy-Microhei fonts are available in the Debian/Raspbian repository as a <code>fonts-wqy-microhei</code> package. Install the wqy-microhei fonts via: <code>sudo apt-get install fonts-wqy-microhei</code> command.<br>
- <a href="https://github.com/ryanoasis/nerd-fonts">nerd fonts</a> - a weather icons glyph pack.<br>
  Nerd Fonts are available in <a href="https://github.com/ryanoasis/nerd-fonts">this github repository</a>. You have to follow the installation instructions from the Nerd Fonts README.<br>
<br>
Main configuration with most settings and changes is a <b>main.py</b> file.<br><br>
The configuration files have some example directories used like the: <b><code>/home/pi</code></b> directory.<br>
Change those at your own discretion.<br>
<br>
