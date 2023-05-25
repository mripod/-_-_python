numbers = []
sum_ = 0

while True:
    n = input()
    numbers.append(int(n))
    sum_ += int(n)
    if sum_ == 0:
        break

sum_sq = sum([num**2 for num in numbers])
print(sum_sq)
