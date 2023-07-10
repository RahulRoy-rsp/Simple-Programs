num = list(map(int, input("Enter numbers separated by space: ").split()))

for i in num:
    if (i % 2) == 0:
        print(f'{i} is an even number')
    else:
        print(f'{i} is an odd number')








''' Example Output
Enter numbers separated by space: 12 21 211 -1 0 7 74
12 is an even number
21 is an odd number
211 is an odd number
-1 is an odd number
0 is an even number
7 is an odd number
74 is an even number
'''
