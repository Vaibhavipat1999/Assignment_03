# Question no. 2

# Write a Python program to reverse a string.

# Sample String : "1234abcd"
# Expected Output : "dcba4321"


def reverse(string):
    string = [string[i] 
    for i in range(len(string)-1, -1, -1)]
    return "".join(string)

s = "1234abcd"
print("The original string : ", s)
print("The reversed string : ", reverse(s))