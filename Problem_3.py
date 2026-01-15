# What is the largest prime factor of the number 600851475143

n = int(input("Enter any integer: "))
largest = 0
while n % 2 == 0:
    largest = 2
    n //= 2

factor = 3
while factor * factor <= n:
    if n % factor == 0:
        largest = factor
        n //= factor
    else:
        factor += 2
if n > 1:
    largest = n

print(largest)
