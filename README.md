# Nana-TgBot

[![Build Status](https://semaphoreci.com/api/v1/ayrahikari/nana-tgbot/branches/master/badge.svg)](https://semaphoreci.com/ayrahikari/nana-tgbot)

### Userbot + Assistant for Telegram

```
#include <std/disclaimer.h>
/**
	I am no responsible about your account.
	I made this for fun only, if you get banned, reported, or even Banned by Telegram itself,
	Then blame yourself.

	This is not copy-pasta project!
	I am make this from scratch with Pyrogram!
	See Credits bellow before you say i am kanger!

	If you blame me if something wrong with your account after use this bot,
	See me in my group chat, i'll laught at you!

	DO WITH YOU OWN RISK!
*/
```

Currently work fine perfectly, but some features may give you error. Please report a bug to me if you facing any issues.
> Go to our group support if you want to ask something [@AyraSupport](https://t.me/AyraSupport)

```
Q: Why need Assistant (Real bot)?
A: Because real bot will help you a lot for many things, and make user easy to use it.
```

### Installation Guide

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/alanndz/Nana-TgBot)

This is long boring confused stuff if you new in this, please read carefully.
If you need something, just come to [@AyraSupport](https://t.me/AyraSupport) to get help.

## Create a Real Bot

1. Go to @BotFather, then type `/newbot`
2. Insert your bot **Name**, for example **My Assistant**
3. Then insert your bot **username** It must end in `bot`. for example **MyAssistantBot**.
4. Copy Token for later

## Configuration

1. Register your account API [here](https://my.telegram.org/apps)
2. Copy api_id and api_hash for config later.
3. Go to [@EmiliaHikariBot](https://t.me/EmiliaHikariBot) or [@MissRose_bot](https://t.me/MissRose_bot), and type `/id`. Copy your ID account.
4. Rename config.example.py to **confing.py** in nana folder
5. And change config like this:

```
api_id = 12345 # From guide no 2
api_hash = "123456789abcdefghijklmnopqrstuvw" # From guide no 2

ASSISTANT_BOT_TOKEN = "TOKEN" # Replace TOKEN from guide above (@BotFather)

Owner = 388576209 # From guide no 3
AdminSettings = [388576209] # From guide no 3
```

Then you ready to go next guide

## Install Requirements

Install all requirements by python, in your terminal type this:
```
pip install -r requirements.txt
```

If you're using pipenv, use this instead:
```
pipenv install -r requirements.txt
```

## Install Database

This is required for some features, if you want to use database, follow this guide.

- Install postgresql
```
sudo apt-get update && sudo apt-get install postgresql
```

- Change user to postgres
```
sudo su - postgres
```

- Create a user, change **YOUR_USER** with you own user
```
createuser -P -s -e YOUR_USER
```

- Create a database, dont forget to change **YOUR_USER** and **YOUR_DB_NAME**
```
createdb -O YOUR_USER YOUR_DB_NAME
```

- Test your database (optional)
```
psql YOUR_DB_NAME -h YOUR_HOST YOUR_USER
```

- After create a database, your database URL should be like this
```
sqldbtype://YOUR_USER:password@localhost:5432/YOUR_DB_NAME
```

## Run NanaBot and Assistant

To run this bot, just type
```
python -m nana
```

Or if you're using pipenv, do this instead
```
pipenv run python -m nana
```

# Getting update

Assistant will check update every bot is running, make sure you're on official branch.

To check update manual, just type `update` with Command (default is .) in your nana bot.

To get update, type `update now` in your nana bot.

Or you can update via Assistant (If they notify you), just click Update Now and wait for update.

# Credits

- [Nana-TgBot Source Base](https://github.com/Hyakei/Nana-TgBot)
- [Telegram Userbot](https://github.com/RaphielGang/Telegram-UserBot)
- [Paperlane Extended](https://github.com/AvinashReddy3108/PaperplaneExtended)
