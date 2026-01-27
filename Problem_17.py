from num2words import num2words

a = 0

for i in range (1, 1001):
    word = num2words(i)
    a += len(word) - word.count("-") - word.count(" ")

print(a)

