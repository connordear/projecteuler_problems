# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


def word_builder(a):
    num_to_word = {}
    num_to_word[0] = ''
    num_to_word[1] = 'one'
    num_to_word[2] = 'two'
    num_to_word[3] = 'three'
    num_to_word[4] = 'four'
    num_to_word[5] = 'five'
    num_to_word[6] = 'six'
    num_to_word[7] = 'seven'
    num_to_word[8] = 'eight'
    num_to_word[9] = 'nine'
    num_to_word[10] = 'ten'
    num_to_word[11] = 'eleven'
    num_to_word[12] = 'twelve'
    num_to_word[13] = 'thirteen'
    num_to_word[14] = 'fourteen'
    num_to_word[15] = 'fifteen'
    num_to_word[16] = 'sixteen'
    num_to_word[17] = 'seventeen'
    num_to_word[18] = 'eighteen'
    num_to_word[19] = 'nineteen'
    num_to_word[20] = 'twenty'
    num_to_word[30] = 'thirty'
    num_to_word[40] = 'forty'
    num_to_word[50] = 'fifty'
    num_to_word[60] = 'sixty'
    num_to_word[70] = 'seventy'
    num_to_word[80] = 'eighty'
    num_to_word[90] = 'ninety'
    num_to_word[100] = 'hundred'

    word = 'hold'
    digits = len(str(a))
    first_digit = int(str(a)[:1])
    if digits > 1:
        second_digit = int(str(a)[1:2])
    if digits > 2:
        third_digit = int(str(a)[2:])

    if digits == 1:
        word = num_to_word[a]
    elif digits == 2:
        if first_digit == 1:
            word = num_to_word[a]
        else:
            word = num_to_word[first_digit * 10] + num_to_word[second_digit]
    elif digits == 3:
        if second_digit == 0 and third_digit == 0:
            word = num_to_word[first_digit] + num_to_word[100]
        elif second_digit == 1:
            word = num_to_word[first_digit] + num_to_word[100] + 'and' + num_to_word[int(str(a)[1:])]
        else:
            word = num_to_word[first_digit] + num_to_word[100] + 'and' + num_to_word[second_digit * 10] + num_to_word[third_digit]

    return word


def main():
    print(word_builder(999))
    count = 0
    for i in range(1, 1000):
        this_word = word_builder(i)
        print(this_word)
        count += len(this_word)
    # account for 1000
    count += 11
    print('The final count is: ' + str(count))
if __name__ == '__main__':
    main()

