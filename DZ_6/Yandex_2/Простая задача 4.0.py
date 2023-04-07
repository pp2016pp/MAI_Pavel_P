def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

numbers = input().split('; ')
numbers = list(map(int, numbers))

n = len(numbers)
mutually_primes = {x: [] for x in numbers}

for i in range(n):
    for j in range(i + 1, n):
        if gcd(numbers[i], numbers[j]) == 1:
            mutually_primes[numbers[i]].append(numbers[j])
            mutually_primes[numbers[j]].append(numbers[i])

for num in numbers:
    primes = " ".join(str(x) for x in mutually_primes[num])
    if primes != "":
        print("{} - {}".format(num, primes))

