#!/bin/bash

y="8217"

while [ $y == "8217" ]
do
    ps aux
    echo "Choose a PID"
    read pid
    kill $pid
    break
done

