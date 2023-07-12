#!/bin/bash

#Script: Ops 301 Class 06 Ops Challenge solution
#Author: Michelle Wright
#Date of last revision: 07/11/2023
#Purpose: Create a bash script that launches a menu system

#Main

import os

# Execute bash commands

whoami_output = os.popen("whoami").read()
ip_output = os.popen("ip a").read()
lshw_output = os.popen("lshw -short").read()

# Print the results

print("Current user:", whoami_output)
print("IP information:\n", ip_output)
print("Hardware information:\n", lshw_output)
