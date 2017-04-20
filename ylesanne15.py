def faktoriaal(n):
     if n == 0:
         return 1
     else:
         return n * faktoriaal(n-1)

print faktoriaal(40) / (faktoriaal(20) * faktoriaal(20))
