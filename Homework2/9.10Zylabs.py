# Gustavo Sanchez PSID: 1861118

import csv  # import file
input_file = input()
f = open(input_file, 'r')  # open and read
myReader = csv.reader(f)
for row in myReader:
    word = set(row)
    for word in row:  # count number of words
        count = row.count(word)
        print(word, count)
