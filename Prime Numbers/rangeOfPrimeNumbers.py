nums = list(map(int, input("Enter the two numbers separated by space for which you want to find prime numbers. Eg: 30 74 \n:- ").split()))

start = nums[0]
end = nums[1]
primes = list()

for num in range(start, end + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           primes.append(num)
           

if len(primes) > 0:
    print(f'Prime Numbers between the numbers starting from {start} and ends with {end} are:')
    for i in primes:
        print(i, end = ' ')
else:
    print(f'There are no Prime Numbers between the numbers starting from {start} and ends with {end}')
