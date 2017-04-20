summa = 200
myndid = [1,2,5,10,20,50,100,200]
mitu = [1] + [0] * summa

for mynt in myndid:
    for i in range(mynt, summa + 1):
        mitu[i] += mitu[i - mynt]

print mitu[summa]
