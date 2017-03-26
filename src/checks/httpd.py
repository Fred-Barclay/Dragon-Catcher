# httpd.py
# Copyright (C) 2016-2017 Dragon Catcher authors
# This file is distributed under the same license as the Dragon Catcher package.

import subprocess

def httpd():
	'''Detect an actively running instance of httpd.'''
	p1 = subprocess.Popen(['pidof', 'httpd'], stdout=subprocess.PIPE).communicate()[0]
	if not len(p1.split()) == 0:
		print('There is an actively running instance of httpd.You may want')
		print('to investigate the cause. \x1b[6;36;43m [Advice] \x1b[0m')
		print(p1.split())
	else:
		print('There are no detected instances of httpd.')
