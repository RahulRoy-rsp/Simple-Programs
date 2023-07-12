# make sure to install wikipedia
# pip install wikipedia

import wikipedia as wp

inp = input("Enter the text you want to search on Wikipedia: ")

print(f" The title info for {inp} is: \n", wp.page(inp))
print(f" The Summary of {inp} is: \n", wp.summary(inp))
