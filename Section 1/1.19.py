'''
1.19 LAB: Warm up: Basic output with variables
This zyLab activity prepares a student for a full programming assignment. Warm up exercises are typically simpler and worth fewer points than a full programming assignment, and are well-suited for an in-person scheduled lab meeting or as self-practice.


A variable like user_num can store a value like an integer. Extend the given program as indicated.

Output the user's input. (2 pts)
Output the input squared and cubed. Hint: Compute squared as user_num * user_num. (2 pts)
Get a second user input into user_num2, and output the sum and product. (1 pt)

Note: This zyLab outputs a newline after each user-input prompt. For convenience in the examples below, the user's input value is shown on the next line, but such values don't actually appear as output when the program runs.

Enter integer:
4
You entered: 4
4 squared is 16 
And 4 cubed is 64 !!
Enter another integer:
5
4 + 5 is 9
4 * 5 is 20
'''

'''----------------------------------------------------------------------------------------------------------'''
#Code Below

user_num = int(input('Enter integer:\n'))
print("You entered:", user_num)
print("{} squared is {}".format(user_num, user_num**2))
print("And {} cubed is {} !!".format(user_num, user_num**3))
user_num2 = int(input('Enter another integer:\n'))

print("{} + {} is {}".format(user_num, user_num2, user_num + user_num2))
print("{} * {} is {}".format(user_num, user_num2, user_num * user_num2))


'''Output the user's input. (2 pts)
Output the input squared and cubed. Hint: Compute squared as user_num * user_num. (2 pts)
Get a second user input into user_num2, and output the sum and product. (1 pt)'''
