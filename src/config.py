#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: config.py
Description: Configuration file for Qtile window manager.
Author: Your Name
Date: YYYY-MM-DD
"""

import os
from datetime import datetime
from src.colors import colors
import random

# variables privadas
__datetime = datetime.now().strftime("%Y%m%d%I%M%S%f")
__home = os.path.expanduser("~")
__screenshots = os.path.join(__home, "Screenshots")


def get_screenshot_path():
    timestamp = datetime.now().strftime("%Y%m%d%I%M%S%f")
    return os.path.join(__screenshots, f"Screenshot-{timestamp}.png")


# Variables
mod = "mod4"
mod_aux = "control"
font = "Hack Nerd Font"
text_size = 16
icon_size = 16
bar_size = 24
bar_opacity = 0.9
terminal = "kitty"
browser = "brave"
file_manager = "thunar"
editor = "vim"
wallpapers = "/usr/share/backgrounds/phast"
if not os.path.exists(wallpapers):
    wallpapers = os.path.expanduser("~/.backgrounds")
    if not os.path.exists(wallpapers):
        os.makedirs(wallpapers)
# tema por defecto: [gruvbox, darcula, nord, solarized-dark, one-dark, ]
themes = list(colors.keys())
random_theme = random.choice(themes)
theme = colors[random_theme]
screenshot = get_screenshot_path()
