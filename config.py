#!/usr/bin/env python

from src.keys import keys
from src.groups import groups
from src.layouts import layouts
# from src.widgets import widgets
from src.screens import screens
import src.autostart
import src.app_rules  # Importar reglas de aplicaciones para activar hooks

keys = keys
groups = groups
layouts = layouts
# widgets = widgets
screens = screens

# ----------------------------
# -------- Launcher ----------
# ----------------------------

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
extentions = []
auto_fullscreen = False
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wl_xcursor_theme = None
wl_xcursor_size = 24
wmname = "LG3D"
