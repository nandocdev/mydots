#!/bin/bash

# A rofi-based session menu.
# El comando de lock se puede configurar en .env con LOCK_COMMAND

# Cargar variables de entorno desde .env si existe
ENV_FILE="$HOME/.config/qtile/.env"
if [ -f "$ENV_FILE" ]; then
    export $(grep -v '^#' "$ENV_FILE" | grep LOCK_COMMAND | xargs)
fi

LOCK_CMD="${LOCK_COMMAND:-light-locker-command -l}"

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
        $LOCK_CMD
        ;;
    "Logout")
        qtile cmd-obj -o cmd -f shutdown
        ;;
esac
