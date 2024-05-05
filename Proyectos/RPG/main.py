# Aqui, en main.py, ejecutaremos el juego
# Todos los demas archivos seran codigo que sera importado
# Utilizare un sistema de enumeracion, pero esto sera un poco desastre
# Desde ahora aviso que daremos muchas vueltas, y no numerare lo que este en la misma seccion
# Pero te aseguro que me he tomato mi tiempo. Tometa tu el tuyo
# Empezando desde 0, vamos a pensar lo que queremos hacer
# Yo quiero hacer un sistema donde puedes elegir la clase y hay armas
# Combate por turnos, un ataque y una magia
# Pues empezemos a crear
# ==1== creare un sistema basico de inputs y outputs
# Tambien creare varios archivos para manejar esto
# En este momento puedes ir a logic.py
from logic import show_text, ask_player, interfaz

# ==4==
def main(): # La funcion que ejecuta el juego. Puedes llamarla como quieras
    while True:
        show_text(**interfaz) # Imprimimos los datos para el usuario
        action = ask_player(text='Accion:') # Le pedimos que haga algo
        if action.lower() == 'salir': # Si pide salir, pues se sale
            break
        else:
            interfaz['Ultima accion'] = [action] # Si no, se imprime lo ultimo que hizo

if __name__ == '__main__':
    # De esta forma, si por alguna razon quieres importar todo este proyecto,
    # no se ejecutara. El codigo solo se ejecuta si lo haces expresamente (desde consola por ejemplo)
    main()