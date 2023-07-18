num = int(input("Enter a number: "))

sum_ = 0

while num > 0:
    curr = num % 10
    sum_ += curr
    num = num//10
    
print(f"Sum of the digits of the number is: {sum_}")
