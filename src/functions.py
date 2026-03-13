import psutil
import time

# Cache para la interfaz de red (mejora performance)
_network_interface_cache = None
_last_check_time = 0
_cache_timeout = 300  # 5 minutos


def get_network_interface():
    """Obtiene la interfaz de red activa usando psutil con cache"""
    global _network_interface_cache, _last_check_time
    
    current_time = time.time()
    
    # Si hay cache válido y no ha expirado, retornarlo
    if _network_interface_cache is not None and (current_time - _last_check_time) < _cache_timeout:
        return _network_interface_cache
    
    _last_check_time = current_time
    
    try:
        # Obtener estadísticas de red
        net_stats = psutil.net_io_counters(pernic=True)
        # Buscar interfaz con tráfico (excluyendo loopback)
        for interface, stats in net_stats.items():
            if interface != "lo" and (stats.bytes_sent > 0 or stats.bytes_recv > 0):
                _network_interface_cache = interface
                return interface
        # Si no hay tráfico, buscar la primera interfaz que no sea loopback
        for interface in net_stats.keys():
            if interface != "lo":
                _network_interface_cache = interface
                return interface
    except Exception as e:
        print(f"Error detecting network interface: {e}")
    
    # Fallback
    _network_interface_cache = "lo"
    return "lo"


def clear_network_cache():
    """Limpia el cache de interfaz de red (útil si cambias de conexión)"""
    global _network_interface_cache
    _network_interface_cache = None
