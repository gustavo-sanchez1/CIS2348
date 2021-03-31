# Gustavo Sanchez PSID:1861118
my_list = []  # my list
words = input().split()  # split the words

for i in words:  # output words and frequencies
    frequency = words.count(i)
    print(i, frequency)
