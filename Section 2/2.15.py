'''
2.15 LAB: Using math functions
Given three floating-point numbers x, y, and z, output x to the power of z, x to the power of (y to the power of z), the absolute value of (x minus y), and the square root of (x to the power of z).

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print('{:.2f} {:.2f} {:.2f} {:.2f}'.format(your_value1, your_value2, your_value3, your_value4))

Ex: If the input is:

5.0
1.5
3.2
Then the output is:

172.47 361.66 3.50 13.13
'''

'''----------------------------------------------------------------------------------------------------------'''
#Code Below


Age = int(input())
Weight = int(input())
HeartRate = int(input())
Time = int(input())


calories_woman = ((Age * 0.074) - (Weight * 0.05741) + (HeartRate * 0.4472) - 20.4022) * Time / 4.184
calories_man = ((Age * 0.2017) + (Weight * 0.09036) + (Heart Rate * 0.6309) - 55.0969) * Time / 4.184

print('Women: {:.2f} calories'.format(calories_woman))
print('Men: {:.2f} calories'.format(calories_man))
