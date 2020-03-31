from nana import app, Command, logging
from pyrogram import Filters

import asyncio
import requests
import datetime
import os
import sys
import json
import shlex
#import subprocess

from shutil import rmtree
from nana.helpers.proc import Group as process, subprocess

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

async def send_out(client, message, msg):
	await message.edit("Message Overflow, send as file")
	with open("nana/cache/output.txt", "w+") as f:
		f.write(msg)

	if os.path.isfile("nana/cache/output.txt"):
		await client.send_document(message.chat.id, 
			"nana/cache/output.txt", 
			reply_to_message_id=message.message_id, 
			caption="`Output file`")
		os.remove("nana/cache/output.txt")

@app.on_message(Filters.user("self") & Filters.command(["loop"], Command))
async def loop(client, message):
	x = 0
	old = ""
	for i in range(10):
		old += str(x) + "\n"
		await message.edit(old)
		x += 1

@app.on_message(Filters.user("self") & Filters.command(["git"], Command))
async def git(client, message):
	if len(message.text.split()) == 1:
		await message.edit(__HELP__)
		return
	args = message.text.split(None, 1)
	argv = message.text.split(None, 4)
	argc = message.text.split(None, 2)
	msg = ""
	cmd = ""
	pwd = ""
	readall = False

	if argc[1] == "test" and argc[2]:
		cmd = argc[2]
		open(dir + "/.out", "w").write("")
		with open(dir + "/.cmd", "w") as f:
			f.write(cmd + " 2>&1 | tee .out")
		subprocess.Popen("bash .cmd", shell=True, cwd=dir)
		with open(dir + "/.out", "r") as f:
			r = f.read()
			await message.edit(r)
		return
	elif argc[1] == "ls":
		pwd = dir + "/" + conf["local"]
		cmd = "du -ah --max-depth=1"
	elif argv[1] == "delete":
		if len(argv) < 3:
			await message.edit("Ussage: `delete` **(folder)**")
			return
		lst = []
		for name in os.listdir(dir):
			if os.path.isdir(dir + "/" + name):
				lst.append(name)
		if not argv[2] in lst:
			await message.edit("Folder not available\nCheck folder with `.git dir`")
			return
		rmtree(dir + "/" + argv[2], ignore_errors=True)
		await message.edit("Success delete folder {}".format(argv[2]))
	if argv[1] == "clone" and argv[2]:
		pwd = dir
		cmd = "git clone {} {}".format(argv[2], dir + "/" + argv[3])
	elif argv[1] == "dir":
		if argv[2] == "ls":
			pwd = dir
			cmd = "du -ah --max-depth=1"
		else:
			conf.update({'local' : argv[2]})
			with open(git_conf,'w') as f:
				json.dump(conf, indent=4, fp=f)
			await message.edit("Successfully changed to `{}`".format(argv[2]))
			return
	elif argv[1] == "patch" and argv[2]:
		pwd = dir + "/" + conf["local"]
		if argv[2] == "abort":
			cmd = "git am --abort"
		else:
			cmd = "curl {}.patch | git am".format(argv[2])
	if not argv[1] in ["clone", "dir", "patch", "ls"]:
		pwd = dir + "/" + conf["local"]
		cmd = "git " + args[1]

	if argv[1] in ["diff", "show", "log"]:
		readall = True
	# teks = "python3 helper.py " + pwd + " " + cmd
	if not cmd: return
	cmd = shlex.split(cmd)
	if not readall:
		proc = process()
		p1 = proc.run(cmd, cwd = pwd)

		while proc.is_pending():
			lines = proc.readlines()
			for pr, line in lines:
				line = line.decode("utf-8")
				if line == "\n":
					msg += "\n"
					continue
				msg += line
				try: await message.edit(msg)
				except: pass
	else: # if readall is True
		proc = subprocess.Popen(cmd, 
			stdout=subprocess.PIPE, 
			stderr=subprocess.PIPE,
			cwd=pwd)
		output = proc.stdout.read()[:-1].decode("utf-8")
		# output, err = proc.communicate()
		# line = proc.stdout.read()[:-1]
		msg = output
		if len(msg) > 4096:
			await send_out(client, message, msg)
		else:
			if msg != "":
				asyncio.sleep(5)
				await message.edit("```{}```".format(msg))
			else: await message.edit("Return is empty")

