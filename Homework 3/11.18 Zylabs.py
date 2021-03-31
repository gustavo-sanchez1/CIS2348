# Gustavo Sanchez PSID:1861118
my_list = []  # my list
integers = input().split()  # split the integers that get put in
for num in integers:  # check for positive numbers
    num = int(num)
    if num >= 0:
        my_list.append(num)
my_list.sort()  # ascending order
for num in my_list:
    print(num, '', end='')
