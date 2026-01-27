import math

right = int(input("Enter the number of right moves: "))
down = int(input("Enter the number of down moves: "))

routes = math.comb(right + down, down)
print(routes)
