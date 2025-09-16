#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: autostart.py
Description: Configuration file for Qtile window manager.
Author: Your Name
Date: YYYY-MM-DD
"""
import os


autoinit = [
    "feh --bg-fill --randomize /usr/share/backgrounds/phast/*",
    "picom --experimental-backends",
    "xrandr --output eDP-1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output HDMI-1 --mode 1920x1080 --pos 1920x0 --rotate normal --output DP-1 --off",
]

for cmd in autoinit:
    os.system(cmd)

# vim: ft=python
