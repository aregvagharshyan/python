import math
def calculate_perimeter(shape = 'Circle', *sides):
    match shape:
        case 'Rectangle':
            if len(sides) != 2:
                raise ValueError("Rectangle requires exactly two sides.")
            length = sides[0]
            width = sides[1]
            perimeter_of_rectangle = 2 * (length + width)
            print(f'Perimeter of Rectangle: {perimeter_of_rectangle}')
        case 'Square':
            if len(sides) != 1:
                raise ValueError("Square requires exactly one side.")
            side_of_square = sides[0]
            perimeter_of_square = 4 * side_of_square
            print(f'Perimeter of Square: {perimeter_of_square}')
        case 'Triangle':
            if len(sides) != 3:
                raise ValueError("Triangle requires exactly three sides.")
            side_1 = sides[0]
            side_2 = sides[1]
            side_3 = sides[2]
            perimeter_of_triangle = side_1 + side_2 + side_3
            print(f'Perimeter of Triangle: {perimeter_of_triangle}')
        case 'Circle':
            if len(sides) != 1:
                raise ValueError("Circle requires exactly one radius.")
            radius = sides[0]
            perimeter_of_circle = 2 * math.pi * radius
            print(f'Perimeter of Circle: {perimeter_of_circle}')
calculate_perimeter('Circle', 3)
calculate_perimeter('Rectangle', 2, 5)
calculate_perimeter('Square', 7)
calculate_perimeter('Triangle', 1, 4, 7)




















