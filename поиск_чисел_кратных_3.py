a, b = (int(i) for i in input().split())
qnt = 0
sum = 0
while a % 3 != 0:
    a += 1
for i in range(a, b + 1, 3):
    sum += i
    qnt = len(range(a, b + 1, 3))
print(sum/qnt) 