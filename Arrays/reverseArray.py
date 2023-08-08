myArr = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"Entered array is: {myArr}")


# Approach 1
myArr.reverse()
print(f"Reversed array is {myArr}")


# Approch 2
print(f"Reversed array is {myArr[::-1]}")


# Approach 3
l = 0
r = len(myArr) - 1
while l < r:
    myArr[l], myArr[r] = myArr[r], myArr[l]
    l += 1
    r -= 1
print(f"Reversed array is {myArr}")

# Approach 4
print(f"Reversed array is {list(reversed(myArr))}")
