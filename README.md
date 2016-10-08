Dragon Catcher
==============

A simple Python 3 script to catch common desktop Linux security errors, like
forgetting to (re)enable the firewall.

Description
===========
Dragon Catcher is designed to test for common Linux security errors. If it finds
errors, then it gives a [WARN] or [Advice], depending on the severity.

Currently, the following tests are included:
 - Is the root account enabled (can someone log into root)?
 
 - Is the firewall running? (Currently only ufw is supported. I plan on adding
	support for firewalld as well.)
	 - Is the firewall logging security events?
	 - Is the firewall blocking unsolicited inbound packets?


 - Has someone tried and failed to log in as root recently? (Useful for
	 detecting brute-force login attempts.)

 - Is the ssh server running?


Installation
============
Currently there is no (supported) way to install Dragon Catcher. You will need
to run it as a script with admin privileges:  
`sudo python3 dragon-catcher.py`  
or  
`gksudo python3 dragon-catcher.py`  

In the future I plan on adding an installation option for at least Debian (and
related distros such as Linux Mint) and probably Fedora as well.

Contributing
============
Contributions of any sort are welcome! Please be sure to test any code changes
first, though... :-)

If you would like to see a feature added but don't know how to code it, please
open an Issue or contact me at BugsAteFred@gmail.com.

Credits
=======
Inspired by https://github.com/snare/idiot.


License
=======
Dragon Catcher is dual-licensed under the GPLv2, or, at your option, any later
version; and custom, highly-permissive licensing terms.

The text for both can be found in the COPYING file. A list of authors is in the
AUTHORS file.

Copyright (C) 2016 Dragon Catcher authors.
