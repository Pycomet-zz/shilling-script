#Telegram Group Shilling Bot

import os
import sys
from telethon import TelegramClient
from telethon.sessions import StringSession
import time
import datetime
from dotenv import load_dotenv
load_dotenv()
starttime = time.time()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

SESSION = os.getenv("SESSION1")

INTERVAL = os.getenv("INTERVAL1")

# INPUT TARGET GROUPS HERE
groups = os.getenv("GROUPS1").split("-")

message = os.getenv("MESSAGE1")

failcount = 0

with TelegramClient(StringSession(SESSION), API_ID, API_HASH) as client:
    while True:
        for x in groups:
            try:
                client.loop.run_until_complete(
                    client.send_message(x, message)
                )
            except:
                print(x, sys.exc_info()[0])
                failcount += 1
        print(datetime.datetime.now(), str(failcount/len(groups) * 100) + '%')
        time.sleep(INTERVAL)