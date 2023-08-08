myArr = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"Entered array is: {myArr}")


# Approach 1
print(f"Smallest number is {min(myArr)}")


# Approach 2
sm = myArr[0]
for i in range(len(myArr)):
    if sm > myArr[i]:
        sm = myArr[i]
print(f"Smallest number is {sm}")

        
# Approch 3
myArr.sort()
print(f"Smallest number is {myArr[0]}")
