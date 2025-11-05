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
    theme, font, text_size, icon_size,
    email_user, email_server, email_mbox, email_keyring_service, email_client,
    backlight_name, disk_device, keyboard_layouts
)
from libqtile import widget
from libqtile.lazy import lazy
from src.functions import get_network_interface
from libqtile.widget import ImapWidget
# from libqtile.widget.bluetooth import Bluetooth
import keyring

# Sistema de colores consistente para mejor diseño
# Mapeo de widgets a colores del tema para consistencia visual
_widget_colors = {
    'default': 'cyan',
    'network': 'bright_cyan',
    'system': 'bright_green',
    'media': 'bright_pink',
    'status': 'bright_yellow',
    'info': 'comment',
}


def __base(color_key='default'):
    """Retorna estilos base con color consistente del tema"""
    color = _widget_colors.get(color_key, 'cyan')
    return {
        "background": theme["background"],
        "foreground": theme[color],
    }


def __inverse():
    return {"background": theme["foreground"], "foreground": theme["background"]}


def __separator():
    """Separador con mejor espaciado visual"""
    return widget.Sep(**__base('info'), linewidth=0, padding=8)


def __icon(icon, color_key='default'):
    """Icono con mejor padding y color consistente"""
    return widget.TextBox(
        text=icon, 
        fontsize=icon_size, 
        padding=2, 
        **__base(color_key)
    )


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
    """Widget de nombre de ventana con mejor diseño"""
    return widget.WindowName(
        font=font,
        fontsize=text_size - 2,
        padding=8,
        foreground=theme["bright_cyan"],
        background=theme["background"],
        parse_text=__textInput,
        max_chars=60,  # Limitar longitud para mejor visualización
    )


def widgetPrompt():
    return widget.Prompt()


def widgetCheckUpdates():
    """Widget de actualizaciones con intervalos optimizados"""
    return widget.CheckUpdates(
        **__base('status'),
        distro="Arch_checkupdates",
        display_format="  {updates}",
        no_update_string="",
        update_interval=3600,  # 1 hora (reducido de 30min para mejor performance)
        colour_have_updates=theme["bright_orange"],
        colour_no_updates=theme["comment"],
    )


def widgetNet():
    """Widget de red con intervalo optimizado"""
    return widget.Net(
        **__base('network'),
        interface=get_network_interface(),
        format="{down} ↓↑ {up}",
        update_interval=2,  # Reducido de default para mejor balance
    )


def widgetWlan():
    """Widget WiFi con intervalo optimizado"""
    return widget.Wlan(
        **__base('network'),
        interface=get_network_interface(),
        format="{essid} {percent:2.0%}",
        disconnected_message="Disconnected",
        update_interval=5,  # Aumentado de 1s a 5s para mejor performance
        max_chars=12,
    )


def widgetWlanSup():
    """Widget WiFi mejorado con detección inteligente"""
    interface = get_network_interface()
    # Solo usar Wlan si es una interfaz inalámbrica
    if any(x in interface for x in ["wlan", "wlp", "wifi"]):
        return widget.Wlan(
            **__base('network'),
            interface=interface,
            format="{essid} {percent:2.0%}",
            disconnected_message="Disconnected",
            update_interval=5,  # Optimizado para mejor performance
            max_chars=12,
        )
    else:
        # Devolver un widget placeholder para interfaces cableadas
        return widget.TextBox(**__base('network'), text="󰈀 Ethernet", padding=5)


def widgetMemory():
    """Widget de memoria con formato optimizado"""
    return widget.Memory(
        **__base('system'),
        format="{MemUsed: .1f}{mm}/{MemTotal: .1f}{mm}",
        measure_mem="G",
        update_interval=3,  # Intervalo optimizado
    )


def widgetCpu():
    """Widget de CPU con intervalo optimizado"""
    return widget.CPU(
        **__base('system'),
        format="{load_percent}%",
        update_interval=2,  # Intervalo explícito para mejor control
    )


def widgetDisk():
    """Widget de disco con formato mejorado"""
    return widget.HDD(
        **__base('system'),
        format="HDD {HDDPercent}%",
        update_interval=300,  # 5 minutos (aumentado para mejor performance)
        device=disk_device,
    )


def widgetBattery():
    """Widget de batería con formato mejorado"""
    return widget.Battery(
        **__base('status'),
        format="{char} {percent:2.0%} {watt:.1f}W",
        charge_char="󱘖 ",
        discharge_char=" ",
        empty_char="󱚢 ",
        full_char="󱇇 ",
        update_interval=10,  # Intervalo optimizado
    )


def widgetClock():
    """Widget de reloj con mejor diseño"""
    return widget.Clock(
        **__base('info'),
        format="%c",
        mouse_callbacks={"Button1": lazy.spawn("zenity --calendar")},
    )


def widgetSystray():
    """Widget de system tray"""
    return widget.Systray(
        **__base('info'),
        padding=5,
    )


def widgetKeyboardLayout():
    """Widget de layout de teclado"""
    # Crear display_map dinámico basado en layouts configurados
    display_map = {}
    for layout in keyboard_layouts:
        layout = layout.strip()
        if layout == "latam":
            display_map[layout] = "󰌓 "
        elif layout == "es":
            display_map[layout] = " "
        else:
            display_map[layout] = f"{layout.upper()} "
    
    return widget.KeyboardLayout(
        **__base('info'),
        configured_keyboards=[k.strip() for k in keyboard_layouts],
        display_map=display_map,
    )


def widgetVolume():
    """Widget de volumen con mejor diseño"""
    return widget.PulseVolume(
        **__base('media'),
        emoji_list=["󰝟 ", "󰕿 ", "󰖀 ", "󰕾 "],
        mouse_callbacks={"Button1": lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")},
        limit_max_volume=True,
        update_interval=0.5,  # Para respuesta rápida en cambios
    )


def widgetBacklight():
    """Widget de brillo con mejor diseño"""
    return widget.Backlight(
        **__base('media'),
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
        **__base('info'),
        fmt="󰄯 {}",
    )


def widgetCurrentLayoutIcon():
    """Widget de icono de layout actual"""
    return widget.CurrentLayout(
        **__base('info'),
        scale=0.7,
    )


def widgetPomodoro():
    """Widget Pomodoro"""
    return widget.Pomodoro(
        **__base('status'),
    )



def widgetImap():
    """Widget de email con intervalo optimizado"""
    # Solo mostrar widget si hay configuración de email
    if not email_user or not email_server:
        return widget.TextBox(**__base('status'), text="", padding=0)
    
    return widget.ImapWidget(
        **__base('status'),
        user=email_user,
        server=email_server,
        password=keyring.get_password(email_keyring_service, email_user),
        mbox=f'"{email_mbox}"',
        label='📧 ',
        hide_no_unseen=True,
        update_interval=60,  # Aumentado de 2s a 60s para mejor performance
        fmt='<b>{}</b>',
        mouse_callbacks={
            'Button1': lazy.spawn(email_client),
        }
    )


def widgetBluetooth():
    """Widget Bluetooth con mejor diseño"""
    return widget.Bluetooth(
        **__base('media'),
        default_text='󰂯 {connected_devices}',
        default_show_battery=True,
        device_battery_format=' ({battery}%)',
        update_interval=10,  # Intervalo optimizado
        mouse_callbacks={
            'Button1': lazy.spawn('blueman-manager'),
        }
    )


primary_widgets = [
    widgetGrupBox(),
    __separator(),
    widgetWindowName(),
    widget.Spacer(length=8),  # Espaciador para mejor distribución
    widgetImap(),
    __separator(),
    widgetCheckUpdates(),
    __separator(),
    __icon("󰛵 ", 'network'),
    widgetWlanSup(),
    widgetNet(),
    __separator(),
    widgetVolume(),
    __separator(),
    widgetBluetooth(),
    __separator(),
    __icon(" ", 'system'),
    widgetCpu(),
    __separator(),
    __icon("󰪏 ", 'system'),
    widgetMemory(),
    __separator(),
    __icon("󰋊 ", 'system'),
    widgetDisk(),
    __separator(),
    widgetBattery(),
    __separator(),
    __icon("󰔠 ", 'info'),
    widgetClock(),
    widgetBacklight(),
    __separator(),
    widgetKeyboardLayout(),
    widgetCurrentLayoutIcon(),
]

secondary_widgets = [
    widgetGrupBox(),
    __separator(),
    widgetWindowName(),
    widget.Spacer(length=8),
    widgetCheckUpdates(),
    __separator(),
    __icon("󰛵 ", 'network'),
    widgetWlan(),
    __separator(),
    __icon(" ", 'system'),
    widgetCpu(),
    __separator(),
    __icon("󰪏 ", 'system'),
    widgetMemory(),
    __separator(),
    __icon("󰋊 ", 'system'),
    widgetDisk(),
    __separator(),
    widgetBattery(),
    __separator(),
    __icon("󰔠 ", 'info'),
    widgetClock(),
    __separator(),
    widgetSystray(),
    widgetKeyboardLayout(),
]
