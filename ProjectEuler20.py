# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!


def factorial(num):
    running_total = 1
    for i in range(num, 1, -1):
        running_total *= i
    return running_total


def digit_sum(num):
    runsum = 0
    str_num = str(num)
    for i in range(0, len(str_num)):
        runsum += int(str_num[i])
    return runsum


def main():
    num = int(input("Which number do you want to know the factorial of? "))
    factorial_num = factorial(num)
    print(factorial_num)
    print(digit_sum(factorial_num))


main()
