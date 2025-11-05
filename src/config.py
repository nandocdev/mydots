#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: config.py
Description: Configuration file for Qtile window manager.
Author: Your Name
Date: YYYY-MM-DD
"""

import os
from datetime import datetime
from src.colors import colors
import random

# variables privadas
__datetime = datetime.now().strftime("%Y%m%d%I%M%S%f")
__home = os.path.expanduser("~")
__screenshots = os.path.join(__home, "Screenshots")
__config_dir = os.path.join(__home, ".config", "qtile")
__env_file = os.path.join(__config_dir, ".env")


def load_env():
    """Carga variables de entorno desde archivo .env"""
    env_vars = {}
    
    if not os.path.exists(__env_file):
        return env_vars
    
    try:
        with open(__env_file, 'r') as f:
            for line in f:
                line = line.strip()
                # Ignorar comentarios y líneas vacías
                if not line or line.startswith('#'):
                    continue
                
                # Separar clave y valor
                if '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip()
                    
                    # Expandir ~ en rutas
                    if value.startswith('~/'):
                        value = os.path.expanduser(value)
                    
                    env_vars[key] = value
    except Exception as e:
        print(f"Error loading .env file: {e}")
    
    return env_vars


# Cargar variables de entorno
_env = load_env()


def get_env(key, default=None):
    """Obtiene una variable de entorno del archivo .env o del sistema"""
    # Primero intentar desde .env
    if key in _env:
        return _env[key]
    # Luego desde variables de entorno del sistema
    return os.getenv(key, default)


def get_screenshot_path():
    """Obtiene la ruta para screenshots"""
    screenshots_path = get_env('SCREENSHOTS_PATH', __screenshots)
    screenshots_path = os.path.expanduser(screenshots_path)
    
    # Crear directorio si no existe
    if not os.path.exists(screenshots_path):
        os.makedirs(screenshots_path, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d%I%M%S%f")
    return os.path.join(screenshots_path, f"Screenshot-{timestamp}.png")


# Variables
mod = "mod4"
mod_aux = "control"
font = "Hack Nerd Font"
text_size = 16
icon_size = 16
bar_size = 24
bar_opacity = 0.9

# Aplicaciones (desde .env o valores por defecto)
terminal = get_env('TERMINAL', 'kitty')
browser = get_env('BROWSER', 'brave')
file_manager = get_env('FILE_MANAGER', 'thunar')
editor = get_env('EDITOR', 'vim')
email_client = get_env('EMAIL_CLIENT', 'evolution')

# Rutas
wallpapers = get_env('WALLPAPERS_PATH', '/usr/share/backgrounds/phast')
wallpapers = os.path.expanduser(wallpapers)
if not os.path.exists(wallpapers):
    wallpapers = os.path.expanduser("~/.backgrounds")
    if not os.path.exists(wallpapers):
        os.makedirs(wallpapers, exist_ok=True)

# Configuración de hardware
backlight_name = get_env('BACKLIGHT_NAME', 'amdgpu_bl1')
disk_device = get_env('DISK_DEVICE', 'nvme0n1')
network_interface = get_env('NETWORK_INTERFACE', '')

# Configuración de email (desde .env)
email_user = get_env('EMAIL_USER', '')
email_server = get_env('EMAIL_SERVER', '')
email_mbox = get_env('EMAIL_MBOX', 'INBOX')
email_keyring_service = get_env('EMAIL_KEYRING_SERVICE', email_server)

# Configuración de teclado
keyboard_layouts = get_env('KEYBOARD_LAYOUTS', 'latam,es').split(',')

# Configuración de sesión
lock_command = get_env('LOCK_COMMAND', 'light-locker-command -l')

# Ruta de configuración de Qtile
qtile_config_path = get_env('QTILE_CONFIG_PATH', __config_dir)
# tema por defecto: [gruvbox, dracula, nord, solarized-dark, one-dark, ayu-dark, catppuccin, tokyo-night]
themes = list(colors.keys())

# Sistema de tema persistente: guarda preferencia en archivo
_theme_file = os.path.join(__home, ".config", "qtile", ".theme")
_use_random_theme = get_env('USE_RANDOM_THEME', 'false').lower() == 'true'

def get_theme():
    """Obtiene el tema, preferentemente desde archivo, .env o aleatorio"""
    # Primero intentar desde .env
    default_theme = get_env('DEFAULT_THEME', 'catppuccin')
    
    if _use_random_theme:
        return colors[random.choice(themes)]
    
    # Intentar leer tema guardado en archivo
    try:
        if os.path.exists(_theme_file):
            with open(_theme_file, 'r') as f:
                saved_theme = f.read().strip()
                if saved_theme in colors:
                    return colors[saved_theme]
    except Exception:
        pass
    
    # Usar tema desde .env o default
    if default_theme in colors:
        return colors[default_theme]
    
    # Fallback a catppuccin
    return colors['catppuccin']

theme = get_theme()
screenshot = get_screenshot_path()
