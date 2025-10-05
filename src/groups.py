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

from libqtile.config import ScratchPad, DropDown

groups.append(ScratchPad('scratchpad', [
    # define a drop down terminal.
    DropDown('term', cfg.terminal, opacity=0.8, height=0.6),
    # define a drop down calculator.
    DropDown('calc', 'galculator', opacity=0.9, width=0.4, height=0.6, x=0.3, y=0.1),
    # define a drop down notes.
    DropDown('notes', 'mousepad', opacity=0.9, width=0.6, height=0.8, x=0.2, y=0.1)
]))

