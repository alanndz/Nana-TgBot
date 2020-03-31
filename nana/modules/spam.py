# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# Port to Nana-TgBot by alanndz
#

import asyncio
from asyncio import wait, sleep

from nana import app, Command, logging
from pyrogram import Filters

__MODULE__ = "Spams"
__HELP__ = """
──「 **Spammer** 」──
-> `spam (count) (text)`
Floods text in the chat!

──「 **Spam letter** 」──
-> `cspam (text)`
Spam the text letter by letter.

──「 **Spam word** 」──
-> `wspam (text)`
Spam the text word by word.

──「 **Pic Spam [Disabled/Not Work]** 」──
-> `picspam (count) (link to image/gif)`
As if text spam was not enough !!

──「 **Spam Delay** 」──
-> `delayspam (delay) (count) (text)`
Floods text with delay int the chat!

NOTE : Spam at your own risk !!"
"""

@app.on_message(Filters.user("self") & Filters.command(["cspam"], Command))
async def tmeme(client, message):
    cspam = message.text.split(None, 1)
    if len(cspam) == 1:
        await message.edit("Usage: `cspam` (text)")
        return
    msg = cspam[1].replace(" ", "")
    await message.delete()
    for letter in msg:
        await client.send_message(message.chat.id, letter)

@app.on_message(Filters.user("self") & Filters.command(["wspam"], Command))
async def tmemes(client, message):
    args = message.text.split(None, 1)
    if len(args) == 1:
        await message.edit("Usage: `wspam` (text)")
        return
    msg = args[1].split()
    await message.delete()
    for word in msg:
        await client.send_message(message.chat.id, word)

@app.on_message(Filters.user("self") & Filters.command(["spam"], Command))
async def spammer(client, message):
    args = message.text.split(None, 2)
    if len(args) == 1:
        await message.edit("Usage: `spam` (counter) (text)")
        return
    counter = int(args[1])
    spam_message = str(args[2])
    await message.delete()
    await asyncio.wait([client.send_message(message.chat.id, spam_message) for i in range(counter)])

#@app.on_message(Filters.user("self") & Filters.command(["picspam"], Command))
async def tiny_pic_spam(client, message):
    args = message.text.split(None, 2)
    if len(args) == 1:
        await message.edit("Usage: `picspam` (count) (link pic/gif)")
        return
    counter = int(args[1])
    link = str(args[2])
    await message.delete()
    for i in range(counter):
        await client.send_document(message.chat.id, link)

@app.on_message(Filters.user("self") & Filters.command(["delayspam"], Command))
async def spammers(client, message):
    args = message.text.split(None, 3)
    if len(args) == 1:
        await message.edit("Usage: `delayspam` (delay) (count) (text)")
        return
    spamDelay = float(args[1])
    counter = int(args[2])
    spam_message = str(args[3])
    await message.delete()
    for i in range(counter):
        await client.send_message(message.chat.id, spam_message)
        await sleep(spamDelay)

