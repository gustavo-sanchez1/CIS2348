# Gustavo Sanchez PSID:1861118

list_of_month = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6, "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12}
month = str(input("Enter month"))
day = (input("Enter day"))
year = (input("Enter year"))

print(month, day + ',' + '', year)

file = open('inputDates.txt', 'r')
f = file.read()
