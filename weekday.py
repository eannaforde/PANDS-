#weekday.py

#Figure out what day it is today
#Use datetime module that comes with python
from datetime import datetime

#This line will get todays day of the week as a number
#Monday = 0, Tuesday = 1, Saturday = 5, Sunday = 6 
#Reference: https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday

today = datetime.today().weekday()

#check if number is less than 5 (Monday to Friday)
#use if else function to distinguish between weekday and weekend
#Then se print function to return message as to what day it is
if today < 5:
    #if it is then it is a weekday
    print("yes, unfortunately today is a weekday.")
else:
    #otherwise it will be a weekend day
    print("it is the weekend, yay!")


#References
#https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday
#https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
#https://labex.io/tutorials/python-how-to-write-an-efficient-python-function-to-check-if-a-date-is-a-weekday-398285
