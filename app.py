def largest_element_list(element_list,n=3):
    element_list.sort()
    # print(element_list[-n:])
    return element_list[-n:]


def validate_even_odd(input_number):
    if (int(input_number) % 2) == 0:
        # print('Even_Nos')
        return '{} is Even Number'.format(input_number)  
    else:  
        # print('Odd_Nos')
        return '{} is Odd Number'.format(input_number)


def  fibonacci_series():
    return 0

def ascii_val_character(character):
    # print(ord(character))
    return ord(character)

def pattern(rows_no):
    for i in range(1, rows_no + 1):

        for k in range(1, i):
            print(" ", end = "")
        for j in range(i, rows_no + 1):
            print("*", end = " ")
        print()
    # for loop for printing lower half
    for i in range(rows_no - 1, 0, -1):

        for k in range(1, i):
            print(" ", end = "")
        for j in range(i, rows_no + 1):
            print("*", end = " ")
        print()

if __name__ == '__main__':
    results = []
    results.append(largest_element_list([1400,-23,970,358,7553,-2]))
    results.append(validate_even_odd(124))
    results.append(ascii_val_character('A'))
    pattern(5)
    print(results)