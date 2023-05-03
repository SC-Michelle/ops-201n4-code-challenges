#!/bin/bash

y="5826"

while [$y == "5026"]
do
    ps aux
    echo "Choose a PID"
    read pid
    kill $pid
    break
done

