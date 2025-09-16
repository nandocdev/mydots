#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: widgets.py
Description: Configuration file for Qtile window manager.
Author: Your Name
Date: YYYY-MM-DD
Colores dsiopnibles:
   background
   foreground
   comment
   cyan
   green
   orange
   pink
   purple
   red
   yellow
   bright_blue
   bright_cyan
   bright_green
   bright_orange
   bright_pink
   bright_purple
   bright_red
   bright_yellow
"""

import random
from src.config import theme, font, text_size, icon_size
from libqtile import widget
from src.functions import get_network_interface


def __randomColor(diccionario):
    #  crea una copia del diccionario
    diccionario = diccionario.copy()
    if not diccionario:
        return None  # Retorna None si el diccionario está vacío
    # elimina el key 'background' del diccionario
    diccionario.pop("background")
    return random.choice(list(diccionario.keys()))


def __base():
    return {
        "background": theme["background"],
        "foreground": theme[__randomColor(theme)],
    }


def __inverse():
    return {"background": theme["foreground"], "foreground": theme["background"]}


def __separator():
    return widget.Sep(**__base(), linewidth=0, padding=5)


def __icon(icon):
    return widget.TextBox(text=icon, fontsize=icon_size, padding=0, **__base())


def __textInput(text):
    s = text.split("-")
    return s[-1].capitalize()


# definimos una funcion para cada widget
def widgetGrupBox():
    return widget.GroupBox(
        **__base(),
        font=font,
        fontsize=text_size,
        margin_y=3,
        margin_x=0,
        padding_y=8,
        padding_x=5,
        borderwidth=3,
        active=theme["bright_green"],
        inactive=theme["bright_purple"],
        rounded=False,
        highlight_method="line",
        highlight_color=[theme["background"], theme["background"]],
        urgent_alert_method="line",
        urgent_border=theme["red"],
        this_current_screen_border=theme["yellow"],
        this_screen_border=theme["orange"],
        other_current_screen_border=theme["comment"],
        other_screen_border=theme["comment"],
        disable_drag=True,
        hide_unused=True,
        toggle=True,
    )


def widgetWindowName():
    return widget.WindowName(
        font=font,
        fontsize=text_size - 4,
        padding=5,
        foreground=theme["cyan"],
        background=theme["background"],
        parse_text=__textInput,
    )


def widgetPrompt():
    return widget.Prompt()


def widgetCheckUpdates():
    return widget.CheckUpdates(
        **__base(),
        distro="Arch_checkupdates",
        display_format="  {updates}",
        no_update_string="0",
        update_interval=1800,
        colour_have_updates=theme[__randomColor(theme)],
        colour_no_updates=theme[__randomColor(theme)],
    )


def widgetNet():
    return widget.Net(
        **__base(), interface=get_network_interface(), format="{down} ↓↑ {up}"
    )


def widgetWlan():
    return widget.Wlan(
        **__base(),
        interface=get_network_interface(),
        format="{essid} {percent:2.0%}",
        disconnected_message="Disconnected",
        update_interval=1,
        max_chars=10,
    )


def widgetWlanSup():
    interface = get_network_interface()
    # Solo usar Wlan si es una interfaz inalámbrica
    if any(x in interface for x in ["wlan", "wlp", "wifi"]):
        return widget.Wlan(
            **__base(),
            interface=interface,
            format="{essid} {percent:2.0%}",
            disconnected_message="Disconnected",
            update_interval=1,
            max_chars=10,
        )
    else:
        # Devolver un widget placeholder para interfaces cableadas
        return widget.TextBox(**__base(), text="Ethernet")


def widgetMemory():
    return widget.Memory(
        **__base(), format="{MemUsed: .2f}{mm}/{MemTotal: .2f}{mm}", measure_mem="G"
    )


def widgetCpu():
    return widget.CPU(
        **__base(),
        format="{load_percent}%",
    )


def widgetDisk():
    return widget.HDD(
        **__base(), format="HDD {HDDPercent}%", update_interval=200, device="nvme0n1"
    )


def widgetBattery():
    return widget.Battery(
        **__base(),
        format="{char} {percent:2.0%} {watt:.2f} W",
        charge_char="󱘖 ",
        discharge_char=" ",
        empty_char="󱚢 ",
        full_char="󱇇 ",
    )


def widgetClock():
    return widget.Clock(
        **__base(),
        format="%A, %d %B - %H:%M",
    )


def widgetSystray():
    return widget.Systray(
        **__base(),
    )


def widgetKeyboardLayout():
    return widget.KeyboardLayout(
        **__base(),
        configured_keyboards=["latam", "es"],
        display_map={"latam": "󰌓 ", "es": " "},
    )


def widgetVolume():
    return widget.Volume(
        **__base(),
        # emoji=True,
        emoji_list=[" ", " ", " ", " "],
    )


def widgetBacklight():
    return widget.Backlight(
        **__base(),
        backlight_name="intel_backlight",
        fmt="󰝩 {}",
    )


def widgetCurrentLayout():
    return widget.CurrentLayout(
        **__base(),
        fmt="󰄯 {}",
    )


def widgetCurrentLayoutIcon():
    return widget.CurrentLayout(
        **__base(),
        scale=0.7,
    )


def widgetPomodoro():
    return widget.Pomodoro(
        **__base(),
    )


primary_widgets = [
    widgetGrupBox(),
    __separator(),
    widgetWindowName(),
    __separator(),
    __separator(),
    widgetCheckUpdates(),
    __separator(),
    __icon("󰛵 "),
    widgetWlanSup(),
    widgetNet(),
    __separator(),
    widgetVolume(),
    __separator(),
    __icon(" "),
    widgetCpu(),
    __separator(),
    __icon("󰪏 "),
    widgetMemory(),
    __separator(),
    __icon("󰋊 "),
    widgetDisk(),
    __separator(),
    widgetBattery(),
    __separator(),
    __icon("󰔠 "),
    widgetClock(),
    widgetKeyboardLayout(),
    widgetCurrentLayoutIcon(),
]

secondary_widgets = [
    widgetGrupBox(),
    __separator(),
    widgetWindowName(),
    __separator(),
    widgetCheckUpdates(),
    __separator(),
    widgetWlan(),
    __separator(),
    widgetCpu(),
    __separator(),
    widgetMemory(),
    __separator(),
    widgetDisk(),
    __separator(),
    widgetBattery(),
    __separator(),
    widgetClock(),
    __separator(),
    widgetSystray(),
    widgetKeyboardLayout(),
]
