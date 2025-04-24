#Accounts.py
#This programme reads in a 10 character account number and outputs the account number with only the last 4 digits showing


def main():

#Ask the user to enter a 10 digit account number
#Use the input() to get user input as a string
#Reference: https://www.w3schools.com/python/ref_func_input.asp
account_number = input("please enter a ten digit account number:")

#Get the last 4 digits of the account number
#use negative slicing to remove last 4 digits
#reference: https://www.w3schools.com/python/python_strings_slicing.asp
last_four = account_number[-4:]

#create the masked version by adding 6 x's infront of the last 4 digits
#reference: # https://www.w3schools.com/python/gloss_python_string_concatenation.asp
masked_account = "x" * 6 + last_four

#print the final masked account number minus the first 6 digits
print(masked_account)

