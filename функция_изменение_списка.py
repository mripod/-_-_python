def modify_list(l):
    for i in range(len(l) -1, -1, -1):
            if l[i] % 2 != 0:
                del l[i]
            else:
                l[i] = int(l[i] / 2)
    return l


l = [int(i) for i in input().split()]
print(*modify_list(l))