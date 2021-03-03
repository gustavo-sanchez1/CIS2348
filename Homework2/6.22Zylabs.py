# Gustavo Sanchez PSID:1861118

integer1 = int(input())  # Print the 6 integers
integer2 = int(input())
integer3 = int(input())
integer4 = int(input())
integer5 = int(input())
integer6 = int(input())

solution = False

for x in range(-10, 11):  # for loop, use brute force
    for y in range(-10, 11):
        if integer1*x+integer2*y == integer3 and integer4*x+integer5*y == integer6  # Check if x and y satisfy both equations
            print(x, y)
            solution = True

if solution == False:  # if they don't, there is no solution
    print('No solution')
