# Obtener todos los numeros de una lista multiplicados al cuadrado

my_list = [i for i in range(10)]

# Usando Def
def get_squares(arr):
    squares = []
    for n in arr:
        squares.append(n * n)
    return squares

# Usando List Comprehension
squares = [n * n for n in my_list]

# Usando Map
squares_map = list(map(lambda x: x*x, my_list))
print(squares_map)