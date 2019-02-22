# 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

hrs = raw_input ('Enter Hours:')
hours = float(hrs)
hourly_rate = float(input('Enter Rate:'))

if hours <= 40:
    pay = hours * hourly_rate
elif hours > 40:
    pay = 40 * hourly_rate + (hours-40)*1.5*hourly_rate
   
print(pay)
