# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
n = int(input("enter natural numbers "))
difference = (n * (n +1) * (n-1) * (3*n + 2)) / 12
print(difference)
