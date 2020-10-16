#!/bin/bash

pin=12
threshold=43

echo "Setting up the fan at pin $pin"
gpio -g mode $pin output

while true; do
    tempdata=$(vcgencmd measure_temp | egrep -o '[0-9]*\.[0-9]*')
    temp=${tempdata%.*}
    state=$(gpio -g read $pin)

    if (( $temp > $threshold )) && (( $state != 1 ))
    then
        echo "| $(date +"%d/%m/%y %T") | Turning on the fan."
        gpio -g write $pin 1
    elif (( $state != 0 )) && (( $temp <= $threshold ))
    then
        echo "| $(date +"%d/%m/%y %T") | Turning off the fan."
        gpio -g write $pin 0
    fi
    sleep 5
done