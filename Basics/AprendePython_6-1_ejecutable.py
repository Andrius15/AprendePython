import mates.ecu as ecu


if __name__ == '__main__':
    import sys
    MimCMul = ecu.MCM(*map(lambda x: int(x), sys.argv[1:]))
    print(MimCMul)

# Ahora explico:
# Si en consola vamos a la direccion de este archivo
# Y ponemos en la consola:
# >python AprendePython_6-1_ejecutable.py 5 7 8 2 65
# Como resultado sale:
"""
36400.0
"""
# Explicacion a produndidad
"""
if __name__ == '__main__': # Esto comprueba si se esta ejecutando directamente o si se importa
                             Por lo general, se usa mucho para poner dentro lo que se quiera ejecutar,
                             mientras fuera se deja las funciones y variables por si se quiere importar

    import sys # Importar el modulo sys


    MimCMul = ecu.MCM(*map(lambda x: int(x), sys.argv[1:])) # Guardamos en una variable lo siguiente:
    # ecu.MCM(*map(lambda x: int(x), sys.argv[1:]))
    # ecu.MCM es la funcion del minimo comun multiplo del paquete    
    # *map(lambda x: int(x), sys.argv[1:]) 
    # La * es para desempaquetar la funcion map
    # El lambda convierte los str de sys.argv en int (porque sys te da str)
    # sys.argv es una lista con todo lo que has puesto en la consola desde el python,
    # es decir, una lista con: ['AprendePython_6-1_ejecutable.py', '5', '7', '8', '2', '65']
    # Por lo que sys.argv[1:] nos da todos los numeros
    # map usa lambda para transformar esos str en int
    # ecu.MCM hace el minimo comun multiplo
    # que se guarda en la variable MimCMul

    print(MimCMul) # Esto se explica solo
"""
# De esta forma, ya sabes utilizar paquetes
# Crearlos
# Si buscas en internet/documentacion, descargarlos y distribuirlos
# Y ya sabes crear archivos que se ejecutan desde consola directamente
# Ya estas completamente losto para AprendePython_Interludio