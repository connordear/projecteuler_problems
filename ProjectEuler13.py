# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers. (located in
# file proj13.txt.


def main():
    summer = 0
    grid = open('proj13.txt', 'r')
    for line in grid:
        sixdig = int(line[0] + line[1] + line[2] + line[3] + line[4] + line[5] + line[6] + line[7] + line[8] +
                     line[9] + line[10] + line[11] + line[12] + line[13] + line[14] + line[15] + line[16] +
                     line[17] + line[18] + line[19] + line[20])
        #print(sixdig)
        summer += sixdig
    print(summer)
    grid.close()


main()
