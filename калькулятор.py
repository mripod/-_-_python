A = float(input())
B = float(input())
C = input()
if B == 0 and (C == '/' or C == 'mod' or C == 'div'):
    print('Деление на 0!')
elif C == '+':
    print(A + B)
elif C == '-':
    print(A - B)
elif C == '/':
    print(A / B)
elif C == '*':
    print(A * B)
elif C =='mod':
    print(A % B)
elif C == 'pow':
    print(A ** B)
elif C == 'div':
    print(A // B)

