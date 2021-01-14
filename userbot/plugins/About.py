#modify by @sameer_795
#Kang with credits else gay.
""" 
Original Plugin By D3VIL BOT
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
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "d3vil user"
global ghanti
ghanti = borg.uid

""" =======================CONSTANTS====================== """
file = "https://telegra.ph/file/8c063f847749e361620f3.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "**🔥🔥 𝐃𝟑𝐕𝐈𝐋_𝐁𝐎𝐓 𝐁𝐘 𝐃𝐄𝐕𝐈𝐋 𝐅𝐑𝐀𝐍𝐂𝐇𝐄𝐒𝐊𝐎𝐎🔥🔥**  \n\n"

pm_caption += f"               ↼🅄🅁 🄳🄰🄳⇀\n      『𝘿3𝙑𝙄𝙇 𝙁𝙍𝘼𝙉𝘾𝙃𝙀𝙎𝙆𝙊𝙊』\n\n"
pm_caption += "✘ A͜͡B͜͡O͜͡U͜͡T͜͡ D͜͡3V͜͡I͜͡L͜͡ O͜͡W͜͡N͜͡E͜͡R͜͡  ✘\n\n"
pm_caption += "➾ 𝐍𝐀𝐌𝐄 ➣ [𝐃3𝐕𝐈𝐋 𝐅𝐑𝐀𝐍.😎](@D3VIL_FRANCHESKOO)\n"
pm_caption += "➾ 𝐇𝐎𝐁𝐁𝐈𝐄 ➣ 𝐆. 𝐌𝐀𝐑𝐍A☠️\n"
pm_caption += "➾ 𝐎𝐖𝐍𝐄𝐑  ➣ [𝐃3𝐕𝐈𝐋 𝐓𝐄𝐀𝐌😈](https://t.me/joinchat/Vy3AoRuVMGxxDCcr)\n"
pm_caption += "➾ 𝐂𝐎-𝐎𝐖𝐍𝐄𝐑  ➣ [𝐌𝐁𝐋 𝐓𝐄𝐀𝐌😍](https://t.me/joinchat/TFLvsrk91e9Me9nV)\n"
pm_caption += "➾ 𝐌𝐘 𝐔𝐒𝐄𝐑𝐁𝐎𝐓 ➣ [𝐃3𝐕𝐈𝐋 𝐁𝐎𝐓⚡](https://t.me/joinchat/SFcYi7S5MFEz2M17)\n" 
pm_caption += " \n\n"
pm_caption += "𝐒𝐏𝐄𝐂𝐈𝐀𝐋 𝐁𝐔𝐓𝐓𝐎𝐍 𝐅𝐎𝐑 𝐌𝐘 𝐇𝐀𝐓𝐄𝐑𝐒  ➣ [𝐂𝐋𝐈𝐂𝐊 𝐇𝐄𝐑𝐄](https://t.me/joinchat/Q28jGPJHf9qb7gAP)\n"
pm_caption += " \n\n"
pm_caption += "[✨𝐀𝐁𝐎𝐔𝐓 𝐃3𝐕𝐈𝐋 𝐎𝐖𝐍𝐄𝐑✨](https://t.me/ABOUT_D3VIL_FRANCHESKOO)"


@borg.on(admin_cmd(pattern=r"alive2"))
@borg.on(sudo_cmd(pattern=r"alive2", allow_sudo=True))

async def amireallyalive(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
##
    on = await borg.send_file(yes.chat_id, file ,caption=pm_caption)
