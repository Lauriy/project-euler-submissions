from math import sqrt

numbrid = set()
summa = 0

def jagajateSumma(n):
    s = 1
    t = sqrt(n)
    for i in range(2, int(t) + 1):
        if n % i == 0:
            s += i + n / i
    if t == int(t):
        s -= t
    return s

for i in range(1, 20162):
    if i < jagajateSumma(i):
        numbrid.add(i)
    if not any((i - a in numbrid) for a in numbrid):
        summa += i

print summa



            
    


        


    
    
    
