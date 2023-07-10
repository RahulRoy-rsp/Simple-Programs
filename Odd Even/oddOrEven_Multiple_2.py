nums = int(input("How many elements do you wish to enter: "))

for x in range(nums):
    n = int(input(f"Enter element no. {x + 1}: "))

    if (n % 2) == 0:
        print(f'{n} is an even number \n')
    else:
        print(f'{n} is an odd number \n')








''' Example Output
How many elements do you wish to enter: 4
Enter element no. 1: 1
1 is an odd number 

Enter element no. 2: 65
65 is an odd number 

Enter element no. 3: 12
12 is an even number 

Enter element no. 4: 44
44 is an even number 
'''
