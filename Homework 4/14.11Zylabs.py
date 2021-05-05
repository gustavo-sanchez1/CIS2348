# GUSTAVO SANCHEZ PSID:1861118

def selection_sort_descent_trace(list_num): #define function
    for i in range(len(list_num)-1): #for loops
        max_num = i
        for j in range(i + 1, len(list_num)):
            if list_num[max_num] < list_num[j]:
                max_num = j
        list_num[i], list_num[max_num] = list_num[max_num], list_num[i]
        for x in list_num:
            print(x, end=" ")
        print()
    return list_num

if __name__ == "__main__": #main program
    numbers = [int(x) for x in input("").split()]
    selection_sort_descent_trace(numbers)