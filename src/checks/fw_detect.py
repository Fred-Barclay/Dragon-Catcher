# fw_detect.py
# Copyright (C) 2016-2017 Dragon Catcher authors
# This file is distributed under the same license as the Dragon Catcher package.

# Detect if a firewall is loaded and running.

import subprocess
from checks import ufw, firewalld

def init_system():
	'''Figure out the running init system.'''
	global init
	# Is systemd running?
	out1 = subprocess.Popen(['pidof', 'systemd'], stdout=subprocess.PIPE).communicate()[0]
	out1 = out1.decode('utf-8')
	if  out1 != '':
		# systemd is running
		init = 'systemd'
	else:
		# Upstart, sysvinit, etc
		init = 'other'
	# return(out1)
	return(out1, init)


def firewall_detect():
	'''Detect if the firewall is ufw, firewalld, or unknown/not running.'''
	global firewall

	if init == 'systemd':
		if subprocess.Popen(['systemctl', 'is-active', 'ufw'], \
				stdout=subprocess.PIPE).communicate()[0] == b'active\n':
			firewall = 'ufw'

		elif subprocess.Popen(['systemctl', 'is-active', 'firewalld'], \
				stdout=subprocess.PIPE).communicate()[0] == b'active\n':
			firewall = 'firewalld'

		else:
			firewall = 0

	elif init == 'other':
		if subprocess.Popen(['service', 'ufw', 'status'], \
				stdout=subprocess.PIPE).communicate()[0] == b'Firewall is running...done.\n':
			firewall = 'ufw'

		elif subprocess.Popen(['service', 'firewalld', 'status'], \
				stdout=subprocess.PIPE).communicate()[0] == b'firewalld is running.\n':
			firewall = 'firewalld'

		else:
			firewall = 0

def firewall_diagnose():
	'''Test the firewall settings.'''
	if firewall == 'ufw':
		print('Your active firewall is `ufw`.')
		ufw.ufw()

	elif firewall == 'firewalld':
		print('Your active firewall is `firewalld`.')
		firewalld.firewalld()

	elif firewall == 0: # Not running/not recognised
		print('Your firewall is not active. \x1b[0;30;41m [WARN] \x1b[0m')
