astendatud = []
kogusumma = 0

for i in range(2, 354295):
    summa = 0
    for j in str(i):
        summa += int(j)**5
    if summa == i:
        astendatud.append(i)

for a in astendatud:
    kogusumma += a

print astendatud
print kogusumma
        
