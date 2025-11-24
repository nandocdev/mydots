#!/bin/bash

# A rofi-based session menu.
# El comando de lock se puede configurar en .env con LOCK_COMMAND

# Cargar variables de entorno desde .env si existe
ENV_FILE="$HOME/.config/qtile/.env"
if [ -f "$ENV_FILE" ]; then
    # Cargar LOCK_COMMAND de forma segura
    LOCK_COMMAND=$(grep -v '^#' "$ENV_FILE" | grep "^LOCK_COMMAND=" | cut -d'=' -f2- | tr -d '"' | tr -d "'")
fi

# Función para bloquear pantalla con múltiples opciones
lock_screen() {
    # Si hay un comando configurado en .env, usarlo
    # if [ -n "$LOCK_COMMAND" ]; then
    #     # Si es light-locker, asegurarse de que el servicio esté activo
    #     if echo "$LOCK_COMMAND" | grep -q "light-locker"; then
    #         # Iniciar el servicio si no está activo
    #         if ! systemctl --user is-active --quiet light-locker 2>/dev/null; then
    #             systemctl --user start light-locker 2>/dev/null
    #             sleep 1  # Dar tiempo para que inicie
    #         fi
    #     fi
    #     eval "$LOCK_COMMAND"
    #     return $?
    # fi
    
    # Intentar diferentes métodos de bloqueo en orden de preferencia
    if command -v light-locker-command >/dev/null 2>&1; then
        # Asegurarse de que light-locker esté activo
        # if ! systemctl --user is-active --quiet light-locker 2>/dev/null; then
        #     systemctl --user start light-locker 2>/dev/null
        #     sleep 1
        # fi
        light-locker-command -l
    fi
    
    if command -v i3lock >/dev/null 2>&1; then
        i3lock && return 0
    fi
    
    if command -v slock >/dev/null 2>&1; then
        slock && return 0
    fi
    
    if command -v xlock >/dev/null 2>&1; then
        xlock && return 0
    fi
    
    if command -v xscreensaver-command >/dev/null 2>&1; then
        xscreensaver-command -lock && return 0
    fi
    
    # Fallback: usar xset para desactivar pantalla (menos seguro)
    if command -v xset >/dev/null 2>&1; then
        xset dpms force off
        return 0
    fi
    
    # Si nada funciona, mostrar error
    notify-send "Error" "No se encontró ningún método de bloqueo disponible" 2>/dev/null || \
    echo "Error: No se encontró ningún método de bloqueo disponible" >&2
    return 1
}

options="Shutdown\nReboot\nLock\nLogout"

selected_option=$(echo -e "$options" | rofi -dmenu -p "Session")

case "$selected_option" in
    "Shutdown")
        systemctl poweroff
        ;;
    "Reboot")
        systemctl reboot
        ;;
    "Lock")
        lock_screen
        ;;
    "Logout")
        qtile cmd-obj -o cmd -f shutdown
        ;;
esac
