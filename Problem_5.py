# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?

for i in range (20,10000000000000000,20):
    for j in range(1,21):
        if i % j != 0:
            break
    else:
        print(i)
        break

    