myArr = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"Entered array is: {myArr}")


# Approach 1
print(f"The sum of the elements of the array is {sum(myArr)}")

# Approach 2
total = 0
for i in myArr:
    total += i
print(f"The sum of the elements of the array is {total}")
