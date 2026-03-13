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
from src.config import wallpapers, get_env, qtile_config_path

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
picom_backend = get_env('PICOM_BACKEND', '')
picom_config = os.path.join(qtile_config_path, "src", "custom", "picom.conf")
xrandr_command = get_env('XRANDR_COMMAND', '')

# Lista de comandos de inicio
autoinit = [
    f"feh --bg-fill --randomize {wallpapers_path}/*",
]

# Agregar picom con configuración si existe
if os.path.exists(picom_config):
    autoinit.append(f"picom --config {picom_config} {picom_backend}")
else:
    autoinit.append(f"picom {picom_backend or '--experimental-backends'} --config /dev/null")

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
