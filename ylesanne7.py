def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

j = 2
i = 0

while 1:
    if(isprime(j) == True):
        i += 1
    j += 1
    if(i == 10001):
        break

print j - 1
    
    
    
