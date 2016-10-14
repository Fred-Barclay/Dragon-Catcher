# ufw.py
# Copyright (C) 2016 Dragon Catcher authors
# This file is distributed under the same license as the Dragon Catcher package.

import subprocess

def ufw():
	'''Tests for ufw'''
# TODO: check for open ports
	p1 = subprocess.Popen(['ufw', 'status', 'verbose'], stdout=subprocess.PIPE).communicate()[0]
	ufw_status = p1.split()

	# ufw is not active
	if not ufw_status[1] == b'active':
		print('Your firewall is not active. \x1b[0;30;41m [WARN] \x1b[0m')
		print(ufw_status[1])
		total_warns.append('firewall_active_FAIL')

	# ufw is active
	else:
		# Is ufw logging events?
		if not ufw_status[3] == b'on':
			print('Your firewall is not logging events. \x1b[6;36;43m [Advice] \x1b[0m')
			print(ufw_status[3])
			# total_advice.append('firewall_log_FAIL')
			if not ufw_status[5] == b'deny' or ufw_status[5] == b'reject':
				print('Your firewall is allowing all inbound packets. \x1b[0;30;41m [WARN] \x1b[0m')
				print(ufw_status[5])
				total_warns.append('firewall_packets_FAIL')
			else:
				print('Your firewall does not allow inbound packets.')

		else:
			print('Your firewall is logging events')
		# Is ufw rejecting unsolicited inbound packets?
			if not ufw_status[6] == b'deny' or ufw_status[6] == b'reject':
				print('Your firewall is allowing all inbound packets. \x1b[0;30;41m [WARN] \x1b[0m')
				print(ufw_status[6])
				total_warns.append('firewall_packets_FAIL')
			else:
				print('Your firewall does not allow inbound packets.')