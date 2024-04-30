# Este es el primer archivo
# Esto son comentarios
# A partir de aqui, habra ejercicios para realizar en CONSOLA
# La ejecucion de archivos sera a partir del segundo

"""
Esto tambien es un comentario
pero en vez de ser uno de una linea
incluye varias.
Ya veras que conocer esto te sera util
"""

# ///////////////////////////////

# Declarar variables
# Declaras variables poniendo un nombre, un igual, y el dato que quieres guardar
a = 'Andrius' # Esta variable es un string (str), texto
b = "Kevin" # El texto se guarda con ' ' o con " ". Abre y cierra con el mismo

n1 = 1 # Esta variable es un integer (int), un numero sin decimales
n2 = 5.5 # Esto es un float (float), un numero con decimales

c = [1,2,3] # Esto es una lista (list), que son varios tipos de datos
d = [4,3,'f', a, c] # Las listas pueden guardar int, str e incluso otras listas y variables
# Las listas se forman con [ ] y separando los datos con comas (,)

A = (3,5,'g') # Esto es una tupla (tuple), son listas QUE NO SE PUEDES MODIFICAR
# Se forman igual que las listas, pero con ( )
# Consumen menos espacio en memoria

# ! por cierto, fijate que a y A no son lo mismo
# Los nombres de las variables solo tienen dos limitaciones:
# Tiene que estar todo unido: (Num 1) no vale, pero (Num_1) o (Num1) si
# No pueden ser palabras reservadas: no pudes usar las palabras que ya usa python para otras cosas
# El (if, else, while, dict, int, try...) todo lo que el editor te autocomplete y no sea azul clarito
# ! If, iF o IF si se pueden usar, debido a las mayusculas

# Ahora prueba a poner tal cual los nombres de las funciones en la consola
# Saldran los valores de las variables
# =======================================================
# Dentro de poco jugaremos con esto
# Antes, aprenderemos otros dos tipos de datos

dic1 = {1: 3, 2: 'a', 'SAO': 'Anime', 3.14: 'PI', 7: 3}
# Un diccionatio (dict) es una estructura que guarda datos usando otros
# Por ejemplo, el dato 'PI' esta guardado con la llave 3.14
# El dato 3 lo contiene tanto 1 como 7.
dic2 = {'cosaf': dic1, 'mucho texto': (a,b,d), 'a': A}
# Los diccionarios pueden contener tuplas, listas e incluso otros diccionarios
# Las key (el numero antes de los : ) no puede ser otra cosa que no sea texto o numeros
# Si repites key, la anterior pierde datos
a_ = {1:1 , 1:2} # Declaralo y mira su contenido

# Si quieres acceder a algo especifico de un diccionario, usa [] despues del nombre
dic1['SAO'] # Esto deberia devolver >>>'Anime'


a_ = {1,2,3,4,5} # Esto es un set (set)
# Los datos que guardas en un set son unicos
# Si intentas annadir mas de una vez un dato, simplemente se ignora
# Los sets consumen menos espacio, pero no itenen orden
# No puedes hacer a[1] porque eso no existe, pero si es iterable
# (Ya veremos como acceder a los datos de las variables despues)

# ///////////////////////////////////////////

# Ahora, vamos a manipular los datos un poco

a
# >>>'Andrius'
b
# >>>'Kevin'
a+b
# >>>'AndriusKevin'
a*2
# >>>'AndriusAndrius'
a + n1
# >>>TypeError
# Si lees sabras porque: los str y los int no se juntan
# Pero
b + str(n1)
# >>>'Kevin1'
# Usar el nombre del tipo de dato y los () convierte lo que hay dentro en el tipo de dato
# Esto lo usaras (sobretodo) para convertir los str en numeros al introducir datos
# Hablando de eso: hagamos un mini proyecto (mini)

# !!! Esto ahora si se hace en un documento
n1 = int(input('=> Introduce en 1º nº:'))
n2 = int(input('=> Introduce en 1º nº:'))
print(n1+n2)
# Esto te devuelve la suma de ambos numeros

# Seguimos con los operadores
n1 + n2
# >>>6.5
n1 - n2
# >>>-4.5
n2 * 2
# >>>11.0
# 11.0 y no 11 porque n2 es float. Cuidado con los float, porque no todos aceptan float
# Usa int() para los integer
int(n2*2) # Con o sin espacio funciona igual. Yo suelo poner espacio para que sea legible
# >>>11
4/2
# >>>2.0
# Por defecto, las diviciones devuelven floats
15/7
# >>>2.142857142857143
15//7
# >>>2
# Usar // devuelve el entero
15%7
# >>>1
# Usar % devuelve el resto si hicieramos la divicion a mano
# Usar % y que de 0 permite conocer si uno es multiplo de otro, cosa util
# Por ejeomplo X%2 == 0 permite comprobar si es par
2**3
# >>>8
# Usar ** es equivalente a usar ^ en la calculadora
10**4
# >>> 10000


# Las listas y tuplas son un tanto mas complejas, pero mas utiles
d
# >>>[1, 2, 3]
A
# >>>(3, 5, 'g')
A[0]
# >>>3
A[1]
# >>>5
A[2]
# >>>'g'
A[3]
# >>>IndexError
A[-1]
# >>>'g'
A[-3]
# >>>3
A[-4]
# >>>IndexError
# Las listas y tuplas permiten guardar datos
# Con A[] conseguimos datos especificos
# Empezamos a contar desde el 0 y puedes ir hacia alante o atras, pero solo 1 vez
# Si te pasas, error
# Ahora mira:
d
# >>>[4, 3, 'f', 'Andrius', [1, 2, 3]]
d[-1]
# >>>[1, 2, 3]
d[4]
# >>>[1, 2, 3]
d[4][0]
# >>>1
# d[4] devuelve una tupla, d[4][0] es equivalente a coger esa tupla (c) y usar [0]
# Esto es un poco lio, pero permite arrays bidimencionales, cosas utiles si quieres hacer mapas
# O matrices, o guardar listas dentro de listas

a[0]
# >>>'A'
# Segun python, las str son considerados listas
a[0:3]
# >>>'And'
a[:3]
# >>>'And'
# Usar : te permite decir desde donde empiezas hasta donde acabas
a[3:5]
# >>>'ri'
a[3:]
# >>>'rius'
a[::2]
# >>>'Adis'
a[::-1]
# >>>'suirdnA'
a[:3:-1]
# >>>'sui'
# Si pones otro : puedes elegir los pasos que das
# Si pones -1 primero inviertes la cadena
# Esto tambien funciona con lo listas y tuplas
A[::-1]
# >>>('g', 5, 3)
d[2::2]
# >>>['f', [1, 2, 3]]
