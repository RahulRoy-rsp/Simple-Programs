num = int(input("Enter a number: "))

prod = 1
if num == 0:
    print(f"Product of the digits of the number {num} is: 0")
elif num > 0:
    while num > 0:
        curr = num % 10
        prod *= curr
        num = num//10
        
    print(f"Product of the digits of the number is: {prod}")
else:
    print("Please Enter a positive number")
