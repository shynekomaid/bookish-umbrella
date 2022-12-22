# Bookish umbrella - fast-comment telegram bot

> WARNING: The software is provided by "AS IS" (read license).
>
> If the use of the software causes your computer to break down, you catch ban on Telegram, falls off your dick or opens a portal with hellish creatures, the developer is not responsible for it.
>
> This project is just a proof-of-concept. Do not use for evil.

A telegram userbot to automatically comment in channel on new posts.

Short install guide:

0. I recomend create new telegram account. Create it without 2FA.
1. Install python 3.10.1
2. Install pip
3. Install requirements:
```pip3 install -r requirements.txt```
4. Get id of needed channels (reply channel post to @JsonDumpBot and read $.message.chat.id)
5. Insert id to `CHANNEL_ID` in `config.json` (without quotes). Examples: `[-1234567789]`, `[-123456789, -987654321]`
6. Change `COMMENT_TEXT` in `config.json`. Examples: `["Первый", "🤡", "Ахахахах"]`
7. Get `API_ID` and `API HASH` [read there](https://core.telegram.org/api/obtaining_api_id) and set in `config.json`
8. Launch:
```python3 main.py```
9. Login using phone number and code from sms
10. ???????
11. PROFIT
