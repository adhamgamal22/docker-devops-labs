#!/bin/sh
touch /tmp/healthy
echo "Application started successfully..."

counter=0
while true; do
  counter=$((counter+1))
  echo "App running cycle $counter"
  sleep 5
  if [ $counter -eq 6 ]; then
    echo "CRITICAL ERROR: Memory leak detected! Killing process..." >> /dev/stderr
    rm -f /tmp/healthy
    exit 1
  fi
done