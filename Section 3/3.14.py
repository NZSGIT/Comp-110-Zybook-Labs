'''
3.14 LAB: Input and formatted output: House real estate summary
Sites like Zillow get input about house prices from a database and provide nice summaries for readers. Write a program with two inputs, current price and last month's price (both integers). Then, output a summary listing the price, the change since last month, and the estimated monthly mortgage computed as (current_price * 0.051) / 12.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print('{:.2f}'.format(your_value))

Ex: If the input is:

200000 
210000
the output is:

This house is $200000. The change is $-10000 since last month.
The estimated monthly mortgage is $850.00.
Note: Getting the precise spacing, punctuation, and newlines exactly right is a key point of this assignment. Such precision is an important part of programming.
'''

'''----------------------------------------------------------------------------------------------------------'''
#Code Below

current_price = int(input())
last_months_price = int(input())

print("This house is ${}. The change is ${} since last month.".format(current_price, current_price-last_months_price))
print("The estimated monthly mortgage is ${:.2f}.".format((current_price * 0.051) / 12))
