# apache2.py
# Copyright (C) 2016-2017 Dragon Catcher authors
# This file is distributed under the same license as the Dragon Catcher package.

import subprocess

def apache2():
	'''Detect an actively running instance of apache 2'''
	out = subprocess.Popen(['pidof', 'apache2'], stdout=subprocess.PIPE).communicate()[0]
	out = out.decode('utf-8').split()
	if len(out) != 0:
		print('There is an actively running instance of apache2. You may want')
		print('to investigate the cause. \x1b[6;36;43m [Advice] \x1b[0m')
		print(out)
	else:
		print('There are not detected instances of apache2.')
