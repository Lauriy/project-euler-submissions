kuudep2evad = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
n2dalap2ev = 2
arv = 0

def kasLiigaasta(n):
    if n % 400 == 0:
        return True
    elif n % 4 == 0:
        return True
    else:
        return False

for i in range(1901, 2001):
    print i
    if kasLiigaasta(i) == True:
        kuudep2evad[1] = 29
    else:
        kuudep2evad[1] = 28
    for a in kuudep2evad:
        for j in range(1, a + 1):
            if n2dalap2ev > 7:
                n2dalap2ev = 1
            if n2dalap2ev == 7 and j == 1:
                arv += 1
                n2dalap2ev += 1
            else:
                n2dalap2ev += 1


print arv


        
    
    
