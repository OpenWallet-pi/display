#!/bin/python2
##
 #  Copyright (C) 2017 OpenWallet-pi
 #            (C) 2017 Joe Maples <joe@frap129.org>
 #
 # Permission is hereby granted, free of charge, to any person obtaining a copy
 # of this software and associated documnetation files (the "Software"), to deal
 # in the Software without restriction, including without limitation the rights
 # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 # copies of the Software, and to permit persons to  whom the Software is
 # furished to do so, subject to the following conditions:
 #
 # The above copyright notice and this permission notice shall be included in
 # all copies or substantial portions of the Software.
 #
 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 # THE SOFTWARE.
 ##

import datetime
import epd2in13b
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from six import unichr
from subprocess import PIPE
from subprocess import Popen
import sys

COLORED = 1
UNCOLORED = 0

def main():
    # initialize display driver
    epd = epd2in13b.EPD()
    epd.init()

    # clear the frame buffer
    frame_black = [0xFF] * (epd.width * epd.height / 8)
    frame_red = [0xFF] * (epd.width * epd.height / 8)

    # initialize buffer with qrcode
    frame_black = epd.get_frame_buffer(Image.open(sys.argv[1]))

    # define font locations
    font = ImageFont.truetype('/usr/share/fonts/TTF/Roboto-Regular.ttf', 16)
    fa = ImageFont.truetype('/usr/share/fonts/TTF/fontawesome-brands.ttf', 22)
    
    # get date time
    date = datetime.datetime.now().strftime("%b %d, %Y")

    # draw OpenWallet PI banner
    epd.draw_filled_rectangle(frame_red, 0, 0, 128, 24, COLORED);
    epd.draw_string_at(frame_red, 2, 0, "OpenWallet PI", font, UNCOLORED)

    # write strings to the buffer
    epd.draw_string_at(frame_black, 6, 30, "Balance:", font, COLORED)
    epd.draw_string_at(frame_black, 4, 50, unichr(int('f42e', 16)), fa, COLORED)
    epd.draw_string_at(frame_black, 20, 50, sys.argv[2], font, COLORED)
    epd.draw_string_at(frame_black, 6, 70, "Checked on:", font, COLORED)
    epd.draw_string_at(frame_black, 6, 90, date, font, COLORED)

    # display the frames
    epd.display_frame(frame_black, frame_red)

if __name__ == '__main__':
    main()
