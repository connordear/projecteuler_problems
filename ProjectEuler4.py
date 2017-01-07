# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

import sys
import csv
import string


def main():
    # print('Enter the number you want to reverse: ')
    # numero = input()
    # numerorev = reverse_this(numero)
    # print(numerorev)
    # if palindrome(numerorev):
    #     print('The number you have entered ' + numero + ' is indeed a palindrome!')
    # else:
    #     print('The number you have entered ' + numero + ' is not a palindrome.')
    for i in range(900, 1000):
        for j in range(900, 1000):
            prod = str(i * j)
            #print(prod)
            if palindrome(prod):
                print(prod)


def reverse_this(a):
    rev = ''.join(reversed(a))
    return rev


def palindrome(b):
    if b == reverse_this(b):
        pal = True
    else:
        pal = False
    return pal


main()



