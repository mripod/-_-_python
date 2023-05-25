waw = input().lower().split()
word_counter = {}
for i in waw:
    if i in word_counter:
        word_counter[i] += 1
    else:
        word_counter[i] = 1
for key, value in word_counter.items():
    print(key, value)
    