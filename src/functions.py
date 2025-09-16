import psutil


def get_network_interface():
    """Obtiene la interfaz de red activa usando psutil"""
    try:
        # Obtener estadísticas de red
        net_stats = psutil.net_io_counters(pernic=True)
        # Buscar interfaz con tráfico (excluyendo loopback)
        for interface, stats in net_stats.items():
            if interface != "lo" and (stats.bytes_sent > 0 or stats.bytes_recv > 0):
                return interface
        # Si no hay tráfico, buscar la primera interfaz que no sea loopback
        for interface in net_stats.keys():
            if interface != "lo":
                return interface
    except Exception as e:
        print(f"Error detecting network interface: {e}")
    return "lo"  # Fallback
