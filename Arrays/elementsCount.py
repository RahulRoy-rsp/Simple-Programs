myArr = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"Entered array is: {myArr}")

# Approach 1
dict_ = {}
for i in myArr:
    if i not in dict_:
        dict_[i] = 1
    else:
        dict_[i] += 1
print(f"Elements with their counts are: {dict_}")


# Approach 2
from collections import Counter
arrCount = Counter(myArr)
print(f"Elements with their counts are: {arrCount}")
