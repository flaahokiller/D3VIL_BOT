# MADE BY LEGENDX22
# IDEA BY PROBOY22
# CREDITS TEAMLEGEND
# PLEASE KEEP CREDITS 🥺



from telethon import events, Button, custom
import os,re
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
@tgbot.on(events.InlineQuery(pattern=r"repo"))
async def inline_id_handler(event: events.InlineQuery.Event):
 LEGEND = event.builder
 X= [[custom.Button.inline("🔥 CLICK ME 🔥",data="obhai")]]
 query = event.text
 result = LEGEND.article("LEGEND",text="REPO AND SUPPORT",buttons=X,link_preview=False)
 await event.answer([result])
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"obhai")))
async def callback_query_handler(event):

# inline by LEGENDX22 and PROBOY22 🔥
  await event.edit(text="D3VIL REPO AND GROUP LINK",buttons=[[Button.url(f"🔥D3VIL REPO🔥", url="https://github.com/https://github.com/sameerpanthi/D3VIL_BOT"), Button.url(f"⚡D3VIL OWNER⚡", url="https://t.me/SAMEER_795")]])
