symbol = input()
key = input()
original = input()
uncoding = input()
for i in original:
    index = symbol.find(i)
    if index != -1:
        print(key[index], end = '')
print()
for j in uncoding:
    index = key.find(j)
    if index != -1:
        print(symbol[index], end = '')
