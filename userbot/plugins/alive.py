# modify by @sameer_795
# Kang with credits else gay.
""" 
Original Plugin By Darkcobra and Godhackerzuserbot
Gv Credits Else Gey 
"""
import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events
from userbot.utils import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND SAR"
file = Config.ALIVE_PHOTTO
global ghanti
ghanti = borg.uid

""" =======================CONSTANTS====================== """
""" =======================CONSTANTS====================== """
pm_caption = "__                   **🔥 𝐃𝟑𝐕𝐈𝐋_𝐁𝐎𝐓 🔥**  __\n\n"

pm_caption += f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**      『[{DEFAULTUSER}](tg://user?id={ghanti})』**\n\n"
pm_caption += "✘ ΔβØỮŦ Μ¥ Ş¥ŞŦ€Μ ✘\n\n"
pm_caption += "➾ **𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍**  ➣ 𝟏.𝟏𝟕.𝟓\n"
pm_caption += "➾ **𝐒𝐔𝐏𝐏𝐎𝐑𝐓 ** ➣ [𝐉𝐎𝐈𝐍](https://t.me/joinchat/SFcYi6LR-Sazusqf)\n"
pm_caption += "➾ **𝐒𝐎𝐂𝐈𝐀𝐋  **  ➣ [𝐉𝐎𝐈𝐍](https://t.me/joinchat/VhpqUT83rKwiDnghqupK8w)\n"
pm_caption += "➾ **𝐂𝐇𝐀𝐍𝐍𝐄𝐋  **  ➣ [𝐉𝐎𝐈𝐍](https://t.me/joinchat/WCEEeeCSq4mE5KWm)\n"
pm_caption += "➾ **𝐂𝐑𝐄𝐀𝐓𝐎𝐑** ➣ [⚡𝐒𝐀𝐌𝐄𝐄𝐑⚡](@D3VIL_SAMEER)\n" 

pm_caption += " \n\n"
pm_caption += "[✨ 𝔻𝔼ℙ𝕃𝕆𝕐 𝕐𝕆𝕌ℝ 𝔻3𝕍𝕀𝕃_𝔹𝕆𝕋 ✨](https://github.com/sameerpanthi/D3VIL_BOT)"


@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))

async def amireallyalive(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
##
    on = await borg.send_file(yes.chat_id, file ,caption=pm_caption)
