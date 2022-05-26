import os 
import random 

replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )

def read_words():
     with open('./archivos/data.txt', 'r', encoding='utf-8') as f:
        # strip() Devuelve una copia de la cadena con los espacios en blanco iniciales y finales eliminados.
        list_words = [word.strip().upper()for word in f]
        choosen_word = list_words[random.randint(0, len(list_words))]
        #Elimina el problema de los caracteres especiales        
        for a, b in replacements:
            choosen_word = choosen_word.replace(a, b).replace(a.upper(), b.upper())
        return choosen_word


def game(magic_word, letter, game_word):
    if letter in magic_word:
        for i in range(len(magic_word)):
             if letter == magic_word[i]:
                 game_word[i] = letter
    return ' '.join(game_word)
    

def run():
    
    lives = 6
    letter = ''
    magic_word = read_words()
    game_word = ['_' for i in range(len(magic_word))]
    
    
    while lives > 0:
        os.system('clear')
        print('''
        ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
        ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
        ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
        ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
        ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
        ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                            ¡Adivina la palabra!
        ''')
        print(f'Vidas restantes: {"❤" * (lives)}')
        print('¡Adivina la palabra!')
        print(game(magic_word, letter, game_word))
        try:
            if len(letter) > 1:
                raise ValueError('Solo puedes ingresar una letra')
            else:
                if game(magic_word, letter, game_word).count('_') > 0:
                    if letter in game(magic_word, letter, game_word):
                        letter = input('Escoge una letra: ').upper()
                    else:
                        lives -= 1 
                        if lives > 0:
                            os.system('clear')
                            print('''
        ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
        ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
        ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
        ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
        ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
        ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                            ¡Adivina la palabra!
                            ''')                    
                            print(f'Vidas restantes: {"❤" * (lives)}')
                            print('¡Adivina la palabra!')
                            print(game(magic_word, letter, game_word))
                            letter = input('Escoge una letra: ').upper()
                        else:
                            os.system('clear')
                            print('''
        ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
        ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
        ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
        ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
        ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
        ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                            ¡Adivina la palabra!
                            ''')  
                            print('¡Te quedaste sin vidas!\nJuego terminado...\n')
                            print('La palabra era: ' +magic_word)
                else:
                    print('''
         ██████╗  █████╗ ███╗   ██╗ █████╗ ██████╗  ██████╗ ██████╗ 
        ██╔════╝ ██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔═══██╗██╔══██╗
        ██║  ███╗███████║██╔██╗ ██║███████║██║  ██║██║   ██║██████╔╝
        ██║   ██║██╔══██║██║╚██╗██║██╔══██║██║  ██║██║   ██║██╔══██╗
        ╚██████╔╝██║  ██║██║ ╚████║██║  ██║██████╔╝╚██████╔╝██║  ██║
         ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝                                    
                    ''')
                    break

        except ValueError as ve:
            return print(ve)


if __name__ == '__main__': run()
# Notas finales por revisar:
# Investiga la función enumerate (documentacion)
# El método get de los diccionarios te puede servir
# Dibuja el ahorcado con el codigo ascii y dibujar en pantalla
# # Mejora la interfaz, emojis