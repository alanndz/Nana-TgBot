import re
import pyrogram

from pyrogram import Filters, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQueryHandler
from nana import setbot, AdminSettings, log, Command, BotName, app, Owner
from __main__ import HELP_COMMANDS, input
from nana.helpers.misc import paginate_modules

__MODULE__ = "Helper"
__HELP__ = """
A Module to check module without assistent bot

Usage: `.help` (*module)"""

def get_help():
	list_help = list(HELP_COMMANDS.keys())

	help_ = ""
	for i in list_help:
		help_ += "`{}`".format(i)
		help_ += "\n"
	return list_help, help_

@app.on_message(Filters.user("self") & Filters.command(["help"], Command))
async def help_command(client, message):
	#await message.edit(list(HELP_COMMANDS.keys()))
	#await message.edit(HELP_COMMANDS["afk"].__HELP__)
	inp = input(message)
	if inp:
		if inp in get_help()[0]:
			_ = "**{} Module**\n{}".format(HELP_COMMANDS[inp].__MODULE__, HELP_COMMANDS[inp].__HELP__)
			await message.edit(_)
		else:
			await message.edit("Module not found, check with command `{}help`".format(Command[0]))
	else:
 		await message.edit("**Module's** List:\n\n" + get_help()[1] + "\nUsage: `help` (*module)")

