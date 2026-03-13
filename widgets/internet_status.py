# ~/.config/qtile/widgets/internet_status.py
# -*- coding: utf-8 -*-

import socket
from libqtile.widget import base

class InternetStatus(base.BackgroundPoll):
    """
    Widget que verifica conectividad real a Internet.
    Permite personalizar iconos, texto y colores dinámicamente.
    """

    defaults = [
        ("update_interval", 10, "Tiempo entre chequeos (segundos)"),
        ("hosts", [("1.1.1.1", 53), ("8.8.8.8", 53), ("google.com", 80)], "Hosts a verificar"),
        ("timeout", 2, "Timeout de conexión (segundos)"),
        ("label_connected", "󰀂 Online", "Texto cuando hay conexión"),
        ("label_disconnected", "󰀂 Offline", "Texto cuando no hay conexión"),
        ("color_connected", None, "Color (hex) cuando hay conexión"),
        ("color_disconnected", None, "Color (hex) cuando no hay conexión"),
    ]

    def __init__(self, **config):
        base.BackgroundPoll.__init__(self, "", **config)
        self.add_defaults(InternetStatus.defaults)
        
        # Habilitar markup si se especifican colores
        if self.color_connected or self.color_disconnected:
            self.markup = True

    def check_internet(self) -> bool:
        """Verifica la conexión intentando conectar a una lista de hosts."""
        for host, port in self.hosts:
            try:
                # Usar el timeout directamente en create_connection es más limpio y seguro
                sock = socket.create_connection((host, port), timeout=self.timeout)
                sock.close()
                return True
            except (OSError, socket.timeout):
                continue
        return False

    def poll(self) -> str:
        """Actualiza el contenido del widget."""
        is_connected = self.check_internet()
        
        text = self.label_connected if is_connected else self.label_disconnected
        color = self.color_connected if is_connected else self.color_disconnected
        
        if color:
            return f'<span foreground="{color}">{text}</span>'
        
        return text
