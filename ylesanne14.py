max = 0
otsitav = 0

for i in range(2,1000000):
    number = i
    mitu = 0
    while number != 1:
        if(number % 2 == 0):
            number = number / 2
        else:
            number = 3 * number + 1
        mitu += 1
    if mitu > max:
        max = mitu
        otsitav = i

print max
print otsitav
