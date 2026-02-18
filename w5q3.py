import numpy as np

arr = np.arange(1, 101)

primes = []
for n in arr:
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                break
        else:
            primes.append(n)

print(np.array(primes))
