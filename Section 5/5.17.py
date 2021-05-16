'''
5.17 LAB: Output range with increment of 5
Write a program whose input is two integers. Output the first integer and subsequent increments of 5 as long as the value is less than or equal to the second integer.

Ex: If the input is:

-15
10
the output is:

-15 -10 -5 0 5 10 
Ex: If the second integer is less than the first as in:

20
5
the output is:

Second integer can't be less than the first.
For coding simplicity, output a space after every integer, including the last.
'''

'''----------------------------------------------------------------------------------------------------------'''
#Code Below

n = int(input())
target = int(input())

if(n > target):
    print("Second integer can't be less than the first.")
    exit()

while (n <= target):
    print(n, end=' ')
    n += 5
    
print()
