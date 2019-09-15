from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from userbot import 978227
, 
cb6d622ea5d1734f3502ee06cd591cc4


print("""Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details""")

with TelegramClient(StringSession(), 978227, 
cb6d622ea5d1734f3502ee06cd591cc4
) as client:
    print(client.session.save())
