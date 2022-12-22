from telethon import *
from telethon.sessions import StringSession
import random
import json
import time

file_1 = open('config.json').read()
config = json.loads(file_1)
file_2 = open('lang.json', encoding='utf-8').read()
lang = json.loads(file_2)

API_ID = config['API_ID']
API_HASH = config['API_HASH']
STRING_SESSION = config['STRING_SESSION']

client = TelegramClient(StringSession(STRING_SESSION),
                        API_ID, API_HASH).start()

client.parse_mode = 'html'

COMMENT_TEXT = config['COMMENT_TEXT']

_lang = config['LANGUAGE']
lang = lang[_lang]


def CONFIG_FUNC():
    file = open('config.json')
    read = file.read()
    j = json.loads(read)
    file.close()
    return j


global CHANNEL_ID
CHANNEL_ID = CONFIG_FUNC()['CHANNEL_ID']


@client.on(events.NewMessage)
async def auto_comment(event):
    if event.chat_id not in CHANNEL_ID:
        return
    print(lang['NEW_POST'].format(event.peer_id.channel_id))
    try:
        await client.send_message(event.chat_id, random.choice(COMMENT_TEXT), comment_to=event.id)
        print(lang['COMMENTED'].format(event.peer_id.channel_id))
    except errors.FloodWaitError as e:
        print(lang['FLOOD_WAIT_ERROR'].format(e.seconds))
        time.sleep(e.seconds)
    except Exception as e:
        print(lang['ERROR_WHILE_POSTING'] + '\n' + e)

print(lang['STARTED_MSG'])

client.run_until_disconnected()
