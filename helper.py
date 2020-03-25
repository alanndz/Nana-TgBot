#!/usr/bin/env python

import subprocess
import os
import sys

#cwd = os.getcwd()
#cwd += '/nana'

def sh(cmd, cwd, input=""):
	rst = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, input=input.encode("utf-8"), cwd=cwd)
	assert rst.returncode == 0, rst.stderr.decode("utf-8")
	return rst.stdout.decode("utf-8")

if __name__ == "__main__":
	argv = sys.argv[1:]
	args = sys.argv[2:]
	if len(argv) == 0 or len(args) == 0:
		sys.exit()
	if argv[0] == "cwd":
		cwd = os.getcwd()
	else:
		cwd = argv[0]
	cmd = " ".join(args)
	print(sh(cmd, cwd))
