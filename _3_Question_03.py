# Question no. 3

# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

# Sample String : 'The quick Brow Fox'

# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

x = 'The quick Brow Fox'
def char(x):
    u = 0
    l = 0
    for i in x:
        if i>='a' and i<='z':
            l += 1
        if i >='A' and i<='Z':
            u += 1

    print("UpperCase letter in the String",u)
    print("LowerCase letter in the String",l)
    
char(x)