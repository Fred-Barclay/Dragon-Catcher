# sshd.py
# Copyright (C) 2016 Dragon Catcher authors
# This file is distributed under the same license as the Dragon Catcher package.

import subprocess

def sshd():
	'''Is the ssh server (not client) running?'''
	p1 = subprocess.Popen(['pidof', 'sshd'], stdout=subprocess.PIPE).communicate()[0]
	if not len(p1.split()) == 0:
		print('There is an actively running instance of ssh-server. \x1b[0;30;41m [WARN] \x1b[0m')
		print(p1.split())
		total_warns.append('sshd_running_FAIL')
	else:
		print('The ssh server does not seem to be running.')
