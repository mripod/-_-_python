n = int(input())
x = 0
s = [0, 0]
while x < n:
    cmd = input().split()
    x += 1
    for i in range(len(cmd)):
        if 'север' in cmd[i]:
            s[1] += int(cmd[i+1])
        elif 'запад' in cmd[i]:
            s[0] -= int(cmd[i+1])
        elif 'юг' in cmd[i]:
            s[1] -= int(cmd[i+1])
        elif 'восток' in cmd[i]:
            s[0] += int(cmd[i+1])
    print(*s)    