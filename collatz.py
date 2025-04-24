# collatz.py
#This programme asks the user for a positive number and prints the collatz sequence
#The collatz sequence asks the user to input any positive integer
#If the number is even, divide it by 2
#if the number is odd,multiply it by 3 and add 1
#repeat until the number becomes 1 then end the program

#ask the user to enter a number
number = int(input("please enter a positive integer:"))

#keep repeating until the number becomes 1
while number != 1: