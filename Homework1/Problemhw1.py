print('Birthday Calculator')  # output the current day
print('Current day')
print('Month: ')
current_month = int(input())
print("Day: ")
current_day = int(input())
print('Year: ')
current_year = int(input())
print('Birthday')  # print user's birthday
print('Month: ')
birthday_month = int(input())
print('Day: ')
birthday_day = int(input())
print('Year: ')
birthday_year = int(input())
age = current_year - birthday_year  # calculate age
print("You are", age, "years old.")
if current_month == birthday_month and current_day == birthday_day:
    print('\nHappy birthday!')
