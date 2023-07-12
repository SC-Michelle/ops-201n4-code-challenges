#Script: Ops 301 Class Ops Challenge 
#Author: Michelle Wright
#Date of last revision: 07/12/2023
#Purpose: FizzBuzz

#Main

n= 100
for n in range(1, n+1):
    message = ''
    if not n % 3:
        message = 'fizz'
    if not n % 5:
        message += 'buzz'
    print(message or n)
# Python program to implement the FizzBuzz problem
for i in range(1, 101):
    # Numbers that are divisible by 3 and 5
    # are always divisible by 15
    # Therefore, "FizzBuzz" is printed in place of that number
    if (i%15 == 0):
        print("FizzBuzz", end=" ")
    # "Fizz" is printed in place of numbers
    # that are divisible by 3
    elif (i%3 == 0):
        print("Fizz", end=" ")
    # "Buzz" is printed in place of numbers
    # that are divisible by 5
    elif(i%5 == 0):
        print("Buzz", end=" ")
    # If none of the above conditions are satisfied,
    # the number is printed
    else:
        print(i, end=" ")
