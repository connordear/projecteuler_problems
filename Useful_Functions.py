# Contains useful functions for helping solve Project Euler Problems


# Find n!
def factorial(num):
    running_total = 1
    for i in range(num, 1, -1):
        running_total *= i
    return running_total


# Sum together the digits of a number
def digit_sum(num):
    runsum = 0
    str_num = str(num)
    for i in range(0, len(str_num)):
        runsum += int(str_num[i])
    return runsum


# Returns an array of all the factors of the inputted value
def factorizor(a):
    factors = []
    for i in range(1, int(math.sqrt(a)) + 1):
        if a % i == 0:
            factors.append(i)
            factors.append((a/i))
    return factors


# Useful for reversing a string
def reverse_this(a):
    rev = ''.join(reversed(a))
    return rev


# Determines the primality of the input
def check_prime(a):
    test = True
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            test = False
            break
    return test


# Imports grid.txt file into a m x n 2D array
def gridder():
    w, h = 20, 20
    gridded = [[0 for x in range(w)] for y in range(h)]
    lines = open('grid.txt').read().splitlines()
    count = 0
    for line in lines:
        splitted = line.split(' ')
        for i in range(0, len(splitted)):
            gridded[count][i] = int(splitted[i])
        count += 1
    return gridded
