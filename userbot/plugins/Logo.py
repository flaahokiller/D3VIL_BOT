 
import os
 
from shutil import rmtree
 
import random
 
import numpy as np
 
from datetime import datetime
 
from PIL import Image, ImageDraw, ImageFont, ImageColor
 
import pytz 
 
import asyncio
 
import requests
 
from PIL import Image, ImageDraw, ImageFont
 
from telegraph import upload_file
 
from userbot import CMD_HELP
 
import os
 
from glitch_this import ImageGlitcher
 
from telethon.tl.types import MessageMediaPhoto
 
from pygifsicle import optimize
 
from userbot import CMD_HELP
 
import asyncio
 
import math
 
import os
 
import time
 
import time
 
from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply
 
import html
 
from telethon.tl.functions.photos import GetUserPhotosRequest
 
from telethon.tl.functions.users import GetFullUserRequest
 
from telethon.tl.types import MessageEntityMentionName
 
import os
 
import base64
 
import sys
 
from telethon.utils import get_input_location
 
import os
 
import textwrap
 
from PIL import Image, ImageDraw, ImageFont
 
 
sedpath = "./LEGENDX/"
 
if not os.path.isdir(sedpath):
 
    os.makedirs(sedpath)
 
    
 
glitcher = ImageGlitcher()
 
DURATION = 200
 
LOOP = 0
 
 
 
 
@borg.on(admin_cmd(pattern="(logo) ?(.*)"))
 
async def slogo(event):
 
    if event.fwd_from:
 
        return
 
    await event.edit("Processing..")
 
    text = event.pattern_match.group(2)
 
    img = Image.open('./20201125_094030 (1).jpg')
 
    draw = ImageDraw.Draw(img)
 
    image_widthz, image_heightz = img.size
 
    pointsize = 500
 
    fillcolor = "white"
 
    shadowcolor = "black"
 
    font = ImageFont.truetype("./Vermin Vibes V.otf", 300)
 
    w, h = draw.textsize(text, font=font)
 
    h += int(h*0.21)
 
    image_width, image_height = img.size
 
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
 
    x = (image_widthz-w)/2
 
    y= (image_heightz-h)/2
 
    draw.text((x, y), text, font=font, fill="white", stroke_width=30, stroke_fill="black")
 
    fname2 = "LOGO BY @sameer_795 .png"
 
    img.save(fname2, "png")
 
    await borg.send_file(event.chat_id, fname2, caption=" LOGO MADE BY D3VIL SAMEER @sameer_795")
 
    if os.path.exists(fname2):
 
            os.remove(fname2)
