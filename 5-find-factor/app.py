import math
def optimized_factor_count(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        # check for factors
        if n % i == 0:
            if i == n/i:
               count += 1
            else:
               count += 2
    return count

print(optimized_factor_count(36))