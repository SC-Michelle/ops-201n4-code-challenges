#!/bin/bash

#Copy path to working directory
currentdate=$(date "+%m-%d-%Y-%H.%M.%S")
name=$"syslog$currentdate.log"
cp /var/log/syslog "$name"



