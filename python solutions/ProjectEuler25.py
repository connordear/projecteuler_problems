def main():
    n_minus_one = 1
    n_minus_two = 1
    n = n_minus_one + n_minus_two
    index = 3
    num_digits = len(str(n))
    while num_digits < 1000:
        n_minus_two = n_minus_one
        n_minus_one = n
        n = n_minus_one + n_minus_two
        index += 1
        num_digits = len(str(n))
        print("Index: ", index, "Number of Digits: ", num_digits)


if __name__ == '__main__':
    main()
