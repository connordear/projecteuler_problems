# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
import math
import time


def main():
    time.clock()
    summer = 0
    for i in range(1, 2000000):
        if check_prime2(i):
            summer += i
    print(summer)
    print(time.clock())


def check_prime2(a):
    monet = True
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            monet = False
            break
    return monet


main()
