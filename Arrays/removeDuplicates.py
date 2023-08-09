myArr = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"Entered array is: {myArr}")


# Approach 1
print(f"The array without duplicates elements is: {set(myArr)}")


# Approach 2
temp = []
for i in myArr:
    if i not in temp:
        temp.append(i)
print(f"The array without duplicates elements is: {temp}")


# Approach 3
dict_ = {}
for i in myArr:
    if i not in dict_:
        dict_[i] = 1

print(f"The array without duplicates elements is: {dict_.keys()}")
