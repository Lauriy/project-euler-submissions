s6nastik = {
            0: 'zero',
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen',
            20: 'twenty',
            30: 'thirty',
            40: 'forty',
            50: 'fifty',
            60: 'sixty',
            70: 'seventy',
            80: 'eighty',
            90: 'ninety',
            100: 'hundred',
            1000: 'onethousand'
           }

def t88tleNumber(n):
    global s6nastring
    if n in s6nastik:
        if n == 100:
            s6nastring += 'onehundred'
            return s6nastring
        s6nastring += s6nastik[n]
        return s6nastring
    elif n % 100 == 0:
        m = n // 100
        s6nastring += s6nastik[m]
        s6nastring += s6nastik[100]
        return s6nastring
    elif n > 100 and n < 1000:
        m = n // 100
        s6nastring += s6nastik[m]
        s6nastring += s6nastik[100]
        s6nastring += 'and'
        n = n - m * 100
        t88tleNumber(n)
    elif n > 20 and n < 100:
        m = (n // 10) * 10
        s6nastring += s6nastik[m]
        n = n - m
        t88tleNumber(n)
    return s6nastring

s6nastring = ''
loendur = 0

for i in range(1,1001):
    s6nastring = ''
    loendur += len(t88tleNumber(i))
    #print t88tleNumber(i)

print loendur


    
    
        

        
        
    

