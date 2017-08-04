# rootlog.py
# Copyright (C) 2016-2017 Dragon Catcher authors
# This file is distributed under the same license as the Dragon Catcher package.

import subprocess

def rootlog():
	'''Has someone tried and failed to log in as root recently?'''
	p1 = subprocess.Popen(['lastb', 'root'], stdout=subprocess.PIPE).communicate()[0]
	p1 = p1.decode('utf-8')
	root_attempts = p1.split()
	if root_attempts[0] == 'root':
		print('Someone has tried (and failed) to log in as root. \x1b[6;36;43m [Advice] \x1b[0m')
		print(root_attempts)
	else:
		print('There are no recent detected failed attempts to log in as root.')
