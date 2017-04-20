arvud = set()

for a in range(2, 101):
    for b in range(2, 101):
        arvud.add(a**b)

print len(arvud)
