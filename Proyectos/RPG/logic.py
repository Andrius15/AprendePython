import os, time
from errors import *
from utilities import *

# ==2==
# Un diccionario para el print
interfaz : dict= {
    'decoration': '=', # Para delimitar el cuadro de texto
    'between': '-', # Para separar secciones
    'character': ['Tu'], # Eventualmente esto tendra sentido
    'data': ['Nada que declarar'], # Lo extra que querramos decir
    'Ultima accion': ['None'] # Lo ultimo que se hizo
}

# Creare una funcion para mostrar texto de forma comoda
def show_text(**lines) -> None: # Se utiliza el diccionario de arriba
    os.system('cls') # Borramos para mantener la pantalla limpia
    # Preparar la decoracion
    size = count_max(lines) # Puedes ir a utilities.py
    decoration = lines['decoration'] * size
    between = lines['between'] * size

    print(decoration)
    for i in lines:
        if i == 'decoration' or i == 'between': # Para no mostrar esto como un dato por si solo
            continue
        
        print('>', i.title(), end=':\n') # Para especificar que es lo que se dice
        print('\n'.join(lines[i]))

        if tuple(interfaz.keys()).index(i) == len(interfaz)-1: # Para que lo ultimo sea '=' y no '-'
            print(decoration)
        else: # Pero entre tipos de datos, se utiliza '-'
            print(between)

# Tambien creare una funcion para pedirle algo al usuario
def ask_player(*, answer_type = str, text : str = '=>') -> int | str: # Fuerzo a que se especifiquen los argumentos
    answer : int | str
    while True: # Haremos un bucle
        try:
            answer = input(text).title() # El usuario da inputs segun tu mensaje
            if answer_type == int: # Si se supone que es un int, lo convierte
                answer = int(answer)
            if answer == '':
                raise NothingError
        except ValueError: # Si el dato se supone que es un int, pero no, lo intenta de nuevo
            print('Deberias introducir un numero')
        except NothingError: # Puedes ir a errors.py
            print('Deberias escribir algo')
        else: # Esto no se ejecuta hasta que no hayan errores
            break
        time.sleep(2)
        show_text(**interfaz)
    return answer # Por lo que solo se llega aqui cuando el usuario introduce el valor que deberia

# Puedes volver a main.py