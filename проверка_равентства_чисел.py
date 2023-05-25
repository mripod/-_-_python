a, b, c = int(input()), int(input()), int(input())
if a <= b <= c:
    print(c, '\n', a, '\n', b)
elif b <= a <= c:
    print(c, '\n', b, '\n', a)
elif c <= a <= b:
    print(b, '\n', c, '\n', a)
elif c <= b <= a:
    print(a, '\n', c, '\n', b)
elif a <= c <= b:
    print(b, '\n', a, '\n', c)
elif b <= c <= a:
    print(a, '\n', b, '\n', c)