# COLLATZ PROBLEM
# n -> n / 2 (n is even)
# n -> 3n + 1 (n is odd)
# Find the longest collatz chain with a starting number under one million


def main():
    #print('Enter the starting number for your Collatz sequence: ')
    #number = int(input())
    #print(collatz(number))
    greatest = 1
    for i in range(1, 1000000):
        if len(collatz(i)) > greatest:
            greatest = len(collatz(i))
            print(i)


def collatz(a):
    collatzed = []
    collatzed.append(a)
    while a > 1:
        if a % 2 == 0:
            a /= 2
            collatzed.append(a)
        else:
            a = (3 * a) + 1
            collatzed.append(a)
    return collatzed


main()
