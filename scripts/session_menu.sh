#!/bin/bash

# A rofi-based session menu.

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
        light-locker-command -l
        ;;
    "Logout")
        qtile cmd-obj -o cmd -f shutdown
        ;;
esac
