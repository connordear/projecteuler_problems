# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math


def main():
    # print(tripleter(3, 4))
    for i in range(100, 1000):
        for j in range(100, 1000):
            summer = tripleter(i, j)
            #print(summer)
            if summer == 1000:
                c = math.sqrt(i ** 2 + j ** 2)
                prod = i * j * c
                print('a = ' + str(i) + ', b = ' + str(j) + ', and c = ' + str(c))
                print('The product of abc is ' + str(prod))



def tripleter(a,b):
    pyth = math.sqrt(a ** 2 + b ** 2) + a + b
    return pyth


main()
