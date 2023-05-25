n = int(input())
first3 = n  // 1000
n1 = first3 // 100
n2 = first3 // 10 % 10
n3 = first3 % 10
last3 = n % 1000
n4 = last3 // 100
n5 = last3 // 10 % 10
n6 = last3 % 10
if (n1 + n2 + n3) == (n4 + n5 + n6):
    print('Счастливый')
else:
    print('Обычный')
