myArr = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"Entered array is: {myArr}")


# Approach 1
print(f"The average of the array is {sum(myArr)/len(myArr)}")

# Approach 2
total = 0
for i in myArr:
    total += i

print(f"The average of the array is {total/len(myArr)}")


# Approach 3
from statistics import mean
print(f"The average of the array is {mean(myArr)}")


# Approach 4
import numpy as np
print(f"The average of the array is {np.average(myArr)}")
