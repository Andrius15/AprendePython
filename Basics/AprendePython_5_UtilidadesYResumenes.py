# Ahora, vamos a aprender a usar expresiones utiles y algunas cosas nuevas
# Este seria lo utlimo
# A partir del proximo archivo, empezariamos con cosas mas potentes


# Primera cosa nueva: funciones anonimas
# Permite crear funciones pequennas facilmente
# Es mas, permite crear funciones que crean funciones

def sumador(n : int = 1) -> callable: # Las anotaciones
    return lambda x: x + n
# Ahora tenemos una funcion que devuelve funciones
# Vamos a crear unas cuantas

a = sumador(6)
b = sumador(3)
c = sumador(-4.5)

a(4)
# >>>10
b(4)
# >>>7
c(4)
# >>>-0.5

# Como podemos ver, sumador() crea funciones que suman el valor que especifiquemos
# lambda compacta el def en una sola linea, por lo que no permite funciones complejas
a = lambda x: x + 1
# Lo que hay despues del lambda pero antes que los : son los argumentos
# Lo que va entre los () en las funciones normales
# Lo que hay despues de los : es equivalente a
# return \\tu codigo aqui\\
# De esta forma, lo anterior es igual a
def a(x):
  return x + 1
# Esto por si solo es inutil, pero es increiblemente poderoso con las siguientes expresiones


del a, b, c # Las borra para no confundirnos
a = list(range(10)) # Numeros del 0 al 9 en una LISTA
b = map(lambda x: x ** 2, a)
b
# >>>map object
# Eso es porque es su propio tipo de objeto
print(*b)
# >>>0 1 4 9 16 25 36 49 64 81
# map lo que ha hecho es aplicar la funcion de antes de la coma (lambda x: x ** 2)
# A todos los valores del iterable despues de la coma (a)
# Y los guarda en su propio objeto iterable, por lo que se puede desempaquetar (*b)
# A que hubiera sido un dolor de huevos definir una funcion entera solo para esto?
# Yo no lo suelo usar porque se me olvida que existe
# Pero la de veces que he usado un for para estas coas....


del a, b
a = list(range(10))
b = filter(lambda x: x%2 == 0, a)
b
# >>>filter object
# Otra vez
print(*b)
# >>>0 2 4 6 8
# Filter hace casi lo mismo que map
# Pero en vez de guardar lo que da la funcion, guarda el valor original
# pero solo si la funcion devuelve True cuando se le aplica
# Si no dieramos una funcion, solo guardaria aquello que funciona como un true

a = (0, None, 1, 'Si', True)
b = filter(None, a)
print(*b)
# >>>1 Si True


# Ahora, la razon por la que no suelo usar mucho esto es porque,
# para mi nivel, uso la contraccion del for
a = list(map(lambda x: x**2, range(10)))
a
# >>>[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
a = [i**2 for i in range(10)]
a
# >>>[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# La segunda forma es un for compactactado en una linea
# Es mas facil de leer, y un poco mas versatil
a = [i**2 for i in range(10) if i%3 == 0] # Solo los multiplos de 3
# >>>[0, 9, 36, 81]
a = [(i, i**2) for i in range(10)]
# >>>[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81)]
# Incluso se pueden crear diccionarios y for anidados
a = {i: i**2 for i in range(10)}
# >>>{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
a = ((i, o) for i in range(5) for o in range(i))
# >>>generator
# Un tipo de objeto que consume menos recursos, pero que solo es iterable 1 vez
list(a)
# >>> ((1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (4, 3))
list(a)
# >>>()

# Por eso no suelo usar los otros
# Los proyectos pequennos y en la consola requieren mucha experientacion
# Y esta es la forma mas rapida
# Pero los otros son mucho mas util en el contexto de ejecucion


# Una ultima cosa: zip
a = list(range(10))
b = list(map(lambda x: x**2, a))
c = dict(zip(a,b))
c
# >>>{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# Basicamente crea un diccionario
# El primer arguento (a) son las keys
# El segundo argumento (b) son los values
b = list(map(lambda x: (x**2, x**3), a))
c = dict(zip(a,b))
c
# >>>{0: (0, 0), 1: (1, 1), 2: (4, 8), 3: (9, 27), 4: (16, 64), 5: (25, 125), 6: (36, 216), 7: (49, 343), 8: (64, 512), 9: (81, 729)}
# Esta vez, guarda el cuadrado y el cubo

# Por cierto, recuerdas...
for i, o in c.items():
    print(i, 'tiene como values:', o)
# >>>0 tiene como values: (0, 0)
# >>>1 tiene como values: (1, 1)
# >>>2 tiene como values: (4, 8)
# etc etc
# Pues bien, mira esto
for i, o in zip(a, b):
    print(i, 'tiene como values:', o)
# Da lo mismo, pero nos ahorramos es diccionario

# ///////////////////////////////////////////

# Los generadores
# Ya vimos un avance antes
# Son objetos iterables una unica vez
# Pero infinitamente mas eficientes
# Porque algunos pueden ser infinitos
# Es decir, objetos que devuelven valores creandolos sobre la marcha
# Vamos a hacer un ejemplo:
a = (i**2 for i in range(10000)) # El generador usa ()
b = [i**2 for i in range(10000)] # La expresion util de la lista usa []
# Para ver bien la diferencia, usemos algo avanzado
import sys
# Para comparar
sys.getsizeof(5)
# >>>28
sys.getsizeof('a')
# >>>50
sys.getsizeof('cosaf')
# >>>54
sys.getsizeof('Esto es una fase larga')
# >>>71

# Ahora la diferencia entre generador y lista
sys.getsizeof(a)
# >>>208
sys.getsizeof(b)
# >>>85176
# Ahora entiendes la diferencia?
# Para ejemplificar, si convertimor b en una tupla:
b = tuple(b)
sys.getsizeof(b)
# >>>80040
# La tupla es menos que la lista, pero sigue siendo mucho
# De aqui la eficiencia de los generadores
# Sin embargo, no son subscriptables
b[10]
# >>>100
a[10]
# >>>Error
# No les puedes pedir un valor exacto, pero puedes pedirle los valores uno a uno
next(a)
# >>>0
# 0**2
next(a)
# >>>1
# 1**2
next(a)
# >>>4
# 2**2
# Pero si ahora lo convertimos en una lista, veremos una cosa cuirosa:
a2 = list(a)[:10] # Solo los 10 primeros valores
a2
# >>>[9, 16, 25, 36, 49, 64, 81, 100, 121, 144]
# No empieza en 0, empieza en 9 (3**2)
# Eso es porque el 0, 1 y 2 ya fueron usados antes
# De hecho, acabamos de usar todo el generador
next(a)
# >>>StopIteration
# list(a)[:10] usa todo el generador, pero solo guarda los primeros 10 numeros
# En su lugar, porque no creamos un generador infinito?

def fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibo()
# >>>generator object
next(fibo()) # Como no hemos guardado fibo() en una variable, hay que ejecutarlo
# >>>0
next(fibo())
# >>>0
# De hecho, como estamos ejecutando la funcion desde 0, el generador empieza desde 0
fib_generator = fibo()

# Ahora, cada vez que usemos next, el generador hara su trabajo
# Ira a la funcion
"""
def fibo():
    a, b = 0, 1
    while True:
        yield a # Equivalente a return
        a, b = b, a + b
# Ahora, cada vez que se use el next, empieza la ejecucion
# Al llegar al yield, devuelve para ESA iteracion ese valor
# Su se vuelve a usar next, el generador lo retoma donde lo dejo:
# a, b = b, a + b
# Lo siguiente es aplicar el yield
# Y asi
# Como es un while True, es un generador infinito
# Pero si pusieramos a < 10000
# Solo seria iterable hasta ese numero
"""
def fibo2():
    a, b = 0, 1
    while a < 10000:
        yield a
        a, b = b, a + b

a2 = fibo2()
for i in a2: print(i, end='/')
# >>>0/1/1/2/3/5/8/13/21/34/55/89/144/233/377/610/987/1597/2584/4181/6765/
a2 = fibo2() # Recargar el generador
while True: print(next(a2), end='/')
# Devuelve lo mismo, pero con un 'StopIteration',
# porque en algun momento se intento seguir cuando ya se habia acabado el generador

# Usemos lo que hemos aprendido
a = [next(fib_generator) for _ in range(10)]
a
# >>>[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# Si ahora usamos next...
next(fib_generator)
# >>>55
# Sige por donde lo dejo
# Y como no pusimos nada que lo limite, seguira hasta que lo paremos
sys.getsizeof(fib_generator)
# >>>208
next(fib_generator) # >>>89
sys.getsizeof(fib_generator)
# >>>208
while True: print(next(fib_generator))
# Ctrl + C -> parar
# Saldran numeros enormes, pero no para
sys.getsizeof(fib_generator)
# >>>208
# Para cosas pequennas no, pero para cosas grandes que seran iteradas son potentisimas


# Por cierto, el filter y el map no se ejecutan hasta que sean usados
# Es decir:
fib_generator = fibo() # Recargar el generador
a = map(lambda x: 1/x, fib_generator)
b = filter(lambda x: x%2 == 0, fib_generator)
# Estas dos cosas no tardan nada en calcular
# Y como son iterables...
next(a)
# >>>ZeroDivisionError
next(a)
# >>>1
next(a)
# >>>1
next(b)
# >>>2
next(b)
# >>>8
next(b)
# >>>34

# Como ves, el map y el filter se aplican sobre la marcha
# Tanto asi que, si hubiera un error en el lambda (o funcion), no salta hasta que se ejecuta
# Y, como generadores provenientes de otro generador infinito, a y b son infinitos
# Pero no son independientes
fib_generator = fibo()
next(b)
# >>>144
next(a)
# >>>0.004291845493562232
# 1/0.004291845493562232 = 233
next(b)
# >>>610
next(b)
# >>>2584
next(a)
# >>>0.00023917723032767282
# 1/0.00023917723032767282 = 4181
# Como ves, a sigue lo que haga b y vicebersa
# Cuidado con eso

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Una ultima cosa util:
del a, b, c, a2
a = 'Andrius'
b = 145
print(f'{a} es buscado en {b} paises')
# >>>Andrius es buscado en 145 paises
# Si pones f antes de ''
# puedes usar {} para poner variables
# Lo que sea que tenga la variable, sera convertido a str
# Las listas tambien
a = ['Andrius', 'Kevin']
print(f'{a} es buscado en {b} paises')
# >>>['Andrius', 'Kevin'] es buscado en 145 paises
# Pero es convertido asi

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Y ya esta
# Con esto ya tenemos todo lo importante
# Hay mas cosas en la documentacion, pero no es importante
# Solo queda errores, modulos y clases
# Pero eso es si quieres llegar a programas muy complejos
# Con haber llegado hasta aqui ya te permite manejar una gran cantidad de problemas
# Sobretodo de calculo y manejo de datos

