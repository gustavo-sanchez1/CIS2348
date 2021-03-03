# Gustavo Sanchez PSID:1861118

original_string = input()  # get input
original_string = original_string.replace(' ', ' ')  # get rido of spaces
new_string = (original_string[::-1])  # reverse the sring
if original_string == new_string:  # check is original string and the revrse match
    print(original_string, 'is a palindrome')
else:
    print(original_string, 'is not a palindrome')
