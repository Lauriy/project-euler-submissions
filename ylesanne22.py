f = open("nimed.txt","r")
read = f.readline()
f.close()

algne = read.split(",")
algne.sort(key = str.lower)

nimed = []

for nimi in algne:
    nimi = nimi.strip('"')
    nimi.lower()
    nimed.append(nimi)
    
kaalud = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
loendur = 0
kaal = 0
summa = 0

for nimi in nimed:
    nimi = list(nimi)
    kaal = 0
    for t2ht in nimi:
        kaal += kaalud[t2ht.lower()]
    summa += kaal * (loendur + 1)
    loendur += 1
    
print summa
