myArr = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"Entered array is: {myArr}")

# Approach 1
dict_ = {}
for i in myArr:
    if i not in dict_:
        dict_[i] = 1
    else:
        dict_[i] += 1

ans = []
for i, j in dict_.items():
    if j == 1:
        ans.append(i)
print(f"Elements appearing only once in the array are: {ans}")



# Approach 2
from collections import Counter
ans_ = []
arrCount = Counter(myArr)
for i, j in arrCount.items():
    if j == 1:
        ans_.append(i)
print(f"Elements appearing only once in the array are: {ans}")


