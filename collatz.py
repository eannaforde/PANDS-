# collatz.py
#This programme asks the user for a positive number and prints the collatz sequence
#The collatz sequence asks the user to input any positive integer
#If the number is even, divide it by 2
#if the number is odd,multiply it by 3 and add 1
#repeat until the number becomes 1 then end the program

#ask the user to enter a number
#input() is used to enter number as a string
#int() converts string to an integer
number = int(input("please enter a positive integer:"))

#keep repeating until the number becomes 1
#if checks if the nmber is even
#else if the number is odd
while number != 1:
    if(number%2==0):
        number=number//2
    else:
        number=number*3+1
#program continues
#sequence ends
    print(number)
#Reference:https://www.youtube.com/watch?v=lAp_5qTdOhM
#Reference:https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff   
#Reference:https://how.dev/answers/how-to-generate-the-collatz-sequence-in-python