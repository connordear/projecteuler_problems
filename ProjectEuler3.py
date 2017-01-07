# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Receive input for number
import math
import time


# def main():
#     time.clock()
#     for i in range(600851475143, 1, -1):
#         if check_prime2(i) and 600851475143 % i == 0:
#             print(i)
#             break
#     print(str(time.clock()) + ' seconds for completion.')
#
#
# def check_prime2(a):
#     monet = True
#     for i in range(2, int(math.sqrt(a)) + 1):
#         if a % i == 0:
#             monet = False
#             break
#     return monet
#
#
# def check_prime3(a):
#     monet = True
#     if a % 2 == 0:
#         monet = False
#     else:
#         for i in range(3, int(math.sqrt(a)) + 1):
#             if i % 2 != 0:
#                 if a % i == 0:
#                     monet = False
#     return monet


def factorizor(a):
    factors = []
    for i in range(1, int(math.sqrt(a)) + 1):
        if a % i == 0:
            factors.append(i)
            factors.append((a/i))
    return factors


def testfac():
    factors = factorizor(600851475143)
    for i in factors:
        if check_prime2(i):
            print(i)



testfac()
