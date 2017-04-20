# -*- coding: cp1252 -*-

def kasAlgarv(number):  
    if number <= 1 or number %2 ==0:  
        return 0  
    check = 3  
    maxneeded = number  
    while check < maxneeded + 1:  
        maxneeded = number / check  
        if number % check == 0:  
            return 0  
        check += 2  
    return 1  

n = 0
arv = 0
maksimum = 0
liige1 = 0
liige2 = 0
kasEdasi = 1

for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        while (kasEdasi == 1):
            arv = (n**2 + a*n + b)
            if(kasAlgarv(arv) == 1):
                n += 1
            else:
                kasEdasi = 0
        if n > maksimum:
            maksimum = n
            liige1 = a
            liige2 = b
        kasEdasi = 1
        
print liige1 * liige2



        
        
        
        
