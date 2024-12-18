def big_of_two(x, y):
    if x > y:
        return x
    if x < y:
        return y

def big_of_three(z, big_of_two):
    if z > big_of_two:
        return z
    if z < big_of_two:
        return big_of_two


print(big_of_three(5, big_of_two(1,3)))


