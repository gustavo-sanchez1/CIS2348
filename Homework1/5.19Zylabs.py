print("Davy's auto shop services")  # print menu
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")

oil_change = 35  # set variables with prices
tire_rotation = 19
car_wash = 7
car_wax = 12

print('\nSelect first service:')  # get user's input and print them
first_service = str(input())
print('Select second service:')
second_service = str(input())

print("\nDavy's auto shop invoice")

if first_service == "Oil change":  # use if statement to determine the 1st and 2nd services
    first_price = oil_change
if first_service == "Tire rotation":
    first_price = tire_rotation
if first_service == "Car wash":
    first_price = car_wash
if first_service == "Car wax":
    first_price = car_wax

if second_service == "Oil change":
    second_price = oil_change
if second_service == "Tire rotation":
    second_price = tire_rotation
if second_service == "Car wash":
    second_price = car_wash
if second_service == "Car wax":
    second_price = car_wax
print("\nService 1: " + first_service + ', $' + str(first_price))  # print selections
print("Service 2: " + second_service + ', $' + str(second_price))
total_cost = first_price + second_price
print('\nTotal: ' + '$' + str(total_cost))