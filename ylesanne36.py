def kahend(n):
    kstr = ''
    if n == 0:
        return '0'
    while n > 0:
        kstr = str(n % 2) + kstr
        n = n >> 1
    return kstr

def kasPalindroom(s):
    s = str(s)
    if s == s[::-1]:
        return True
    return False

summa = 0

for i in range(0, 1000000):
    if kasPalindroom(i) and kasPalindroom(kahend(i)):
        summa += i

print summa
