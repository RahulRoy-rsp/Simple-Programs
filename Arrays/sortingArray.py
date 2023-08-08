myArr = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"Entered array is: {myArr}")


# Approach 1
myArr.sort()
print(f'Sorted Array is: {myArr}')


# Approach 2
myArr.sort()
print(f'Sorted Array is: {sorted(myArr)}')


# Approach 3
for i in range(len(myArr)):
    for j in range(len(myArr)- i - 1):
        if myArr[j] > myArr[j + 1]:
            myArr[j], myArr[j+1] = myArr[j+1], myArr[j]

print(f'Sorted Array is: {myArr}')


# Approach 4
for i in range(len(myArr)):
    smallest = i
    for j in range(i + 1, len(myArr)):
        if myArr[j] < myArr[smallest]:
            smallest = j        
    myArr[i], myArr[smallest] = myArr[smallest], myArr[i]

print(f'Sorted Array is: {myArr}')


# Approach 5
# https://github.com/RahulRoy-rsp/DataStructures-Algorithms/tree/main/Merge%20Sort
