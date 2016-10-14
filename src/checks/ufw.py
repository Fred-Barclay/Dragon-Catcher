import subprocess

def ufw():
# TODO: check for open ports
	p2 = subprocess.Popen(['ufw', 'status', 'verbose'], stdout=subprocess.PIPE).communicate()[0]
	firewall_status = p2.split()

	# Is the firewall active (double-check)?
	if not firewall_status[1] == b'active':
		print('Your firewall is not active. \x1b[0;30;41m [WARN] \x1b[0m')
		print(firewall_status[1])
		total_warns.append('firewall_active_FAIL')

	else:
		# Is the firewall logging events?
		if not firewall_status[3] == b'on':
			print('Your firewall is not logging events. \x1b[6;36;43m [Advice] \x1b[0m')
			print(firewall_status[3])
			total_advice.append('firewall_log_FAIL')
			if not firewall_status[5] == b'deny' or firewall_status[5] == b'reject':
				print('Your firewall is allowing all inbound packets. \x1b[0;30;41m [WARN] \x1b[0m')
				print(firewall_status[5])
				total_warns.append('firewall_packets_FAIL')
			else:
				print('Your firewall does not allow inbound packets.')

		else:
			print('Your firewall is logging events')
		# Is the firewall rejecting unsolicited inbound packets?
			if not firewall_status[6] == b'deny' or firewall_status[6] == b'reject':
				print('Your firewall is allowing all inbound packets. \x1b[0;30;41m [WARN] \x1b[0m')
				print(firewall_status[6])
				total_warns.append('firewall_packets_FAIL')
			else:
				print('Your firewall does not allow inbound packets.')
