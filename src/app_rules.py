#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: app_rules.py
Description: Reglas para asignar aplicaciones a grupos específicos
Author: Your Name
Date: YYYY-MM-DD
"""

from libqtile.config import Match
from libqtile import hook


# Reglas de aplicaciones: diccionario {wm_class: grupo}
# wm_class puede ser el nombre de la clase o una expresión regular
# Para encontrar el wm_class de una aplicación:
#   xprop WM_CLASS
#   o usar: qtile cmd-obj -o window -f info

app_rules = {
    # Navegadores - Grupo 2
    'brave': '2',  # Brave Browser
    'Brave-browser': '2',
    'firefox': '2',
    'Firefox': '2',
    'chromium': '2',
    'google-chrome': '2',
    
    # Editores de código - Grupo 3
    'subl': '3',  # Sublime Text
    'Sublime_text': '3',
    'code': '3',  # VS Code
    'Code': '3',
    'vim': '3',
    'gvim': '3',
    'neovim': '3',
    
    # Terminales - Grupo 1 (o el grupo que prefieras)
    'kitty': '1',
    'Kitty': '1',
    'alacritty': '1',
    'urxvt': '1',
    'xterm': '1',
    
    # Gestores de archivos - Grupo 4
    'thunar': '4',
    'Thunar': '4',
    'nautilus': '4',
    'dolphin': '4',
    'pcmanfm': '4',
    
    # Multimedia - Grupo 5
    'vlc': '5',
    'Vlc': '5',
    'mpv': '5',
    'spotify': '5',
    'Spotify': '5',
    
    # Office - Grupo 6
    'libreoffice': '6',
    'soffice': '6',  # LibreOffice
    'writer': '6',
    'calc': '6',
    'impress': '6',
    
    # Email - Grupo 7
    'evolution': '7',
    'Evolution': '7',
    'thunderbird': '7',
    'Thunderbird': '7',
    
    # Chat/Comunicación - Grupo 8
    'discord': '8',
    'Discord': '8',
    'telegram': '8',
    'TelegramDesktop': '8',
    'slack': '8',
    
    # Otros - Grupo 9
    # Agrega más aplicaciones según necesites
}


def get_group_for_app(wm_class):
    """
    Obtiene el grupo asignado para una aplicación basado en su wm_class
    """
    if not wm_class:
        return None
    
    # Buscar coincidencia exacta
    if wm_class in app_rules:
        return app_rules[wm_class]
    
    # Buscar coincidencia parcial (para casos como "sublime_text" vs "Sublime_text")
    wm_class_lower = wm_class.lower()
    for key, group in app_rules.items():
        if key.lower() in wm_class_lower or wm_class_lower in key.lower():
            return group
    
    return None


@hook.subscribe.client_new
def assign_app_to_group(window):
    """
    Hook que se ejecuta cuando se abre una nueva ventana
    Asigna la aplicación a un grupo específico si hay una regla definida
    """
    try:
        wm_class = window.window.get_wm_class()
        
        if not wm_class:
            return
        
        # wm_class puede ser una lista o un string
        if isinstance(wm_class, list):
            wm_class = wm_class[0] if wm_class else None
        
        if not wm_class:
            return
        
        # Obtener el grupo asignado (número como string: '1', '2', etc.)
        group_index = get_group_for_app(wm_class)
        
        if group_index:
            try:
                # Convertir el índice a número
                group_num = int(group_index)
                
                # Obtener todos los grupos (excluyendo scratchpad)
                groups = window.qtile.groups
                group_list = [g for g in groups.values() if g.name != 'scratchpad']
                
                # Verificar que el índice sea válido (1-9)
                if 1 <= group_num <= len(group_list):
                    # Obtener el grupo correspondiente (índice 0-based)
                    target_group = group_list[group_num - 1]
                    
                    # Mover la ventana al grupo y cambiar a ese grupo
                    window.togroup(target_group.name)
                    target_group.toscreen()
            except (ValueError, IndexError, AttributeError) as e:
                # Silenciar errores para no interrumpir el flujo
                pass
    except Exception:
        # Silenciar cualquier error para no interrumpir el flujo
        pass

