# not_owned.py
# Copyright (C) 2016-2017 Dragon Catcher authors
# This file is distributed under the same license as the Dragon Catcher package.

import subprocess
import os

def not_owned():
	'''Are there files in /home/$USER that are not owned by $USER?'''
	user = os.getlogin() #Unlike os.getuid(), this gives the actual (non-root, usually) user.
	home_var = '~'+user
	home_dir = os.path.expanduser(home_var)

	cmd = ['find', home_dir , '!', '-user', user, '-type', 'f']

	out = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
	out = out.decode('utf-8').split()

	if len(out) == 0:
		print('There are no files in your home directory that are owned by another user.')
	elif len(out) != 0:
		print('The following files in your home directory are owned by another user.  \x1b[6;36;43m [Advice] \x1b[0m')
		for file in out:
			print(file)
		print('You may want to investigate why you do not own these files.\n')
	else:
		print('not_owned.py has failed to run properly. Please contact the author with all relevant information.')

	return(out)
