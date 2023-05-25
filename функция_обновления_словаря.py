def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif d.get(key*2) is not None:
        d[key*2].append(value)
    else:
        d[key *2] = [value]

d = {}
print(update_dictionary(d, 1, -3))
print(d)

