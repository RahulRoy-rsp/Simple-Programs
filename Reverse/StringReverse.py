user_input = (input("Enter a String: "))

string = ''
for i in user_input:
    string = i + string
print(f"Reverse of {user_input} using loop is {string}")

''' Alternate Method: Slicing is built in function in python
Here [::-1] will read the string from backwards i.e in reverse form
'''

print("\nAlternate Method")
reversed_string = user_input[::-1]
print(f"Reverse of {user_input} using slicing is {reversed_string}")

# Fun part of this program is that we can also reverse a number easily.
