'''
4.18 LAB*: Program: Automobile service invoice
(1) Output a menu of automotive services and the corresponding cost of each service. (2 pts)

Ex:

Davy's auto shop services
Oil change -- $35
Tire rotation -- $19
Car wash -- $7
Car wax -- $12



(2) Prompt the user for two services from the menu. (2 pts)

Ex:

Select first service:
Oil change
Select second service:
Car wax



(3) Output an invoice for the services selected. Output the cost for each service and the total cost. (3 pts)


Davy's auto shop invoice

Service 1: Oil change, $35
Service 2: Car wax, $12

Total: $47



(4) Extend the program to allow the user to enter a dash (-), which indicates no service. (3 pts)

Ex:

Davy's auto shop services
Oil change -- $35
Tire rotation -- $19
Car wash -- $7
Car wax -- $12

Select first service:
Tire rotation
Select second service:
-

Davy's auto shop invoice

Service 1: Tire rotation, $19
Service 2: No service

Total: $19
'''

'''----------------------------------------------------------------------------------------------------------'''
#Code Below

print("Davy's auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n")

Service1 = input("Select first service:\n")

Service2 = input("Select second service:\n")

print("\nDavy's auto shop invoice\n")

List = [Service1, Service2]
total = 0
z = 0
for x in List:
    if x == "Oil change":
        List[z] += ", $35"
        total += 35
    elif x == "Tire rotation":
        List[z] += ", $19"
        total += 19
    elif x == "Car wash":
        List[z] += ", $7"
        total += 7
    elif x == "Car wax":
        List[z] += ", $12"
        total += 12
    elif x == "-":
        List[z] = "No service"
    z += 1
        
print("Service 1:", List[0])
print("Service 2:", List[1] + "\n")

print("Total: ${}".format(total))
    
        



