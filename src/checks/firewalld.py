# firewalld.py
# Copyright (C) 2016-2017 Dragon Catcher authors
# This file is distributed under the same license as the Dragon Catcher package.

import subprocess

def firewalld():
	'''Tests for firewalld'''
	out = subprocess.Popen(['firewall-cmd', '--state'], stdout=subprocess.PIPE \
		).communicate()[0]
	out = p1.decode('utf-8')

	# Firewalld is not running
	if not out == 'running\n':
		print('Your firewall is not active. \x1b[0;30;41m [WARN] \x1b[0m')
		print(out)
	else:
		print('Your firewall is active.')

	return(out)
