# firewalld.py
# Copyright (C) 2016-2017 Dragon Catcher authors
# This file is distributed under the same license as the Dragon Catcher package.

import subprocess

def firewalld():
	'''Tests for firewalld'''
	p1 = subprocess.Popen(['firewall-cmd', '--state'], stdout=subprocess.PIPE \
		).communicate()[0]
	p1 = p1.decode('utf-8')

	# Firewalld is not running
	if not p1 == 'running\n':
		print('Your firewall is not active. \x1b[0;30;41m [WARN] \x1b[0m')
		print(p1)
	else:
		print('Your firewall is active.')
