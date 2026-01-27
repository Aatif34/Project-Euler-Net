n = int(input("Enter the power: "))
num = 2 ** n

digit_sum = 0
while num > 0:
    digit_sum += num % 10
    num = num // 10

print(digit_sum)
