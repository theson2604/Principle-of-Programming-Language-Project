def power(exp):
    return lambda x: pow(x, exp)

square = power(2)
cube = power(3)

print(square(5))
print(cube(5))
