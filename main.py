#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd2in13
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import requests

try:
    # Initialize the EPD class:
    epd = epd2in13.EPD()
    epd.init(epd.FULL_UPDATE)
    # Start with a clear (white) background:
    epd.Clear(0xFF)
    
    # Initiate drawing on the image
    image = Image.new('1', (epd2in13.EPD_HEIGHT, epd2in13.EPD_WIDTH), 255)  # 255: clear the frame

    # How to optimise that thing to not ping for weather twice at the same time.
    # Weather location: niepolomice1 + niepolomice2 = 'niepolomice' something something ... format=?
    # THIS PART REQUIRE REVIEW AND REDO. See wttr github documentation --> https://github.com/chubin/wttr.in .
    # The idea is to do one get request at a time for all informations needed and then to splice them into parts.
    # I'm not a programmer and I know nothing about those things at all - just throwing some randoms hoping for a better results..
    niepolomice = requests.get('https://wttr.in/Niepołomice?format=%l:+%c+%t+%w&period=60') # +%S (sunrise)
    niepolomice2 = requests.get('https://wttr.in/Niepołomice?format=%h+%w+%o&period=60') # +%d (dusk)

    # From Demo - leave those for the future reference sake:
    # epd.Clear(0xFF)
    # epd.display(epd.getbuffer(image))
    # time.sleep(2)
    
    # Partial update
    print("Show time")
    epd.init(epd.PART_UPDATE)
    # Full update - image refresh is flickering visibly every 1sec. 
    # Change to FULL_UPDATE, when you'll figure it out how to change the time interval of that weird refresh.
    #epd.init(epd.FULL_UPDATE) # for reference
    
    # Clear (white) background (TEST THIS BIT - as it seems there may be no need to do that twice (line:15 and 38)!):
    epd.Clear(0xFF)
    
    # Lets define some fonts:
    font26 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 26)
    font32 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 32)
    # Change font15 -> wqy-microhei to NotoColorEmoji font (weather glyphs from https://github.com/ryanoasis/nerd-fonts).
    font15 = ImageFont.truetype('/home/pi/.local/share/fonts/NotoColorEmoji.ttf', 15)
    #font15 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 15)
    
    # Create an empty image for objects/layers:
    time_image = Image.new('1', (epd2in13.EPD_HEIGHT, epd2in13.EPD_WIDTH), 255)
    # Render the time section:
    time_draw = ImageDraw.Draw(time_image)
    while (True):
        time_draw.rectangle((10, 10, 120, 50), fill = 255)
        
        # show day and day date (left side):
        time_draw.text((10, 10), time.strftime(' %a %d'), font = font26, fill = 0)
        
        ### Leave that bit from example code for next code update in the future (for a nice GUI optimisations):
        # draw.line([(100,10),(100,50)], fill = 0,width = 1)
        ###

        # show month and year (right side):
        time_draw.text((110, 10), time.strftime('%b %Y'), font = font26, fill = 0)
        
        # show time (left side, bigger and bolder font):
        time_draw.text((10,60), time.strftime('%H:%M'), font = font32, fill = 0)
        
        #show wttr.in weather (right side):
        time_draw.text((110, 60), niepolomice.text, font = font15, fill = 0)
        time_draw.text((110, 80), niepolomice2.text, font = font15, fill = 0)

        newimage = time_image.crop([10, 10, 120, 50])
        time_image.paste(newimage, (10,10))  
        epd.displayPartial(epd.getbuffer(time_image))
    epd.sleep()

        
except:
    print('traceback.format_exc():\n%s',traceback.format_exc())
    exit()
