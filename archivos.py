def read():
    numbers = []
    with open('./archivos/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Facundo", "Miguel", "Pepe", "Christian", "Rocío", "Castaño"]
    with open('./archivos/names.txt', 'a', encoding = 'utf-8') as f:
        for names in names:
            f.write(names)
            f.write("\n")

def run():
    write()

if __name__ == '__main__':
    run()