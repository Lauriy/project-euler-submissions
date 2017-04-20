from math import sqrt

n = 165

def kasPentagonaalne(n):
    p = (sqrt(1 + 24 * n) + 1) / 6
    return p == int(p)

while True:
    a = n * (2 * n - 1)
    if(kasPentagonaalne(a) == True):
        break
    n += 1

print a

        
        
