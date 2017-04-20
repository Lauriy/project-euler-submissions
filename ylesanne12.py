from operator import mul

def kysiAlgarvulineKordaja(n):
    a = 2
    while True:      
        if(n % a == 0):
            return a
        else:
            a += 1

def kysiAlgarvulisedKordajad(n):
    kordajad = []
    while(n != 1):
        a = kysiAlgarvulineKordaja(n)
        kordajad.append(a)
        n = n / a
    return kordajad

n = 2
mitu = 2
Tn = 0

while True:
    Tn = (n * (n + 1)) / 2
    algarvkordajad = kysiAlgarvulisedKordajad(Tn)
    loendur = []
    while len(algarvkordajad) != 0:
        loendur.append(algarvkordajad.count(algarvkordajad[0]))
        del algarvkordajad[:loendur[-1]]
    k6ikkordajad = reduce(mul, [loendur[i] + 1 for i in range(len(loendur))])
    mitu = max(k6ikkordajad, mitu)
    if(mitu >= 500):
        break
    n += 1

print Tn
    


        
