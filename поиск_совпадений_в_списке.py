lst = [int(i) for i in input().split()]
x = int(input())
indexes = []
if x not in lst:
    print('Отсутствует')
else:
    for i in range(len(lst)):
        if lst[i] == x:
            indexes.append(i)
print(*sorted(indexes))






