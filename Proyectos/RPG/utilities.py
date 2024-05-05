# ==3==
# Esta funcion cuenta los caracteres del str mas largo que vayamos a mostrar
# He creado una funcion entera porque un max(map(lambda x: len(x), lines)) no daba para todos los casos
def count_max(dictionary : dict | list) -> int: # Como lo quiero hacer generica, hago que soporte ambos tipos
    if type(dictionary) == dict: # Pero paso los dict a list para manejarlos todos igual
        dictionary = list(dictionary.values())
    
    dictionary2 : list = [] # Una lista con las longitudes de los distintos str
    for i in dictionary:
        if type(i) == list: # Las listas dentro de la lista
            # Recordemos que casi todo lo estamos guardando en listas
            for o in i:
                dictionary2.append(len(o))
        else:
            dictionary2.append(len(i))

    return max(dictionary2) # Devuelve el valor mas alto
# Puedes volver a logic.py