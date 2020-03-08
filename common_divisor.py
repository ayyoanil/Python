import time
start_time = time.time()

from math import gcd
a, b = map(int, input().split())

max_num = max(a, b)
min_num = min(a, b)

if max_num % min_num == 0:
    gcd_common_divisor = min_num
else:
    gcd_common_divisor = gcd(a, b)

count = 1

for number in range(2, gcd_common_divisor + 1):
    if gcd_common_divisor % number == 0:
        count += 1
print(count)

print("--- %s seconds ---" % (time.time() - start_time))