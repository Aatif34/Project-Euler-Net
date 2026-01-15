# what is the 10 001st prime number?


count = 0
n = 2

while count < 10001:
    is_prime = True

    for i in range (2, int(n**0.5)+1):
        if n % i == 0:
            is_prime = False
            break
        
    if is_prime:
        count += 1
    n += 1

print(n - 1)