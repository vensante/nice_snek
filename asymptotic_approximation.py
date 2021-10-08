n = int(input())

from math import log

total = 0

for i in range (1, n + 1):
    num = 1 / i
    total = total + num

print(total - log(n))
