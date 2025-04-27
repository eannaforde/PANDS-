#Bank.py
#This program will prompt the user to read in two money amounts
#Add the two amounts
#Print the answer in a human readable format
 
#Ask user for the first amount in cents 
#use input() function and wrap it with int() to convert the input string to an integer
#reference: https://www.w3schools.com/python/ref_func_input.asp

amount1 = int(input("Enter amount1 in cents"))
#Ask user for the second amount in cents
amount2 = int(input("Enter amount2 in cents"))

#Add the two amounts together
total_cents = amount1 + amount2

#Convert the total amount to euros and cents
#use // to get whole euros, % to get the leftover cents
#reference: https://www.w3schools.com/python/python_operators.asp

euros = total_cents // 100
cents = total_cents % 100

#print the total in euro format with two decimal digits for cents
#use f-strings and :02d to round cents
#reference: https://realpython.com/python-f-strings/#padding-and-aligning-strings

print(f"the sum of these is €{euros}.{cents:02d}")