import random
import json
import time
from telethon import TelegramClient, events, errors
from telethon.sessions import StringSession

def load_config(file_path):
    """
    Load JSON data from a file and return the parsed data.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The parsed JSON data as a dictionary.
    """
    with open(file_path) as file:
        return json.load(file)

# Load config and language data
config = load_config('config.json')
lang = load_config('lang.json')

API_ID = config['API_ID']
API_HASH = config['API_HASH']
STRING_SESSION = config['STRING_SESSION']

client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH).start()
client.parse_mode = 'html'

COMMENT_TEXT = config['COMMENT_TEXT']
LANG = config['LANGUAGE']
lang = lang[LANG]

CHANNEL_ID = config['CHANNEL_ID']

@client.on(events.NewMessage)
async def auto_comment(event):
    """
    Automatically post a random comment in response to new messages in the configured channel.

    Args:
        event (telethon.tl.custom.Message): The new message event.
    """
    if event.chat_id not in CHANNEL_ID:
        return
    print(lang['NEW_POST'].format(event.peer_id.channel_id))
    try:
        await client.send_message(event.chat_id, random.choice(COMMENT_TEXT), comment_to=event.id)
        print(lang['COMMENTED'].format(event.peer_id.channel_id))
    except errors.FloodWaitError as flood_wait_duration:
        print(lang['FLOOD_WAIT_ERROR'].format(flood_wait_duration.seconds))
        time.sleep(flood_wait_duration.seconds)
    except Exception as unknown_error:
        print(lang['ERROR_WHILE_POSTING'] + '\n' + str(e))

print(lang['STARTED_MSG'])

client.run_until_disconnected()
