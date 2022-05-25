# Suma todos los valores de una lista

from functools import reduce

my_list = [i for i in range(10)]
# Usando def
def get_sum(arr):
    result = 0
    for n in arr:
        result += n
    return result

# Usando Reduce
sum = reduce(lambda a, b: a + b, my_list)
print(sum)