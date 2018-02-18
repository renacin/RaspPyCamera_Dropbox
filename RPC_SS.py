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

from Functions import get_brightness, upload_image, add_date_stamp
# ----------------------------------------------------------------------------------------------------------------------

# Basic APP Credentials
APP_KEY = "APP_KEY"
APP_SECRET = "APP_SECRET"
ACCESS_TOKEN = "ACCESS_TOKEN"

# ----------------------------------------------------------------------------------------------------------------------

# Instantiate Basic Pi Camera Objects
camera = picamera.PiCamera()
image_name = "RPC_SS.jpg"


# Basic File Paths
directory = "/home/pi/RPC_Images/"
db_direc = "/RaspberryPi_Camera/"

x = directory + image_name
xdb = db_direc + image_name
ax = ACCESS_TOKEN


# Camera Settings
camera.vflip = False
camera.resolution = (2592, 1944)
camera.brightness = 50
camera.saturation = 0
camera.framerate = 1


camera.capture(directory + image_name)
time.sleep(2)

# Create A While Loop To Continuously Run Program
while True:
    try:    
        # Get Current Time
        complete_time = str(datetime.datetime.now())
        split_observation = complete_time.split(" ")
        date = "Date: " + split_observation[0]
        time_s = split_observation[1].split(".")
        time_b = time_s[0]
        time_24 = "Time: " + time_b

        # Base Shutter Speed
        camera.shutter_speed = 900  # 150 - 9000000

        # Capture Test Image
        camera.capture(directory + image_name)
        time.sleep(2)

        # Capture Actual Image
        camera.capture(directory + image_name)

        # Get Brightness Of Image
        stat = get_brightness(x)

        upload_image(ax, x, xdb)

        # If Image Is At Night
        if (int(stat) < 50):

            camera.shutter_speed = 9000000  # 150 - 9000000

            # Capture Test Image
            camera.capture(directory + image_name)
            time.sleep(2)

            # Capture Actual Image
            camera.capture(directory + image_name)

            # Add Date & Time Stamp To Image
            add_date_stamp(x)

            # Upload Image
            upload_image(ax, x, xdb)

        # If Image Is During The Day
        else:

            # Capture Actual Image
            camera.capture(directory + image_name)

            # Add Date & Time Stamp To Image
            add_date_stamp(x)

            # Upload Image
            upload_image(ax, x, xdb)

        time.sleep(180)

    except:
        pass


