from math import sqrt

arv = 0

def leiaJagajateSumma(n):
    s = 1
    t = sqrt(n)
    for i in range(2, int(t) + 1):
        if n % i == 0:
            s += i + n / i
    if t == int(t):
        s -= t
    return s

for i in range(2, 10000):
    a = leiaJagajateSumma(i)
    b = leiaJagajateSumma(a)
    if a > i and b == i:
        arv += a + i

print arv


        


    
    
    
