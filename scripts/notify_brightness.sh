#!/bin/bash

# notify_brightness.sh
# Uso: ./notify_brightness.sh [up|down]

case $1 in
    up)
        brightnessctl set +10%
        ;;
    down)
        brightnessctl set 10%-
        ;;
esac

BRIGHTNESS=$(brightnessctl -m | cut -d, -f4 | tr -d '%')
BAR=$(seq -s "─" $(($BRIGHTNESS / 10)) | sed 's/[0-9]//g')

notify-send -a "Sistema" -u low -r 9994 -i display-brightness "Brillo: $BRIGHTNESS%" "$BAR"
