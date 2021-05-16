'''
5.21 LAB: Smallest and largest numbers in a list
Write a program that reads a list of integers into a list as long as the integers are greater than zero, then outputs the smallest and largest integers in the list.

Ex: If the input is:

10
5
3
21
2
-6
the output is:

2 and 21
You can assume that the list of integers will have at least 2 values.
'''

'''----------------------------------------------------------------------------------------------------------'''
#Code Below

nums = []

usernum = int(input())

while usernum > 0:
    nums.append(usernum)
    usernum = int(input())
    
print("{} and {}".format(min(nums), max(nums)))
