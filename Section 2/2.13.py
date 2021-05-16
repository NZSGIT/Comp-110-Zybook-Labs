'''
2.13 LAB: Driving costs
Driving is expensive. Write a program with a car's miles/gallon and gas dollars/gallon (both floats) as input, and output the gas cost for 20 miles, 75 miles, and 500 miles.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print('{:.2f} {:.2f} {:.2f}'.format(your_value1, your_value2, your_value3))

Ex: If the input is:

20.0
3.1599
Then the output is:

3.16 11.85 79.00
Note: Real per-mile cost would also include maintenance and depreciation.
'''

'''----------------------------------------------------------------------------------------------------------'''
#Code Below

gasmileage = float(input())
gasprice = float(input())

''test'''

_20mil = (20/gasmileage) * gasprice
_75mil = (75/gasmileage) * gasprice
_500mil = (500/gasmileage) * gasprice

print('{:.2f} {:.2f} {:.2f}'.format(_20mil, _75mil, _500mil))



