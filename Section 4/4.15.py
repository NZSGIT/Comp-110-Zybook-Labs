'''
4.15 LAB: Exact change
Write a program with total change amount as an integer input, and output the change using the fewest coins, one coin type per line. The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.

Ex: If the input is:

0 
(or less than 0), the output is:

No change 
Ex: If the input is:

45
the output is:

1 Quarter
2 Dimes
'''

'''----------------------------------------------------------------------------------------------------------'''
#Code Below

import math
Change = int(input())

if Change == 0:
    print("No change")
    exit()
 
DolAmount = 0 
QAmount = 0
DAmount = 0 
NAmount = 0 
PAmount = 0
 
DolAmount = math.floor(Change / 100)
Change = Change % 100  

if Change != 0: 
    QAmount = math.floor(Change / 25)
    Change = Change % 25 
    
    if Change != 0:
        DAmount = math.floor(Change / 10)
        Change = Change % 10
     
        if Change != 0:
            NAmount = math.floor(Change / 5)
            Change = Change % 5 
            
            if Change != 0:
                PAmount = math.floor(Change / 1)
               
ListofChange = [DolAmount, QAmount, DAmount, NAmount, PAmount]

t = 0
for x in ListofChange:
    add_s = 's' if x > 1 else ''
    if x > 0:
        x = str(x)
        if t == 0:
            print(x+" Dollar"+add_s)
            
        elif t == 1:
            print(x+" Quarter"+add_s)    
        
        elif t == 2:
            print(x+" Dime"+add_s)   
            
        elif t == 3:
            print(x+" Nickel"+add_s)   
        
        elif t == 4:
            if int(x) > 1:
                print(x+" Pennies")
            else:
                print(x+" Penny")
            
    t += 1


