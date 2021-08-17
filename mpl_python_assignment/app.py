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

def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
    
def fibonacci_range(nos1,nos2):
    fibonacci_list = []
    for i in range(nos1,nos2+1):
        res = Fibonacci(i);
        # print(res)
        fibonacci_list.append(res)
    return 'Fibonacci Series in range of {} & {} is {}'.format(nos1,nos2,fibonacci_list[1::])


def ascii_val_character(character):
    # print(ord(character))
    return 'ascii_val_character {}'.format(ord(character))

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
    # results.append(Fibonacci(5))
    results.append(fibonacci_range(1,5))
    print(results)