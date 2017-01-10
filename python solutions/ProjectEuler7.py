# #By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the
# 10001st
# prime
# number?
import time
import math


def main():
    time.clock()
    counter = 0
    itter = 2
    while counter < 10002:
        if check_prime2(itter):
            counter += 1
            #print(itter)
            if counter == 10001:
                print(itter)
        itter += 1
    print(str(time.clock()) + 'seconds since start of main.')


def main2():
    time.clock()
    counter = 0
    itter = 2
    while counter < 10001:
        if not check_composite(itter):
            counter += 1
            if counter == 10000:
                print(itter)
        itter += 1
    print(str(time.clock()) + 'seconds since start of main2.')


def check_prime(a):
    monet = True
    for i in range(2, a):
        if a % i == 0:
            monet = False
            break
    return monet


def check_prime2(a):
    monet = True
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            monet = False
            break
    return monet


def check_prime3(a):
    monet = True
    if a % 2 == 0:
        monet = False
    else:
        for i in range(3, int(math.sqrt(a)) + 1):
            if i % 2 != 0:
                if a % i == 0:
                    monet = False
    return monet


def check_composite(a):
    # Check compositeness and report
    one = False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            one = True
            break
    return one


main()
