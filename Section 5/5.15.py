'''
5.15 LAB: Count input length without spaces, periods, exclamation points, or commas
Given a line of text as input, output the number of characters excluding spaces, periods, exclamation points, or commas.

Ex: If the input is:

Listen, Mr. Jones, calm down.
the output is:

21
'''

'''----------------------------------------------------------------------------------------------------------'''
#Code Below

user_text = input()
blah = 0

for char in user_text:
    if not (char == ',' or char == ' ' or char == '!' or char == '.'):
        blah += 1

print(blah)
