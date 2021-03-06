Dragon Catcher
==============
*There be dragons.*

A simple Python 3 script for beginners and developers alike, to catch common
desktop Linux security errors:
 - Ever disable the firewall and then forget to re-enable it?
 - Ever run Apache to test something and then forget to turn it off?
 - Ever test openssh-server and then accidentally leave it running?

Dragon Catcher is the tool for you! It's designed to test for common Linux
security errors, like the ones above. If it finds any, it returns a
[WARN] or [Advice], depending on the severity.

Currently, the following tests are included:

 - Is the firewall running?
	 - Is the firewall logging security events? (UFW only)
	 - Is the firewall blocking unsolicited inbound packets? (UFW only)


 - Has someone tried and failed to log in as root recently? (Useful for
	 detecting brute-force login attempts.)

 - Is the ssh server running?

 - Is httpd running?

 - Is apache2 running?

 - Are there files in the user's home that are owned by someone other than that user? 


Installation
============
Currently there is no (supported) way to install Dragon Catcher. You will need
to run it as a script with admin privileges:  
```
git clone https://www.github.com/Fred-Barclay/Dragon-Catcher.git
cd Dragon Catcher
./run.sh
```

In the future I plan on adding an installation option for at least Debian (and
related distros such as Linux Mint) and probably Fedora as well.

Roadmap
=======
*Where did we come from? Where are we going?*

*Is there a giant pizza at the end?*    :-)

Please view the ROADMAP file.

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
