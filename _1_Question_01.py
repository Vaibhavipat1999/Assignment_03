# Question no. 1

#Write a Python function to sum all the numbers in a list.

#Sample List : (8, 2, 3, 0, 7)

#Expected Output : 20

#Explanation:
#Summation should like 8+2+3+0+7 = 20

def sum(nums):
    total = 0
    for i in nums:
        total += i
    return total
print(sum((8, 2, 3, 0, 7)))

