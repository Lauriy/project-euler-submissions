def onKolmik(a, b, c):
    if(c**2 == a**2 + b**2):
        return True
    return False

for a in range(0,1000):
    for b in range(0,1000):
        for c in range(0,1000):
            if(a + b + c == 1000):
                if(onKolmik(a, b, c) == True):
                    print a, b, c
