# Actually Problem 11
# Largest Product in a grid.
# Slice notation?

# Importing into parsed list
import re

def gridder():
    w, h = 20, 20
    gridded = [[0 for x in range(w)] for y in range(h)]
    # print(grid)
    gridf = open('grid.txt', 'r+')
    grid = gridf.read()
    count = 0
    # for i in range(0, 60, 3):
    #     num = int(grid[i:i+2])
    #     gridded[0][count] = num
    #     count += 1
    #     #print(num)
    #     print(gridded)
    gridsp = (re.split(' \n', grid))
    print(gridsp)


def gridder2():
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


def main():
    grid = gridder2()
    # First iterate through each number
    greatestprod = 0
    prod = 0
    vert4 = []
    for i in range(0, 20):
        for j in range(0, 20):
        # Now do all horizontal products
            horizontal4 = grid[i][j:j + 4]
            #print(horizontal4)
            if len(horizontal4) == 4:
                prod = horizontal4[0] * horizontal4[1] * horizontal4[2] * horizontal4[3]
            if prod > greatestprod:
                greatestprod = prod
    for k in range(0, 20):
        #for l in range(0, 20):
        placer = 0
        vertcount = 0
        while placer < 20:
            digit = grid[placer][k]
            vert4.append(digit)
            placer += 1
            if len(vert4) == 4:
                vert4prod = vert4[0] * vert4[1] * vert4[2] * vert4[3]
                if vert4prod > greatestprod:
                    greatestprod = vert4prod
                print(vert4)
                print(vert4prod)
                vert4 = []
                vertcount += 1
                placer = vertcount
    # Now need to do the horizontals left to right...

    horz4 = []
    for m in range(0, 20):
        # for l in range(0, 20):
        placerhorz = 0
        horz4count = 0
        while placerhorz < 20:
            try:
                digit = grid[placerhorz][placerhorz + m]
                horz4.append(digit)
                placerhorz += 1
                if len(horz4) == 4:
                    horz4prod = horz4[0] * horz4[1] * horz4[2] * horz4[3]
                    if horz4prod > greatestprod:
                        greatestprod = horz4prod
                    print(horz4)
                    print(horz4prod)
                    if horz4prod > greatestprod:
                        greatestprod = horz4prod
                    horz4 = []
                    horz4count += 1
                    placerhorz = horz4count
            except IndexError:
                break

    horz4l2r = []
    for n in range(19, -1, -1):
        # for l in range(0, 20):
        placerhorz = 19
        horz4count = 0
        while placerhorz <= 0:
            try:
                digit = grid[placerhorz][placerhorz + n]
                horz4l2r.append(digit)
                placerhorz += 1
                if len(horz4l2r) == 4:
                    horz4prod = horz4l2r[0] * horz4l2r[1] * horz4l2r[2] * horz4l2r[3]
                    if horz4prod > greatestprod:
                        greatestprod = horz4prod
                    print(horz4l2r)
                    print(horz4prod)
                    if horz4prod > greatestprod:
                        greatestprod = horz4prod
                    horz4l2r = []
                    horz4count += 1
                    placerhorz = horz4count
            except IndexError:
                break


    print(greatestprod)
        # if len(fournum) == 4:
        #     prod = fournum[0] * fournum[1] * fournum[2] * fournum[3]
        #     print(prod)

main()
