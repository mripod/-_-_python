n = int(input())
n10 = n % 10
one = 'программист'
two = 'программиста'
four = 'программистов'
if n10 == 0 or n10 >= 5:
    print(n, four)
elif 9 < n < 21 or 109 < n < 121 or 209 < n < 221 or 309 < n < 321 or 409 < n < 421 or 509 < n < 521 or 609 < n < 621 or 709 < n < 721 or 809 < n < 821 or 909 < n < 921:
    print(n, four)
elif n10 == 1:
    print(n, one)
elif 1 < n10 < 5:
    print(n, two)

