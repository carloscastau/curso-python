# Dada una lista de numeros filtra para quedarte solo con los números impares

my_list = [i for i in range(10)]

# Usando def
def get_odds(arr):
    odds = []
    for n in arr:
        if n % 2 == 1:
            odds.append(n)
    return odds

# Usando List Comprehension
odds = [n for n in my_list if n % 2 == 1]

# Usando Filter
odds_filter = list(filter(lambda n: n % 2 == 1, my_list))
print(odds_filter)