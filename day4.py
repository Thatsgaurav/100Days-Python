## Heads or Tails

# Instructions

# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails". 

# **Important**, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

# There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

# e.g.
# 1 means Heads
# 0 means Tails 

# Example Output

# ```
# Heads
# ```

# or

# ```
# Tails
# ```

import random

random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")

# -------------------------------------- >>>

# Instructions
# You are going to write a program which will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# Line 8 splits the string names_string into individual names and puts them inside a List 
# called names. For this to work, you must enter all the names as name followed by comma 
# then space. e.g. name, name, name

# Split string method
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

#Write your code below this line 👇

#Get the total number of items in list.
num_items = len(names)
#Generate random numbers between 0 and the last index. 
random_choice = random.randint(0, num_items - 1)
#Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")

# --------------------------------------------------------------------- >>>>

# Instructions
# You are going to write a program which will mark a spot with an X.

# In the starting code, you will find a variable called map.

# This map contains a nested list.
# When map is printed this is what the nested list looks like:

# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
# In the starting code, we have used new lines (\n) to format the three rows into a square, like this:

# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']


row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("What do you want to put the trasure? ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "x"

print("{row1}\n{row2}\n{row3}")