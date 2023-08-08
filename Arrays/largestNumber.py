myArr = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"Entered array is: {myArr}")


# Approach 1
print(f"Largest number is {max(myArr)}")


# Approach 2
lar = myArr[0]
for i in range(len(myArr)):
    if lar < myArr[i]:
        lar = myArr[i]
print(f"Largest number is {lar}")

        
# Approch 3
myArr.sort()
print(f"Largest number is {myArr[-1]}")
