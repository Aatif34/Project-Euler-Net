largest_palindrome = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        product = i*j

        if product <= largest_palindrome:
            break
        if str(product) == str(product)[::-1]:
            largest_palindrome = product

print(largest_palindrome)
