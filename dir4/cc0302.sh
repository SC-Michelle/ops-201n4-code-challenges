#!/bin/bash

#Copy path to working Directory
current_time=$(date "+%Y.%m.%d-%H.%M.%S")
name=$"syslog$currentdate.log"
cp /var/log/syslog "$name"



