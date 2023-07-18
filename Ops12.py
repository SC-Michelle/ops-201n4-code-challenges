# Your challenge tonight is to write a basic adventure game using some of the  
#code provided below and using if/elif statements

yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
 
# Introduction
name = input("What is your name, adventurer?\n")
print("Greetings, " + name + ". Let us go on a quest!")
print("You find yourself on the edge of a dark forest.")
print("Can you find your way through?\n")
 
# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to step into the forest?\nyes/no\n")
    if response == "yes":
        print("You head into the forest. You hear crows cawwing in the distance.\n")
    elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
 
# Part 2
response = ""
while response not in yes_no:
    response = input("Would you like to continue exploring?\nyes/no\n")
    if response == "yes":
        print("You see a dim light flickering in the distance. Something is pulling you towards that direction\n")
    elif response == "no":
        print("Don't be a baby! Only way out is in.")
    else: 
        print("I didn't understand that.\n")

# Part 3
response = ""
while response not in yes_no:
    response = input("Would you like to turn around?\nyes/no\n")
    if response == "yes":
        print("You trip on a branch and go unconscious\n Goodbye, " + name + ".")
        quit()
    elif response == "no":
        print("You come up to a dwindling campfire with no people, but you see a few trails leading in different directions" )
    else: 
        print("I didn't understand that.\n")


# Part 4
response = ""
while response not in directions:
    response = input("What direction would you like to go?\nleft/right\forward/n")
    if response == "left":
        print("You run into a Zombie and he eats your brains\n Goodbye, " + name + ".")
        quit()
    elif response == "right":
        print("You walk until you hit the beach where you see a raft caught on the shore" )
    else: 
        print("I didn't understand that.\n")

# Final Part
response = ""
while response not in yes_no:
    response = input("Would you like to use the raft?\nyes/no\n")
    if response == "yes":
        print("The raft seems structural and has a paddle. You use it to escape the island. After a few hours drifting on the raft a passing cruise ship rescues you" )
    elif response == "no":
        print("A wave comes and washes the raft away. You're now stranded forever...with whatever else that roams the island\n I hope you're a fast runner, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
