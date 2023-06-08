#!/bin/bash

# Create a menu of options
options=(
    "Hello world"
    "Ping self"
    IP info"
    "Exit"
    "
)

# Loop until the user exits 
    while true; do

        # Print the menu
        echo "Select an option:"
        for option in "${options[@]}"; do
            echo
        done

        # Get the user's input
        read -p "Your choice: " choice

        # Evaluate the user's input
        case "$choice" in
          "Hello world")
            echo "Hello world!"
            ;;
          "Ping self")
            ping 127.0.0.1
            ;;
          "IP info")
            ifconfig
            ;;
          "Exit")
            break
            ;;
          *)
            echo "Invalid choice."
        esac

done         



