# 2520 is the smallest number that can be divided by each
#  of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def main():
    for i in range(100000000, 1000000000):
        if devise(i):
            print(i)


def devise(a):
    spring = True
    for i in range(1, 21):
        if a % i != 0:
            spring = False
    return spring


main()
