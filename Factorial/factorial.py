""" This is a program which shows the factorial of a number 
A factorial of a number can be calculated by the 
product of all positive integers less than or equal to a given positive integer 
and denoted by that integer and an exclamation point.
5!
5 * 4 * 3 * 2 * 1 = 120
"""


num = int(input("Enter a number to find its factorial: "))
facto = 1
count = 1
if num == 0:
    print(f"The factorial for {num} cannot be generated.")
elif num == 1:
    print(f"The factorial for {num} is 1.")
else:
    for i in range(1, num+1):
        facto = facto * i
    print(f"The factorial for {num} is {facto}.")
