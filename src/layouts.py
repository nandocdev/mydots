#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: layouts.py
Description: Configuration file for Qtile window manager.
Author: Your Name
Date: YYYY-MM-DD
"""

from src.config import theme
from libqtile import layout
from libqtile.config import Match


__base = {
   'border_focus': theme['cyan'],
   'border_width': 1,
   'margin': 3
}

layouts = [
    layout.Max(),
    layout.MonadTall(**__base),
    layout.MonadWide(**__base),
    layout.Bsp(**__base),
    layout.Matrix(**__base),
    layout.RatioTile(**__base),
    # layout.Columns(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
    ],
    border_focus=theme['comment']
)