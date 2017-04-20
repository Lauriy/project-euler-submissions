def kasOnPalindroom(n):
    s6na = str(n)
    tagurpidi = s6na[::-1]
    if(s6na == tagurpidi):
        return 1

def leiaSuurim():
    kolmekohalisedarvud = []
    maksimaalne = 0
    for i in range(0,1000):
        kolmekohalisedarvud.append(i)
    for esimenearv in kolmekohalisedarvud:
        for teinearv in kolmekohalisedarvud:
            if (kasOnPalindroom(esimenearv * teinearv) == 1):
                if(esimenearv * teinearv > maksimaalne):
                    maksimaalne = esimenearv * teinearv
    return maksimaalne


print leiaSuurim()
