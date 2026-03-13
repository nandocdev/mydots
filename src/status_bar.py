#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: status_bar.py
Description: Definición de la barra de estado de Qtile.
"""

from libqtile import bar
from src.config import bar_size, bar_opacity

def status_bar(widgets):
    """Crea una instancia de la barra con los widgets proporcionados"""
    return bar.Bar(widgets, bar_size, opacity=bar_opacity)
