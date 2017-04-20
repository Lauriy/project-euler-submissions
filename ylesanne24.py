def permutations(li):
    if len(li) <= 1:
        yield li
    else:
        for el in li:
            for p in permutations([e for e in li if not e == el]):
                yield [el] + p

loendur = 0

for p in permutations('0123456789'):
    loendur += 1
    if loendur == 1000000:
        print p
