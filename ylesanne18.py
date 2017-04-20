f = open('kolmnurk.txt')

read = []

for rida in f:
    read.append([int(x) for x in rida.split()])

def v2hendaKolmnurk(k):
    viimanerida = k[-1]
    for i in xrange(len(k) - 1):
        k[-2][i] += max(viimanerida[i:i +2])
    del k[-1]

def leiaMaksimaalneTeekond(k):
    while len(k) > 1:
        v2hendaKolmnurk(k)
    return k[0][0]

print leiaMaksimaalneTeekond(read)




