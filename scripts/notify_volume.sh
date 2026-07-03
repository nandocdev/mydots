#!/bin/bash

# notify_volume.sh
# Uso: ./notify_volume.sh [up|down|mute]

function get_volume {
    pactl get-sink-volume @DEFAULT_SINK@ | grep -Po '[0-9]+(?=%)' | head -n 1
}

function is_mute {
    pactl get-sink-mute @DEFAULT_SINK@ | grep -q "yes"
}

case $1 in
    up)
        pactl set-sink-mute @DEFAULT_SINK@ false
        pactl set-sink-volume @DEFAULT_SINK@ +5%
        ;;
    down)
        pactl set-sink-mute @DEFAULT_SINK@ false
        pactl set-sink-volume @DEFAULT_SINK@ -5%
        ;;
    mute)
        pactl set-sink-mute @DEFAULT_SINK@ toggle
        ;;
esac

VOLUME=$(get_volume)

if is_mute ; then
    notify-send -a "Sistema" -u low -r 9993 -i audio-volume-muted "Silenciado"
else
    # Crear una barra de progreso simple con caracteres
    BAR=$(seq -s "─" $(($VOLUME / 5)) | sed 's/[0-9]//g')
    notify-send -a "Sistema" -u low -r 9993 -i audio-volume-high "Volumen: $VOLUME%" "$BAR"
fi
