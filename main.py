#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os

# 800x480

picdir = '/home/pi/epd-test-py/e-Paper/RaspberryPi&JetsonNano/python/pic/'
libdir = '/home/pi/epd-test-py/e-Paper/RaspberryPi&JetsonNano/python/lib/'
imgfile = './img.bmp'
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in5_V2
import time
from PIL import Image, ImageDraw, ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

logging.info(sys.argv)


try:
    epd = epd7in5_V2.EPD()
    logging.info("init")
    epd.init()

    for action in sys.argv:
        if "clear" == action:
            logging.info("Clearing")
            epd.Clear()
        elif "img" == action:
            logging.info("Drawing Image")
            Himage = Image.open(imgfile)
            epd.display(epd.getbuffer(Himage))
        elif "wait" == action:
            logging.info("Waiting 1s")
            time.sleep(1)

        time.sleep(0.100)


    #logging.info("Clear...")
    #epd.init()
    #epd.Clear()

    logging.info("Goto Sleep...")
    epd.sleep()
    epd.Dev_exit()

    epd7in5.epdconfig.module_exit()
    exit()

except IOError as e:
    logging.warning(e)
