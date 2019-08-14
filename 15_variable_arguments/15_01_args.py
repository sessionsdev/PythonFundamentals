'''
Write a script with a function that demonstrates the use of *args.

'''


cubes = []

def cubed_numbers(*args):
    for n in args:
        n += n**3
        cubes.append(n)


cubed_numbers(1, 2, 3, 4, 5, 6, 7, 8)
print(cubes)
