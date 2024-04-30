# Recomiendo archivo, pero puedes combinar archivo y consola segun convenga
# Yo lo hare en consola

# Empezamos fuerte
# Recuardas en el segundo el while?
a, b = 0, 1
while a <10:
  print(a)
  a, b = b, a+b
# Pues ahora lo vamos a mejorar y explicar un poco

a, b = 0, 1
# Esto tiene mas profundidad, pero por ahora te dire lo importante
# Puedes declarar varias variables de una sola vez
# Se llama desempaquetar
# Como tenemos 2 variables para guardar y declaramos 2 valores,
# python entiende que queremos hacer:
# a = 0
# b = 1

while a < 10: # Esto ya sabes porque es
  print(a, end = '') # Lo entiendes, no?
  a, b = b, a + b # Lo mismo que al principio, pero lo que hacemos es intercambiar valores sobre la marcha
  # No podriamos hacerlo en separado usando solo 2, porque estariamos cambiando la variable que necesiamos por otra

  if not a < 10: continue
  print(',', end = '')
else:
  print()
# Esto ultimo hace que el ultimo numero no tenga la coma (,)
# El not y usar la misma expresion DESPUES de lo que cambia la variable garantiza que,
# si es la ultima vez que se ejecuta el while, no se ejecute lo de debajo del continue
# Tecnicamente el else sobra aqui, pero ahora veras porque hay que acostumbrase a eso

def fib():
  a, b = 0, 1
  while a < 10:
    print(a, end='')
    a, b = b, a + b
    if not a < 10: continue
    print(',', end = '')
  else:
    print()
# Poner esto (ya sea en consola o archivo) no te dira nada
# Pero ahora pon esto:
fib()
# Si es en consola, ya salio
# Si es archivo, veras que cuantas mas veces pongas la funcion, mas veces saldra los numeros
# Si no hubieramos puesto el else, seria dificil ver si el print esta en la funcion, el while o de normal

# //////////////////////////////////////////////

# Ahora algo un pelin mas util, y mas complejo, por supuesto
# Trabajaremos sobre lo que ya tenemos

def fib(n : int = 10) -> None:
  a, b = 0, 1
  while a < n:
    print(a, end='')
    a, b = b, a + b
    if not a < n: continue
    print(',', end = '')
  else:
    print()
# Hay pocas diferencias, pero las 2 que hay son clave

# La primera: los (: int) y el (-> None)
# Esto se usa para poder determinar de un vistazo el tipo de dato que se usa
# Ademas, VS deberia ser capaz de mostrarte el tipo de dato si escibes fib(|)
# \\\ La barrita (|) es el cursor \\\
# Veras que pide un int
# Si pusieras un str, dara error
# Esto sera util cuando, tras mucho tiempo, revisas tu codigo
# O si otro lo usa
# Esto evita los TypeError por parte del humano (el 25-30 %)
# El (-> None) es lo mismo, pero para la funcion
# Igual que int() devuelve un enetro,
# .append() no devuelve nada, solo hace cosas
# (-> None) es la forma de decir "Esto solo hace cosas, no devuelve nada"

# La segunda diferencia es el (n : int = 10)
# Si ahora pones
fib()
# >>>0,1,1,2,3,5,8
# Pero si pones
fib(7)
# >>>0,1,1,2,3,5
fib(50)
# >>>0,1,1,2,3,5,8,13,21,34
# Lo que estamos haciendo es pasar 50 como n
# El (n : int = 10) significa:
# Dame un numero (n) de tipo entero (: int)
# Si no me lo das, asumire que es 10 (n = 10)
# Si quitamos el (= 10) daria error y nos pediria dar el numero


# Ahora, por que no creamos una funcion que devuelva cosas?
def multiplayer(n1 : int, n2 : int) -> int:
  return n1 * n2
# Ahora esto es una funcion que devuelve enteros
# ! NO imprime nada en pantalla
# Si lo ejecutas en VS veras que no sale nada
# Esto lo que hace es devolver un valor, de forma que podemos guardarlo
a = multiplayer(3, 4)
print(a)
# >>>12
# De la misma forma que hasta ahora, el return devuelve lo que le digas que devuelva
# Ten en cuenta que el return es como el break: si se ejecuta, se salta todo lo de abajo


# Otra cosa es que las funciones son tecnicamente variables
a = multiplayer
multiplayer = fib
fib = 0
multiplayer(7)
# >>>0,1,1,2,3,5
a(2, 2)
# >>>4
fib
# >>>0
# Puedes cambiarlas si te da la gana
# No lo recomiendo, pero lo usaremos mas adelante con las funciones anonimas

# Ahora, cuidado:
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
# >>>[1]
print(f(2))
# >>>[1, 2]
print(f(3))
# >>>[1, 2, 3]
# Los valores por defecto solo se declaran 1 vez
# Por lo que si modificas el valor por defecto, lo modificas para las veces siguientes
# Para evitar eso, esta el None
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

# ////////////////////////////////////////////////////////

# Por otra parte, la forma en la que metemos valores a una funcion son diversas
def poss(n1, n2, n3):
  return n1, n2, n3
# Esta devolvera una tupla segun el orden de entrada
poss(1, 2, 3)
# >>>(1, 2, 3)
# Ten en cuenta que hay que meter los tres valores
# Ahora, se puede declarar excatamnete el orden
poss(n1 = 1, n3 = 2, n2 = 3)
# >>>(1, 3, 2)
# Esto significa que ignora el orden y pone el valor en la variable especifica
# Hay mas formas, como hacer que solo se pueda por orden, o solo por nombre
# Pero eso ya lo miras en la documentacion, ya que no se suele usar


# Lo que si suele pasar es que una funcion pueda requerir un numero indeterminado de valores
# Es decir, si pido una lista de invitados
# Pueden ser 2, 3, 5 o 20 invitados
# Podria pasar una lista, pero hay otra forma mas comoda
def fiesta(hospedante, *invitados):
  print(hospedante, 'le da la bienvenida a:')
  for persona in invitados: print(persona)

fiesta('Andrius', 'Kevin', 'Adriel', 'Mas geste')
# >>>Andrius le da la bienvenida a:
# >>>Kevin
# >>>Adriel
# >>>Mas geste

# Se que solo ahorra la molestia de pasar una tupla
# Pero esa pequenna molestia permite ahorras espacio
# Y, por poco que sea, tiempo
# Pero esta no es la unica forma de pasar parametros

args = (1, 10)
list(range(*args))
# >>>[1, 2, 3, 4, 5, 6, 7, 8, 9]
# El * desempaqueta los datos
# Lo que significa que mete los datos por orden
# De esta forma, usar
a = ['a', 'b', 'c']
poss(*a)
# >>>('a', 'b', 'c')
# Es lo mismo que
poss('a', 'b', 'c')
# Solo que esta vez, el * indeoendiza la variable y los datos
# Permitiendo meter los datos con un input


# Otra opcion es declarar los nombres sobre la marcha
# Definamos dos diccionarios de documentacion
docc1 = {
  'DNI': 1234,
  'Nombre': 'Pepe',
  'Fecha': '12/12/12'
} # Una persona con papeles
docc2 = {'Nombre': 'Willy'} # Otra sin papeles

def DNI(**datos): # La funcion
  if 'DNI' in datos:
    print(datos['Nombre'] + ', tu DNI es:', datos['DNI'])
  else:
    print(datos['Nombre'], 'no tiene papeles') # Si la persona no tiene nombre, esto causaria error
    # Asuamos que no

DNI(**docc1) # Esta vez usamos ** porque es un diccionario.
# >>>Pepe, tu DNI es: 1234
DNI(**docc2)
# >>>Willy no tiene papeles

DNI(Nombre = 'Jose', DNI = 4321)
# >>>Jose, tu DNI es: 4321
# Esto es lo que significa el **
# Si usas * simple, estas desempaquetando una lista sin mas
# Si usas **, estas pasando un valor como key y otro como value (diccionarios)


# Aprende la diferencia y podras crear funciones ESCALABLES que funcionan UNIVERSALMENTE
# (A mi me encanta hacer eso, y creo que a ti tambien)
