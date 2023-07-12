#!/bin/bash

# Get the current time
timestamp=$(date +"%Y%m%d%H%M%S")

# Get the size of the original log files
syslog_size=$(stat -c%s /var/log/syslog)
wtmp_size=$(stat -c%s /var/log/wtmp)

# Compress the log files
gzip -c /var/log/syslog > /var/log/backups/syslog-$timestamp.gz
gzip -c /var/log/wtmp > /var/log/backups/wtmp-$timestamp.gz

# Clear the contents of the log files
echo "" > /var/log/syslog
echo "" > /var/log/wtmp

# Get the size of the compressed log files
syslog_compressed_size=$(stat -c%s /var/log/backups/syslog-$timestamp.gz)
wtmp_compressed_size=$(stat -c%s /var/log/backups/wtmp-$timestamp.gz)

# Compare the sizes of the original and compressed log files
echo "Original syslog file size: $syslog_size"
echo "Compressed syslog file size: $syslog_compressed_size"
echo "Original wtmp file size: $wtmp_size"
echo "Compressed wtmp file size: $wtmp_compressed_size"
