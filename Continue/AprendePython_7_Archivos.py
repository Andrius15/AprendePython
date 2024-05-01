# Vamos a aprender a abrir, leer y editar archivos
# Solo lo txt. El resto por tu cuenta.

# De normal, el archivo se guarda en una variable
# Se usa open() y hay varios modos de abrir un archivo
# Si el archivo no existe, se creara (siempre que el modo sea escritura)

# Abrimos el archivo (y lo creamos si no lo tenemos)
f = open('AprendePython\Continue\Ejemplo.txt', 'w')
# Primero el nombre del archivo (y/o su path), despues el modo.
# w para write (solo escritura, borra todo lo que tenia el archivo)
# r para read (solo lectura)
# r+ (escritura y lectura)
# a append (annade a lo que tenia el archivo)

f.write('Hola')
# Si estas en consola, aunque entres ahora en el archivo no encontraras nada

f.close()
# Ahora si veras que se ha guardado
# Es importante cerrar los archivos para poder guardarlos

# Pero si no queremos escribir el close(), hay otra forma que lo hace solo:

with open('AprendePython\Continue\Ejemplo.txt', 'r+') as g: # De esta forma, cuando termine de ejecutarse, se cierra solo
    # Vamos a aprender a hacer unas cuantas cosas

    # Pongamos cosas en el archivo:
    g.write('Adios')
    text = g.readline()
    print(text) # >>>Hola
    text2 = g.readline()
    print(text2) #>>>
    

# Si ahora entras en el archivo, veras que dice: 'HolaAdios'
# Esto es muy delicado. Recomiendo las pruebas y la experimentacion
# Pero, en resumen:
# Al leer y escribir, se utilizan 'cursores' como los que utilizas tu
# De esta forma, al leer, lo que ya has leido no se vuelve a leer
# Quedan mas conceptos, asi que hagamoslo rapido:
# Para hacerlo rapido:

"""
read() # Guarda todo el texto de una sola vez.
readline() # Lee una linea a la vez. El cursos se mueve.
readlines() # Lee todas las lineas a la vez.
write() # Escribe donde este el cursor.
seek(offset, whence=0) # Cambia el cursor
# Esta ultima funcion requiere 2 argumentos:
# Mueve el cursor esa cantidad de posiciones respecto a whence. 0 es el inicio del archivo
"""


# Ejemplo que puede ser interesante
with open('AprendePython\Continue\Carta.txt', 'w') as c:
    nombre = input('Tu nombre:')
    edad = input('Tu edad:')
    c.write(f'Hola {edad}, tienes {nombre} annos')

# Y ya esta. Eso es mas o menos todo lo necesario
# El resto es logica, practica y recordar comprobar que no hay errores