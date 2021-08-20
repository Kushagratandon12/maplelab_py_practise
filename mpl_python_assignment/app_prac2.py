import random

def middle_of_three(a, b, c):
    if ((a < b and b < c) or (c < b and b < a)) :
        return b;
    if ((b < a and a < c) or (c < a and a < b)) :
        return a;
    else :
        return c

def findTrailingZeros(n):
    count = 0
    i = 5
    while (n / i>= 1):
        count += int(n / i)
        i *= 5
    return int(count)

def absent_digits(number):
  all_nums = set([0,1,2,3,4,5,6,7,8,9])
  absent_nos = set([int(i) for i in number])
  absent_nos = absent_nos.symmetric_difference(all_nums)
  absent_nos = sorted(absent_nos)
  return absent_nos


def rev_number(number):
  while True:
    rev_nos = str(number)
    if rev_nos == rev_nos[::-1]:
      break
    else:
      add_rev_nos = int(rev_nos[::-1])
      number += add_rev_nos
  return number 

def check_random(list_nos):
    random.shuffle(list_nos)
    return list_nos

if __name__ == '__main__':
    results = [middle_of_three(10,44,2),findTrailingZeros(10),rev_number(1234),check_random(['a','e','i','o','u']),absent_digits([9,4,1,5,1,1,5,6,8,1])]
    print(results)