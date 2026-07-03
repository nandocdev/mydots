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

from src.config import (
    theme,
    font,
    text_size,
    icon_size,
    email_user,
    email_server,
    email_mbox,
    email_keyring_service,
    email_client,
    backlight_name,
    disk_device,
    keyboard_layouts,
    bar_size,
)
from libqtile import widget, bar
from libqtile.lazy import lazy
from src.functions import get_network_interface
from libqtile.widget import ImapWidget
from widgets.internet_status import InternetStatus

# from libqtile.widget.bluetooth import Bluetooth
import keyring

# Sistema de colores consistente para mejor diseño
# Mapeo de widgets a colores del tema para consistencia visual
_widget_colors = {
    "default": "cyan",
    "network": "bright_cyan",
    "system": "bright_green",
    "media": "bright_pink",
    "status": "bright_yellow",
    "info": "comment",
}


def __base(color_key="default"):
    """Retorna estilos base con color consistente del tema"""
    color = _widget_colors.get(color_key, "cyan")
    return {
        "background": theme["background"],
        "foreground": theme[color],
    }


def __inverse():
    return {"background": theme["foreground"], "foreground": theme["background"]}


def __separator():
    """Separador con mejor espaciado visual"""
    return widget.Sep(**__base("info"), linewidth=1, padding=12, size_percent=50)


def __icon(icon, color_key="default", is_pill=False):
    """Icono con mejor padding y color consistente"""
    base_style = __base(color_key)
    if is_pill:
        # Si es parte de una píldora, invertimos colores
        base_style = {"background": theme[_widget_colors.get(color_key, "cyan")], "foreground": theme["background"]}
        
    return widget.TextBox(text=icon, font=font, fontsize=icon_size + 4, padding=6, **base_style)


def __pill_open(color_key="default"):
    """Abre una cápsula con el color del tema (estilo triángulo)"""
    color = theme[_widget_colors.get(color_key, "cyan")]
    return widget.TextBox(
        text="\uE0BA",
        font=font,
        fontsize=bar_size + 14,
        padding=0,
        foreground=color,
        background=theme["background"]
    )


def __pill_close(color_key="default"):
    """Cierra una cápsula con el color del tema (estilo triángulo)"""
    color = theme[_widget_colors.get(color_key, "cyan")]
    return widget.TextBox(
        text="\uE0BC",
        font=font,
        fontsize=bar_size + 14,
        padding=0,
        foreground=color,
        background=theme["background"]
    )


def __pill_base(color_key="default"):
    """Estilo base para el contenido de una píldora (colores invertidos)"""
    color_name = _widget_colors.get(color_key, "cyan")
    return {
        "background": theme[color_name],
        "foreground": theme["background"],
    }


def __textInput(text):
    if not text:
        return ""
    s = text.split("-")
    return s[-1].strip().capitalize()


# definimos una funcion para cada widget
def widgetGrupBox():
    return widget.GroupBox(
        **__base(),
        font=font,
        fontsize=text_size,
        margin_y=3,
        margin_x=0,
        padding_y=8,
        padding_x=10,
        borderwidth=2,
        active=theme["bright_green"],
        inactive=theme["comment"],
        rounded=False,
        highlight_method="line",
        highlight_color=[theme["background"], theme["background"]],
        this_current_screen_border=theme["cyan"],
        this_screen_border=theme["comment"],
        other_current_screen_border=theme["background"],
        other_screen_border=theme["background"],
        disable_drag=True,
        hide_unused=True,
        toggle=True,
    )


def widgetWindowName():
    """Widget de nombre de ventana con mejor diseño"""
    return widget.WindowName(
        font=font,
        fontsize=text_size - 2,
        padding=10,
        foreground=theme["foreground"],
        background=theme["background"],
        parse_text=__textInput,
        max_chars=50,
        fmt="  {}",
        markup=False,
    )


def widgetPrompt():
    return widget.Prompt(
        **__base("info"),
        font="Hack Nerd Font",  # Fuente monoespaciada ideal para prompts
        fontsize=14,
        cursor=True,
        cursor_color="88c0d0",  # Azul claro
        cursorblink=0.3,
        prompt="> ",  # Prompt simple
        fmt='<span foreground="#a3be8c">[>_]</span> {}',  # Formato con markup
        markup=True,
        max_history=50,
        ignore_dups_history=True,
        record_history=True,
        bell_style="visual",  # Alerta visual para inicio/fin del historial
        visual_bell_color="bf616a",  # Rojo para el bell visual
        visual_bell_time=0.1,
        padding=5,
    )


def widgetCheckUpdates(is_pill=True):
    """Widget de actualizaciones con intervalos optimizados"""
    style = __pill_base("status") if is_pill else __base("status")
    return widget.CheckUpdates(
        **style,
        distro="Arch_checkupdates",
        display_format="󰚰 {updates}",
        no_update_string="󰚰 0",
        update_interval=3600,
        colour_have_updates=theme["background"], # Invertido
        colour_no_updates=theme["background"],
    )


def widgetNet(is_pill=True):
    """Widget de red con intervalo optimizado"""
    style = __pill_base("network") if is_pill else __base("network")
    return widget.Net(
        **style,
        interface=get_network_interface(),
        format="{down} ↓↑ {up}",
        update_interval=2,
    )


def widgetWlan(is_pill=True):
    """Widget WiFi con intervalo optimizado"""
    style = __pill_base("network") if is_pill else __base("network")
    return widget.Wlan(
        **style,
        interface=get_network_interface(),
        format="{essid} {percent:.0%}",
        disconnected_message="Disconnected",
        update_interval=5,
        max_chars=12,
    )


def widgetInternetStatus(is_pill=True):
    """Widget de estado de internet con integración de colores del tema"""
    style = __pill_base("network") if is_pill else __base("status")
    return InternetStatus(
        **style,
        label_connected="Online",
        label_disconnected="Offline",
        color_connected=theme["background"], # Invertido porque está en píldora
        color_disconnected=theme["red"],
        update_interval=10,
        fontsize=text_size - 2,
    )


def widgetWlanSup(is_pill=True):
    """Widget WiFi mejorado con detección inteligente"""
    interface = get_network_interface()
    style = __pill_base("network") if is_pill else __base("network")
    # Solo usar Wlan si es una interfaz inalámbrica
    if any(x in interface for x in ["wlan", "wlp", "wifi"]):
        return widget.Wlan(
            **style,
            interface=interface,
            format="{percent:.0%}",
            disconnected_message="X",
            update_interval=5,
            max_chars=12,
        )
    else:
        return widget.TextBox(**style, text="ETH", padding=5)


def widgetMemory(is_pill=True):
    """Widget de memoria con formato optimizado"""
    style = __pill_base("system") if is_pill else __base("system")
    return widget.Memory(
        **style,
        format="{MemUsed: .1f}G",
        measure_mem="G",
        update_interval=3,
    )


def widgetCpu(is_pill=True):
    """Widget de CPU con intervalo optimizado"""
    style = __pill_base("system") if is_pill else __base("system")
    return widget.CPU(
        **style,
        format="{load_percent}%",
        update_interval=2,
    )


def widgetDisk(is_pill=True):
    """Widget de disco con formato mejorado"""
    style = __pill_base("system") if is_pill else __base("system")
    return widget.HDD(
        **style,
        format="{HDDPercent}%",
        update_interval=300,
        device=disk_device,
    )


def widgetBattery(is_pill=True):
    """Widget de batería con formato mejorado"""
    style = __pill_base("status") if is_pill else __base("status")
    return widget.Battery(
        **style,
        format="{char} {percent:.0%}",
        charge_char="󱘖",
        discharge_char="",
        empty_char="󱚢",
        full_char="󱇇",
        update_interval=10,
    )


def widgetClock(is_pill=True):
    """Widget de reloj con mejor diseño"""
    style = __pill_base("info") if is_pill else __base("info")
    return widget.Clock(
        **style,
        format="%H:%M",
        mouse_callbacks={"Button1": lazy.spawn("zenity --calendar")},
    )


def widgetSystray():
    """Widget de system tray"""
    return widget.Systray(
        **__base("info"),
        padding=5,
    )


def widgetKeyboardLayout(is_pill=True):
    """Widget de layout de teclado"""
    style = __pill_base("info") if is_pill else __base("info")
    # Crear display_map dinámico basado en layouts configurados
    display_map = {}
    for layout in keyboard_layouts:
        layout = layout.strip()
        if layout == "latam":
            display_map[layout] = "LA"
        elif layout == "es":
            display_map[layout] = "ES"
        else:
            display_map[layout] = layout.upper()

    return widget.KeyboardLayout(
        **style,
        configured_keyboards=[k.strip() for k in keyboard_layouts],
        display_map=display_map,
    )


def widgetVolume(is_pill=True):
    """Widget de volumen con mejor diseño"""
    style = __pill_base("media") if is_pill else __base("media")
    return widget.PulseVolume(
        **style,
        limit_max_volume=True,
        update_interval=0.5,
    )


def widgetBacklight(is_pill=True):
    """Widget de brillo con mejor diseño"""
    style = __pill_base("media") if is_pill else __base("media")
    return widget.Backlight(
        **style,
        backlight_name=backlight_name,
        fmt="󰃠 {}",
        mouse_callbacks={
            "Button4": lazy.spawn("brightnessctl set +5%"),
            "Button5": lazy.spawn("brightnessctl set 5%-"),
        },
        update_interval=1,
    )


def widgetCurrentLayout():
    """Widget de layout actual"""
    return widget.CurrentLayout(
        **__base("info"),
        fmt="󰄯 {}",
    )


def widgetCurrentLayoutIcon():
    """Widget de icono de layout actual"""
    return widget.CurrentLayout(
        **__base("info"),
        mode="icon",
        scale=0.7,
    )


def widgetPomodoro():
    """Widget Pomodoro"""
    return widget.Pomodoro(
        **__base("status"),
    )


def widgetImap():
    """Widget de email con intervalo optimizado"""
    # Solo mostrar widget si hay configuración de email
    if not email_user or not email_server:
        return widget.TextBox(**__base("status"), text="", padding=0)

    return widget.ImapWidget(
        **__base("status"),
        user=email_user,
        server=email_server,
        password=keyring.get_password(email_keyring_service, email_user),
        mbox=f'"{email_mbox}"',
        label="📧 ",
        hide_no_unseen=True,
        update_interval=60,  # Aumentado de 2s a 60s para mejor performance
        fmt="<b>{}</b>",
        mouse_callbacks={
            "Button1": lazy.spawn(email_client),
        },
    )


def widgetBluetooth(is_pill=True):
    """Widget Bluetooth con mejor diseño"""
    style = __pill_base("media") if is_pill else __base("media")
    return widget.Bluetooth(
        **style,
        default_text="{connected_devices}",
        default_show_battery=True,
        update_interval=10,
        mouse_callbacks={
            "Button1": lazy.spawn("blueman-manager"),
        },
    )


primary_widgets = [
    # Izquierda: Grupos y Ventana
    widget.Spacer(length=5, background=theme["background"]),
    widgetGrupBox(),
    __separator(),
    widgetWindowName(),
    widgetPrompt(),

    widget.Spacer(length=bar.STRETCH, background=theme["background"]),
    
    # Derecha: Cápsulas de información
    # Red
    __pill_open("network"),
    __icon("󰀂", "network", is_pill=True),
    widgetInternetStatus(),
    widget.TextBox(text=" ", **__pill_base("network")),
    __icon("󰛵", "network", is_pill=True),
    widgetWlanSup(),
    __pill_close("network"),
    
    widget.Spacer(length=3, background=theme["background"]),
    
    # Sistema (CPU + Mem)
    __pill_open("system"),
    __icon("", "system", is_pill=True),
    widgetCpu(),
    widget.TextBox(text=" ", **__pill_base("system")),
    __icon("󰪏", "system", is_pill=True),
    widgetMemory(),
    __pill_close("system"),
    
    widget.Spacer(length=5, background=theme["background"]),
    
    # Media (Volumen + Brillo)
    __pill_open("media"),
    __icon("󰕾", "media", is_pill=True),
    widgetVolume(),
    widget.TextBox(text=" ", **__pill_base("media")),
    widgetBacklight(),
    __pill_close("media"),
    
    widget.Spacer(length=5, background=theme["background"]),
    
    # Estado (Batería + Updates)
    __pill_open("status"),
    widgetBattery(),
    widget.TextBox(text=" ", **__pill_base("status")),
    widgetCheckUpdates(),
    __pill_close("status"),
    
    widget.Spacer(length=5, background=theme["background"]),
    
    # Reloj y Teclado
    __pill_open("info"),
    __icon("󰔠", "info", is_pill=True),
    widgetClock(),
    widget.TextBox(text=" ", **__pill_base("info")),
    widgetKeyboardLayout(),
    __pill_close("info"),
    
    widget.Spacer(length=5, background=theme["background"]),
    widgetSystray(),
    widget.Spacer(length=5, background=theme["background"]),
    widgetCurrentLayoutIcon(),
    widget.Spacer(length=5, background=theme["background"]),
]

secondary_widgets = [
    widget.Spacer(length=5),
    widgetGrupBox(),
    __separator(),
    widgetWindowName(),
    
    widget.Spacer(length=bar.STRETCH),
    
    __pill_open("system"),
    __icon("", "system", is_pill=True),
    widgetCpu(),
    __pill_close("system"),
    
    widget.Spacer(length=5),
    
    __pill_open("info"),
    widgetClock(),
    __pill_close("info"),
    
    widget.Spacer(length=5),
]
