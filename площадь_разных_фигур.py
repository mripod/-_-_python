S = input()
if S == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c)/2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif S == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(a * b)
elif S == 'круг':
    a = int(input())
    pi = 3.14
    print(pi * a ** 2)