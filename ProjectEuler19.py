# How many Sundays fell on the 1st of a month in the first century?
# Jan 1 1901 to Dec 31 2000
# Jan 1 1901 was Monday
# Months 9 4 6 11 have 30
# Months 1 3 5 7 8 10 12 have 31
# Month 2 has 28, years divisible by 4, 29

d = 0
nd = 0
m = 1
w = 1
o = 0
y = 0
x = [d, m, w, o, y]

while y < 100:
    if m == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        nd = 31
    elif m == 4 or 6 or 9 or 11:
        nd = 30
    elif m == 2:
        if y % 4 == 0:
            nd = 29
        else:
            nd = 28
    for i in range(1, nd):
        d = i
        w += 1
        if w == 8:
            w = 1
        if d == 1 and w == 1:
            o += 1
    m += 1
    if m == 13:
        m = 1
        y += 1

print(o)
