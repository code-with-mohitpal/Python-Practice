def primes(n):
    res = []
    for num in range(2, n+1):
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            res.append(num)
    return res

print(primes(20))
