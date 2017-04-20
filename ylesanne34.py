def faktoriaal(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    elif n == 4:
        return 24
    elif n == 5:
        return 120
    elif n == 6:
        return 720
    elif n == 7:
        return 5040
    elif n == 8:
        return 40320
    elif n == 9:
        return 362880

summa = 0

for i in range(3, 100000):
    istr = str(i)
    tulemus = 0
    for symbol in istr:
        tulemus += faktoriaal(int(symbol))
    if tulemus == i:
        summa += i

print(summa)
