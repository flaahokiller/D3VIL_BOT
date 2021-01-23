 
from asyncio import sleep
 
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
 
from telethon.tl.functions.channels import EditBannedRequest
 
from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply
 
from userbot import bot
 
 
 
@bot.on(admin_cmd(pattern=r"banall", outgoing=True))
 
@bot.on(sudo_cmd(pattern=r"banall", allow_sudo=True))
 
async def _(savagebot):
 
    chat = await hellbot.get_chat()
 
    getme = await hellbot.client.get_me()
 
    admin = chat.admin_rights
 
    creator = chat.creator
 
    if not admin and not creator:
 
        await edit_or_reply(savagebot, "Not enough permission to do a magikð¤")
 
        return
 
    await edit_or_reply(savagebot, "Lets get started with my magik ð")
 
    gotta = await savagebot.client.get_participants(savagebot.chat_id)
 
    for user in gotta:
 
        if user.id == getme.id:
 
            pass
 
        try:
 
            await savagebot.client(EditBannedRequest(savagebot.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
 
        except Exception as e:
 
            await savagebot.edit(str(e))
 
        await sleep(.5)
 
    await edit_or_reply(savagebot, "Magik doneâ¡")
