'''
2.12 LAB: Divide by x
Write a program using integers user_num and x as input, and output user_num divided by x three times.

Ex: If the input is:

2000
2
Then the output is:

1000 500 250
Note: In Python 3, integer division discards fractions. Ex: 6 // 4 is 1 (the 0.5 is discarded).
'''

'''----------------------------------------------------------------------------------------------------------'''
#Code Below

import math
userNum = float(input())
divder = float(input())

print("{} {} {}".format(math.floor(userNum/divder), math.floor((userNum/ divder)/divder), math.floor(((userNum/divder)/divder)/divder )))


