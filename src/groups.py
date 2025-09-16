#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: groups.py
Description: Configuration file for Qtile window manager.
Author: Your Name
Date: YYYY-MM-DD
"""

import src.config as cfg
from src.keys import keys
from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.config import Group

groups = [
    Group(" ", layout="monadtall"),
    Group(" ", layout="monadtall"),
    Group(" ", layout="monadtall"),
    Group("󰖟 ", layout="monadtall"),
    Group(" ", layout="monadtall"),
    Group(" ", layout="monadtall"),
    Group(" ", layout="monadtall"),
    Group(" ", layout="monadtall"),
    Group(" ", layout="monadtall"),
]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend(
        [
            Key([cfg.mod], actual_key, lazy.group[group.name].toscreen()),
            Key([cfg.mod, cfg.mod_aux], actual_key, lazy.window.togroup(group.name)),
        ]
    )

