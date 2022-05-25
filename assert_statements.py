def divisors(num):
    # try:
    #     if num < 0 or num == 0:
    #         raise ValueError('Ingresa un número positivo') 
        divisors = [i for i in range(1, num+1) if num % i == 0]
    # divisors = []
    # for i in range(1, num + 1):
    #     if num % i == 0:
    #         divisors.append(i)
        return divisors
    # except ValueError as ve:
    #     print(ve)
    #     return False

def run():
        num = (input('Ingresa un número: '))
        assert num.isnumeric() and int(num) > 0 and int(num) == 0, 'Ingresa solo numeros positivos diferentes a 0 o un número' 
        print(divisors(int(num)))
        print("Terminó mi programa")

if __name__ == '__main__':
    run()