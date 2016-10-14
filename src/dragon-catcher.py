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
import os
import sys
# From 'tests' directory
from checks import apache2, httpd, rootlog, sshd, ufw

total_warns = []
total_advice = []

# Make sure we are running as root
if os.geteuid() != 0:
	print('This script requires elevated priviledges!\nExiting.')
	sys.exit(0)

# Which firewall is present?
# UFW
if subprocess.Popen(['service', 'ufw', 'status'], \
	stdout=subprocess.PIPE).communicate()[0] == b'Firewall is running...done.\n':
	firewall = 'ufw'
#Firewalld
#if subprocess.Popen(['service', 'firewalld', status'], \
#	stdout=subprocess.PIPE).communicate()[0] ==
#	firewall = 'firewalld'

# Not running/not recognised
else:
	firewall = 0

# UFW
if firewall == 'ufw':
	ufw.ufw()
# elif firewall == 'firewalld':
# do something

# No detected firewall
elif firewall == 0: # Not running/not recognised
	print('Your firewall is not active. \x1b[0;30;41m [WARN] \x1b[0m')

# Check for apache2
apache2.apache2()

# Check for httpd
httpd.httpd()

# Check for recent root login attempts
rootlog.rootlog()

# Check for running sshd
sshd.sshd()

# Final messages
print('You have %d warnings' % len(total_warns))
print('You have %d advisories' % len(total_advice))
