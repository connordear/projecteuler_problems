# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def main():
    summer = 0
    for i in range(1, 101):
        summer += i ** 2
    print(summer)
    fall = 0
    for i in range(1, 101):
        fall += i
    winter = fall ** 2
    print(winter)
    spring = winter - summer
    print(spring)


main()
