#!/bin/bash

THRESHOLD=80

check_memory() {

    TOTAL_MEMORY=$(free | awk '/^Mem:/{print $2}')
    AVAILABLE_MEMORY=$(free | awk '/^Mem:/{print $4}')

    MEMORY_USAGE_PERCENT=$((100 * (TOTAL_MEMORY - AVAILABLE_MEMORY) / TOTAL_MEMORY))

    echo "Memory usage: $MEMORY_USAGE_PERCENT%"

    if [ $MEMORY_USAGE_PERCENT -gt $THRESHOLD ]; then
        echo "Memory usage exceeds threshold. Clearing cache..."
        sync; echo 1 > /proc/sys/vm/drop_caches
        echo "Cache cleared."
    else
        echo "Memory usage is within threshold."
    fi
}

while true; do
    check_memory
    sleep 10  
done

