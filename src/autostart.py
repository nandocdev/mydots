#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: autostart.py
Description: Configuration file for Qtile window manager.
Author: Your Name
Date: YYYY-MM-DD
"""
import subprocess
import os
from src.config import wallpapers, get_env

def run_cmd(cmd, shell=True, check=False):
    """Ejecuta comando de forma no bloqueante para mejor performance"""
    try:
        subprocess.Popen(
            cmd,
            shell=shell,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )
    except Exception as e:
        print(f"Error running command '{cmd}': {e}")


# Configuración de comandos de inicio desde .env o valores por defecto
wallpapers_path = wallpapers
picom_backend = get_env('PICOM_BACKEND', '--experimental-backends')
xrandr_command = get_env('XRANDR_COMMAND', '')

# Lista de comandos de inicio
autoinit = [
    f"feh --bg-fill --randomize {wallpapers_path}/*",
    f"picom {picom_backend} --config /dev/null",
]

# Agregar comando xrandr si está configurado
if xrandr_command:
    autoinit.append(xrandr_command)
else:
    # Comando por defecto si no hay configuración
    autoinit.append(
        "xrandr --output eDP-1 --primary --mode 1920x1080 --pos 0x0 --rotate normal "
        "--output HDMI-1 --mode 1920x1080 --pos 1920x0 --rotate normal --output DP-1 --off"
    )

# Ejecutar comandos de forma asíncrona
for cmd in autoinit:
    run_cmd(cmd)

# vim: ft=python
