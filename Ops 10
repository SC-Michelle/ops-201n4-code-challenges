# Create a Python script that performs the following:

# Prompt the user to type a string input as the variable for your destination URL.
# Prompt the user to select a HTTP Method of the following options:
# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS


# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.

# Using the requests library, perform a GET request against your lab web server.

# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.

# For the given URL, print response header information to the screen.
from urllib import response
import requests
b = input("Get, Post, Put, Delete , Head, Patch, Options:")

if b == "Get":
    responce = requests.get('https://https://github.com/SC-Michelle/ops-201n4-code-challenges.git')
elif b == "Post":
    response = requests.post('https://https://github.com/SC-Michelle/ops-201n4-code-challenges.git')
elif b == "Put":
    response = requests.put('https://https://github.com/SC-Michelle/ops-201n4-code-challenges.git')
elif b == "Delete":
    response = requests.delete('https://https://github.com/SC-Michelle/ops-201n4-code-challenges.git')
elif b == "Head":
    response = requests.head('https://https://github.com/SC-Michelle/ops-201n4-code-challenges.git')
elif b == "Patch":
    response = requests.patch('https://https://github.com/SC-Michelle/ops-201n4-code-challenges.git')
elif b == "Options":
    response = requests.options('https://https://github.com/SC-Michelle/ops-201n4-code-challenges.git')
else:
    print("input error")
    quit()
answer = input("Enter yes or no:")
if answer =="yes":
    print(response)
else:
    print("cancelling")

#End  
