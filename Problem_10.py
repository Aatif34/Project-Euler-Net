# Find the sum of all the primes below two million.

total = 0
n = 2

while n < 2000000:
    is_prime = True

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        total += n
    n += 1

print(total)
        
