'''
2.14 LAB: Expression for calories burned during workout
The following equations estimate the calories burned when exercising (source):

Women: Calories = ( (Age x 0.074) — (Weight x 0.05741) + (Heart Rate x 0.4472) — 20.4022 ) x Time / 4.184

Men: Calories = ( (Age x 0.2017) + (Weight x 0.09036) + (Heart Rate x 0.6309) — 55.0969 ) x Time / 4.184

Write a program using inputs age (years), weight (pounds), heart rate (beats per minute), and time (minutes), respectively. Output calories burned for women and men.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print('Men: {:.2f} calories'.format(calories_man))

Ex: If the input is:

49
155
148
60
Then the output is:

Women: 580.94 calories
Men: 891.47 calories
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
