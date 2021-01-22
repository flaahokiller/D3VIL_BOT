from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("impress"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "impress":
    await event.edit("impress")
    animation_chars = [
            "Suno na👀",
            "❤️ I LOVE U ❤️",
            "🥺 PLZZ MERI GF BN JAO 🥺",
            "🙏 HAMESHA KHUSH RAKHUGA 🙏",
            "🔥 APNE SE JYADA TUMSE LOVE KRTA HU 😘",
            "💝 APAN SATH RAHEGE POORI LIFE 💝",
            "💘 MERI JAAN HE TU 💓",
            "😊 POORI LIFE SAATH RAHUGA 🥺❤️",
            "😘 MERI LIFE HE TU 😘",
            "😍 TERE SARE NAKHRE SEH LUGA 😍",
            "🙂 HAR BAAT MANUGA ☺️",
            "💥ME LOVE U MORE THEN MYSELF💥",
        ]

    for i in animation_ttl:
         
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])

