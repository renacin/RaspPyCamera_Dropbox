# Name:                                             Renacin Matadeen
# Student Number:                                         N/A
# Date:                                               01/11/2018
# Course:                                                 N/A
# Title                                      Raspbery Pi Dropbox Camera System
#
#
#
#
#
# ----------------------------------------------------------------------------------------------------------------------

import time
import datetime
import picamera
import dropbox

from dropbox.files import WriteMode
from PIL import Image, ImageDraw, ImageFont, ImageStat

# ----------------------------------------------------------------------------------------------------------------------


def get_brightness(x):

    # Get Brightness Of Image
    im = Image.open(x).convert("L")
    stat = ImageStat.Stat(im)
    stat = stat.mean[0]
    return stat


def upload_image(ax, x, xdb):

    dbx = dropbox.Dropbox(ax)

    with open(x, "rb") as f:
        dbx.files_upload(f.read(), xdb, mute=True, mode=dropbox.files.WriteMode.overwrite)

def add_date_stamp(imx):
    image = Image.open(imx)
    font_type = ImageFont.truetype("Roboto-Thin.ttf", 25)

    draw = ImageDraw.Draw(image)

    draw.text(xy=(20, 25), text=date, fill=(255, 255, 0), font=font_type)
    draw.text(xy=(20, 50), text=time_24, fill=(255, 255, 0), font=font_type)

    image.save(imx, "JPEG")
    
    
    
    
    
