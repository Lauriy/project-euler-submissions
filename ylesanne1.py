arv = 999

def arvJagatav(n):
    p = arv / n
    return (n * (p * (p + 1))) / 2

print arvJagatav(3) + arvJagatav(5) - arvJagatav(15)
