#!/usr/bin/env bash

# This script monitors CPU usage and restarts the Laravel service
# if usage exceeds the specified THRESHOLD (default 80%).

THRESHOLD=80
SERVICE_NAME="laravel-app"

while true; do
  # Using 'top' in batch mode to capture CPU usage
  CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
  CPU_USAGE_INT=${CPU_USAGE%.*}

  if [ "$CPU_USAGE_INT" -gt "$THRESHOLD" ]; then
    echo "[Alert] CPU usage is ${CPU_USAGE_INT}%. Restarting ${SERVICE_NAME}..."
    sudo systemctl restart "${SERVICE_NAME}"
  else
    echo "CPU usage is ${CPU_USAGE_INT}%, within normal limits."
  fi

  sleep 30
done