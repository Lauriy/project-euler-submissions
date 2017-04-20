esimene = 1
teine = 1
fibonacciarv = 0
i = 2

while len(str(fibonacciarv)) < 1000:
    fibonacciarv = esimene + teine
    esimene = teine
    teine = fibonacciarv
    i += 1

print i
