# GUSTAVO SANCHEZ PSID:1861118
parts = input().split() # split input
name = parts[0]
while name != '-1':
    try: # increase age by 1
        age = int(parts[1]) + 1

    except ValueError:
        age = 0
    print('{} {}'.format(name, age)) # format name and age
    parts = input().split()
    name = parts[0]