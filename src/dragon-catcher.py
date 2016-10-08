#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Dragon Catcher - Catch common security mistakes for desktop Linux
# Copyright (C) 2016 Dragon Catcher authors.
# Dual-licensed under the GPLv2 (or, at your option, any later version) and
# custom licensing terms:
# GPL v2:
#   This program is free software; you can redistribute it and/or
#   modify it under the terms of the GNU General Public License
#   as published by the Free Software Foundation; either version 2
#   of the License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
# Custom license terms:
#   You are hereby granted a perpetual, irrevocable license to copy, modify,
#   publish, release, and distribute this program as you see fit. However,
#   under no circumstances may you claim original authorship of this program;
#   you must credit the original author(s). You may not remove the listing of
#   the original author(s) from the source code, though you may change the
#   licensing terms. If you publish or release binaries or similarly compiled
#   files, you must credit the author(s) on your home and/or distribution page,
#   whichever applies. In your documentation, you must credit the author(s) for
#   the portions of their code you have used. This, of course, does not revoke
#   or change your right to claim original authorship to any portions of the
#   code that you have written.
#
#   You must agree to assume all liability for your use of the program, and to
#   indemnify and hold harmless the author(s) of this program from any liability
#   arising from use of this program, including, but not limited to: loss of
#   data, death, dismemberment, or injury, and all consequential and
#   inconsequential damages.
#
#   For clarification, contact Fred Barclay:
#       https://github.com/Fred-Barclay
#       BugsAteFred@gmail.com

import subprocess

total_warns = []
total_advice = []

# Is the root account enabled?
p1 = subprocess.Popen(["passwd", "-S", "root"], stdout=subprocess.PIPE).communicate()[0]
noroot = p1.split()[1]
if not noroot == b'L':
	print('The root account is enabled on your system. [WARN]')
	print(noroot)
	total_warns.append('noroot_FAIL')
else:
	print('The root account is disabled on your system.')

# Is the firewall running? (only ufw at the moment)
# TODO: check for open ports
p1 = subprocess.Popen(['ufw', 'status', 'verbose'], stdout=subprocess.PIPE).communicate()[0]
firewall_status = p1.split()

# Is the firewall active?
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

# Has someone recently tried and failed to log in as root?
p1 = subprocess.Popen(['lastb', 'root'], stdout=subprocess.PIPE).communicate()[0]
root_attempts = p1.split()
if root_attempts[0] == b'root':
	print('Someone has tried (and failed) to log in as root. \x1b[6;36;43m [Advice] \x1b[0m')
	print(root_attempts)
	total_advice.append('attempted_root_login_FAIL')

# Final messages:
print('You have %d warnings.' % len(total_warns))
print('You have %d advisories.' % len(total_advice))
