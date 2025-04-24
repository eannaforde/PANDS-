#Bank.py
#This program will prompt the user to read in two money amounts
#Add the two amounts
#Print the answer in a human readable format

def main (): 
#Ask user for the first amount in cents 
#use input() function and wrap it with int() to convert the input string to an integer
#reference: https://www.w3schools.com/python/ref_func_input.asp

Amount1 = int(input("Enter amount one in cents"))
#Ask user for the second amount in cents
Amount2 = int(input("Enter amount two in cents"))

#Add the two amounts together
total_cents = amount1 + amount2

#Convert the total amount to euros and cents
#use // to get whole euros, % to get the leftover cents
#reference: https://www.w3schools.com/python/python_operators.asp

euros = total_cents // 100
cents = total_cents % 100
