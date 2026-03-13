#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: screens.py
Description: Configuration file for Qtile window manager.
Author: Your Name
Date: YYYY-MM-DD
"""

import subprocess
from libqtile.log_utils import logger
from libqtile.config import Screen
from src.widgets import primary_widgets, secondary_widgets
from src.status_bar import status_bar

screens = [
    Screen(top=status_bar(primary_widgets)),
]

monitors = "xrandr --query | grep ' connected' | cut -d ' ' -f1 | wc -l"

command = subprocess.run(monitors, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if command.returncode != 0:
      error = command.stderr.decode("UTF-8")
      logger.error(f"Failed counting monitors using {monitors}:\n{error}")
      connected_monitors = 1
else:
      connected_monitors = int(command.stdout.decode("UTF-8")) 

if connected_monitors > 1:
    for _ in range(1, connected_monitors):
        screens.append(Screen(top=status_bar(secondary_widgets)))

