faktoriaal = 1

for i in range(1,101):
    faktoriaal *= i

faktoriaal = str(faktoriaal)

s = 0

for a in faktoriaal:
    s += int(a)

print s
