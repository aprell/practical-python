# Exercise 1.5

def bounce(height):
    return 3/5 * height

height = 100

for i in range(1, 11):
    height = bounce(height)
    print(i, round(height, 4))
