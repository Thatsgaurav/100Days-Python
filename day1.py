# Day 1 

# print('Day 1 - Python Print Function')
# print("The function is declared like this")
# print("print('what to print')")

# Insert a newline 
print("Hello" + " " + "Gaurav")

#--->>> Day 1 - String Manipulation <<<---
# String Concatenation is done with the "+" sign.
# e.g. print("Hello " + "world")
# New lines can be created with a backslash and n.

print("Day 1" + "-" + "String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world"')
print(("New lines can be created with a backslash and n."))

# input() 
# Then print() with input
print("Hello " + input("What is Your name?"))

# Write a program that prints the number of characters in a user's name. 
# You might need to Google for a function that calculates the length of a string.
print( len(input("What is your name? ") ) )

# Write a program that switches the values stored in the variables a and b.
a = input("a :")
b = input("b :")

a , b = b , a

print("a:" + a)
print("b: " + b)

#1. Create a greeting for your program..
print("Welcome to python")

#2. Ask the user for the city that they grew up in.
city = input("Where are you from :\n")
#3. Ask the user for the name of a pet.
pet = input("What is your pet name :\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your band name is ",  city + pet)
#5. Make sure the input cursor shows on a new line, see the example 