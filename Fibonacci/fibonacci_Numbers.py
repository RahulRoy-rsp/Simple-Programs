""" This is a program which shows the fibonacci numbers sequence till the number specified.
Fibonacci series starts from 0 and 1 and next terms are calculated by adding 
the previous two terms from the sequence.
0,
1,
0 + 1 = 1,
1 + 1 = 2, and so on... """

numbers = int(input("How many numbers do you want? "))

first, second = 0, 1

def firstTwo():
    print(first)
    print(second)

if numbers <= 0:
    print("No fibonacci numbers can be generated.")
elif numbers == 1:
    print(f"The first fibonacci number is:")
    print(first)
elif numbers == 2:
    print(f"The first two fibonacci numbers are:")
    firstTwo()
else:
    print(f"The first {numbers} fibonacci numbers are:")
    firstTwo()
    for i in range(2, numbers):
        n_ = first + second
        first = second
        second = n_
        print(n_)
         