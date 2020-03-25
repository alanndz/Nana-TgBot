import asyncio
import requests
import datetime
import os
import re
import shutil
import subprocess
import sys
import traceback
import json

from nana import app, Command, logging
from nana.helpers.parser import mention_markdown
from pyrogram import Filters

__MODULE__ = "Git"
__HELP__ = """
This command means for helping development
Usage: .git (command)

──「 **Cloning** 」──
-> `clone (link_repository) (name_folder`
Cloning repository

──「 **Directory** 」──
-> `dir (ls/name_folder)`
ls for checking folder available, name_fooder to set this folder
Set default Directory

──「 **Patching** 」──
-> `patch (url_commit)`
Execute command shell

──「 **Take log** 」──
-> `log`
Edit log message, or deldog instead

──「 **Get Data Center** 」──
-> `dc`
Get user specific data center
"""

cwd = os.getcwd()
dir = cwd + "/git"
git_conf = dir + "/.config.json"

if not os.path.isdir(dir):
	os.mkdir(dir)

def load_local():
	if not os.path.isfile(git_conf):
		with open(git_conf,'w') as f:
			data = {
				'local': ''
				}
			json.dump(data,indent=4,fp=f)
	with open(git_conf,'r') as f:
		config = json.load(f)
	return config

conf = load_local()

@app.on_message(Filters.user("self") & Filters.command(["git"], Command))
async def git(client, message):
	if len(message.text.split()) == 1:
		await message.edit(__HELP__)
		return
	args = message.text.split(None, 1)
	argv = message.text.split(None, 4)
	if argv[1] == "clone":
		pwd = dir
		cmd = "git clone {} {}".format(argv[2], dir + "/" + argv[3])
	elif argv[1] == "dir" and argv[2]:
		if argv[2] == "ls":
			pwd = dir
			cmd = "ls"
		else:
			conf.update({'local' : argv[2]})
			with open(git_conf,'w') as f:
				json.dump(conf, indent=4, fp=f)
			await message.edit("Successfully changed to `{}`".format(argv[2]))
			return
	elif argv[1] == "patch":
		pwd = dir + "/" + conf["local"]
		if argv[2] == "abort":
			cmd = "git am --abort"
		else:
			cmd = "curl {}.patch | git am".format(argv[2])
	if not argv[1] in ["clone", "dir", "patch"]:
		pwd = dir + "/" + conf["local"]
		cmd = "git " + args[1]
	teks = "python helper.py " + pwd + " " + cmd
	if "\n" in teks:
		code = teks.split("\n")
		output = ""
		for x in code:
			shell = re.split(''' (?=(?:[^'"]|'[^']*'|"[^"]*")*$)''', x)
			try:
				process = subprocess.Popen(
					shell,
					stdout=subprocess.PIPE,
					stderr=subprocess.PIPE
				)
			except Exception as err: 
				await message.edit("""
**Input:**
```{}```

**Error:**
```{}```
""".format(cmd, err))
			output += "**{}**\n".format(code)
			output += process.stdout.read()[:-1].decode("utf-8")
			output += "\n"
	else:
		shell = re.split(''' (?=(?:[^'"]|'[^']*'|"[^"]*")*$)''', teks)
		for a in range(len(shell)):
			shell[a] = shell[a].replace('"', "")
		try:
			process = subprocess.Popen(
				shell,
				stdout=subprocess.PIPE,
				stderr=subprocess.PIPE
			)
		except Exception as err:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			errors = traceback.format_exception(etype=exc_type, value=exc_obj, tb=exc_tb)
			await message.edit("""**Input:**\n```{}```\n\n**Error:**\n```{}```""".format(cmd, "".join(errors)))
			return
		output = process.stdout.read()[:-1].decode("utf-8")
	if str(output) == "\n":
		output = None
	if output:
		if len(output) > 4096:
			file = open("nana/cache/output.txt", "w+")
			file.write(output)
			file.close()
			await client.send_document(message.chat.id, "nana/cache/output.txt", reply_to_message_id=message.message_id, caption="`Output file`")
			os.remove("nana/cache/output.txt")
			return
		await message.edit("""**Input:**\n```{}```\n\n**Output:**\n```{}```""".format(cmd, output))
	else:
		await message.edit("**Input: **\n`{}`\n\n**Output: **\n`No Output`".format(cmd))

