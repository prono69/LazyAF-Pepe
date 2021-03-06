#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.
 
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
 
print("""Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details
 
if Telegram is blocked by your ISP, you can try the @useTGxBot""")
APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("Enter API HASH here: ")
 
with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    session_string = client.session.save()
    saved_messages_template = """@PepeB0t 
<code>HU_STRING_SESSION</code>: <code>{}</code>
 
⚠️ <i>it is forbidden to pass this value to third parties</i>""".format(session_string)
    client.send_message("me", saved_messages_template, parse_mode="html")
    
print("""Please Check Your Telegarm Saved Message for String Session.
Thank You for Using PepeBot Service.""")