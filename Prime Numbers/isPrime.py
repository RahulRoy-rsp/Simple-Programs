num = int(input("Enter a number: "))

isPrime = False

if num == 1 or num == 0:
    print(f"{num} is not a prime number nor composite.")
elif num < 0:
    print(f"{num} is a negtive number. Please enter a positive number.")
else:
    for i in range(2, num):
        if num%i == 0:
            isPrime = True
            break
        
    if isPrime:
        print(f"{num} is a Prime Number.")
    else:
        print(f"{num} is not a Prime Number.")
        
