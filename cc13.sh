#!/bin/bash

#Ops Challenge 13
#Author: Michelle Wright

#Main

echo "Type a website"
read website

whois $website > DomainAnalyzer.txt
dig $website >> DomainAnalyzer.txt
hots $website >> DomainAnalyzer.txt
nslookup $website >> DomainAnalyzer.txt

#End