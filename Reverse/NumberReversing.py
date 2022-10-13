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

