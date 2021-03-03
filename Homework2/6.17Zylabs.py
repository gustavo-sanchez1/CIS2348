# Gustavo Sanchez PSID:1861118


password = str(input())  # Input the password

password = password.replace('i', '!')  # Replace each letter with a different using the replace method
password = password.replace('a', '@')
password = password.replace('m', 'M')
password = password.replace('B', '8')
password = password.replace('o', '.')

password = password + 'q*s'  # Add q*s to the end
print(password)  # print new password
