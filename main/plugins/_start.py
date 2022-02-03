#Github.com/Vasusen-code

import os
from .. import bot as Drone
from telethon import events, Button

from ethon.mystarts import start_srb

st = "**Hii,\nI am @Pyrogrammers Save restricted Contents bot.**\nSend me any public or private restricted Channel post link.\nI will give you that post.\n**Hit /help to know more.**"


 @Drone.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply(f'{st}', 
                      buttons=[
                        [Button.url("Updates Channel", url="https://t.me/pyrogrammers"),
                         Button.url("Support Group", url="https://t.me/+7ScFy39Vckk5MWQ1")],
                        [Button.url("YouTube Channel", url="https://youtube.com/channel/UC2anvk7MNeNzJ6B4c0SZepw")],
                    ])
    try:
        await Bot.start()
        await idle()
    except Exception as e:
        if 'Client is already connected' in str(e):
            pass
        else:
            return

    # start help Message
@Drone.on(events.NewMessage(pattern="^/help$"))
async def search(event):
    await event.reply('<b><u>For Public Restricted Channel contents.</b></u>\nTo get public restricted Channel contents, just send your Post link i will give you that post without Downloading.\n\n<b><u>For Private Restricted Channel contents.</b></u>\nTo get private restricted Channel contents, First send me Channel invite link so that i can join your channel after that send me post link of your restricted Channel to get that post.', parse_mode="HTML")
    #end help Message
