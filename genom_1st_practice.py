genom = input()
G = 0
C = 0
all = len(genom)
for a in genom:
    if a == 'g' or a == 'G':
        G += 1
for b in genom:
    if b == 'c' or b == 'C':
        C += 1
print((G + C) / all * 100)

        