#!/bin/sh

# Get the current working directory
current_dir=$(pwd)

# Copy the syslog file to the current directory
cp /var/log/syslog $current_dir

# Change the date and time of the file
date -s "$(date +%Y-%m-%d-%H:%M:%S)" $current_dir/syslog

# Check if the copy was successful
if [ -f $current_dir/syslog ]; then
echo "Successfully copied syslog file to $current_dir/syslog"
else
echo "Error: Could not copy syslog file to $current_dir/syslog"
fi

