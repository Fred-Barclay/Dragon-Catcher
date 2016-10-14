# firewalld.py
# Copyright (C) 2016 Dragon Catcher authors
# This file is distributed under the same license as the Dragon Catcher package.

import subprocess

def firewalld():
	'''Tests for firewalld'''
	p1 = subprocess.Popen(['firewall-cmd', '--state'], stdout=subprocess.PIPE \
		).communicate()[0]

	# Firewalld is not running
	if not p1 == b'running\n':
		print('Your firewall is not active. \x1b[0;30;41m [WARN] \x1b[0m')
		print(p1)
	else:
		print('Your firewall is active.')
