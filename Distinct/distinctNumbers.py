from collections import Counter

# arr = [87, 44, 21, 44, 2, 0, 45, 0, 7]
arr = list(map(int, input("Enter numbers separted by space: ").split()))

arrCount = Counter(arr)
print("Distinct elements in the array: ")
for i, j in arrCount.items():
  if j == 1:
    print(i, end = ' ')
