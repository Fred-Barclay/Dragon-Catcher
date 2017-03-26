# run.sh
# Copyright (C) 2016-2017 Dragon Catcher authors
# This file is distributed under the same license as the Dragon Catcher package.
cd $(pwd)/src/
sudo python3 dragon-catcher.py
sudo rm -rf checks/__pycache__
