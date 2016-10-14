# apache2.py
# Copyright (C) 2016 Dragon Catcher authors
# This file is distributed under the same license as the Dragon Catcher package.

import subprocess

def apache2():
	'''Detect an actively running instance of apache 2'''
	p1 = subprocess.Popen(['pidof', 'apache2'], stdout=subprocess.PIPE).communicate()[0]
	if not len(p1.split()) == 0:
		print('''
		There is an actively running instance of apache2. You may want to
		investigate the cause. \x1b[6;36;43m [Advice] \x1b[0m
		''')
		print(p1.split())
	else:
		print('There are not detected instances of apache2.')
