# Getting a number from the user

number = int(input("Enter a number: "))
print("Reversing")

temp = number
reverse = 0

while number != 0:
    remainder = number % 10
    reverse = (reverse * 10) + (remainder)
    number = number // 10

print(f"The reverse of {temp} is {reverse}")


'''
Example for the above code
Suppose we take input as 102
As it is not equals to Zero,
number = 102
(1) remainder will be: 2
...{ 102 % 10 = 2}

(2) reverse will be 2
...{ (0*10) + (2) = 2}


(3) number will be 10
...{ 102//10 = 10}

(4) Then again it will go to the top of loop to check the condition
number = 10
remainder = 0
reverse = 2


'''
