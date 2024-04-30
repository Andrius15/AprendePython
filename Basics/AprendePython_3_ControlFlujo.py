# A partir de aqui recomiendo usar VS directamente (copiar y pegar o descargar el archivo)
# Pero ten la consola a mano
# Si bien VS tiene consola, tenerla a parte permite hacer experimentos
# Realmente agradeceras tener el habito de hacer experimentos en consola

# /////////////////////////////////////////////////

# Empezamos con el if
x = int(input("Please enter an integer: ")) # Esto ya te lo conoces

if x < 0:
  print('Negativo')
elif x == 0:
  print('0')
elif x == 1:
  print('Es 1')
else:
  print('Mas')

# Creo que esto ya sabes como funciona
# Tan solo vamos a experimentar un poco
# ! Abre la consola

True
# >>> True
False
# >>> False
# En python, True y False (con mayuscula) son los buleaon (bool)
# Pero tambien se puede usar 0/None como False y 1/'Algo' como true
# Ejemplo para pegar en consola

if 0:
  print(0)

if 1:
  print(1) # >>>1

if None:
  print(None)

a = 'hola'
if a:
  print(a) # >>>hola

# En general, esto se usa poco
# Pero cuando se usa, es util
# Imagina tener que poner a != None
# Que eso es otra: los comparadores

# Los comparadores son expreciones que devuelves True o False
# Son:
# == ; != ; < ; > ; <= ; >= ; is ; in
# or ; and ; not

1 == 1
# >>>True
# Igual?

1 != 2
# >>>True
# Distinto?

3 < 1
# >>>False
# Menor?
# Asumo que ya pillas lo de >

# Cuidado:
3 <= 3
# >>>True
3 < 3
# >>>False
# Los < > son estrictos. Es decir, SOLO los que son mayores o menores
# Los <= >= son 'menor/mayor o igual', por lo que incluyen el numero
# Esto importa, porque es la diferencia entre que alguien muera a los 0 de vida o no
# O que se ejecute un codigo 10 u 11 veces

# Los or; and; not son puertas logicas
# Porsi acaso:
True and True
# >>>True
True and False
# >>>False
True or False
# >>>True
not True
# >>>False

# Dato: primero se hacen los not, despues los and y por ultimo los or
True or False and True
# >>>True
# True or (False and True)
False or False and True
# >>> False
# False or (False and True)
False or not False and True
# >>>True
# False or ((not False) and True)
# False or (True and True)

# Ahora, el is
# Se usa poco
# En general, se usa para comprobar si algo ES TAL CUAL OTRA COSA
# Por ejemplo: (solo noto diferencias a partir de listas)
a = [1, 2]
b = [1, 2]
c = a

a == b
# >>>True
a == c
# >>>True
# Hasta ahora, logico
a is c
# >>>True # Porque c es a copiado
a is b
# >>>False # Porque b se creo a parte


dic1 = {1: 'a', 2: 'b'}
'b' in dic1
# >>>False
1 in dic1
# >>>True

a = [1, 2, 3]
4 in a
# >>>False
1 in a
# >>>True

# Asumo que eres lo suficientemente inteligente para ver que es esto

# ///////////////////////////////////

# Ahora match
# Son como los if, pero solo para una variable
# Hasta ahora los he usado poco
# Sobretodo porque son nuevos
# No me detendre mucho

# En vez de:
"""
x = int(input("Please enter an integer: ")) # Esto ya te lo conoces
if x < 0:
  print('Negativo')
elif x == 0:
  print('0')
elif x == 1:
  print('Es 1')
else:
  print('Mas')
"""
# Usa:
x = int(input("Please enter an integer: ")) # Esto ya te lo conoces

match x:
  case 0:
    print(0)
  case 1:
    print(1)
  case _:
    print('Ni 0 ni 1')

# Solo funciona como == (hasta donde he visto), pero ahorra tiempo y recursos

# ///////////////////////////////////////////
# Ahora lo que nos interesa: bucles

a = [0, 1, 2, 3, 4]

for i in a:
  print(i)
# >>>0
# >>>1
# >>>2
# >>>3
# >>>4

# Esto ya te lo sabes. Pero hay mas

for i in a:
  print(i, end=',')
#>>>0,1,2,3,4,
# Esto es para aprender el primero de 3 cosas utiles en print
# Las otras 3 te las ensenno luego
# Te habras dado cuenta que los numeros se superponen a la consola
# Eso es porque la consola no cambia de linea
# Eso lo haras tu luego

# Hay mejores formas de crear iterables

for i in range(5):
  print(i, end=',')
# Es lo mismo, pero nos ahorramos a
# Range empieza en 0 y termina en 4 (1 menos que el que le digas)

for i in range(10, 110, 10):
  print(i, end=',')
# >>>10,20,30,40,50,60,70,80,90,100,
# De esta forma, el primer numero es donde empiezas
# El segundo donde terminas (+ el extra del salto)
# Y el tercero son los saltos


# ====================================
# Un poco mas de curiosidades:
a = {'Sao':9, 'DrStone':10, 'Your Lie in April':10, 'Beastars':None, 'Mira Que Eres Boba': 0}
for nombre, puntos in a.items():
  if puntos == None: continue
  print('A ',nombre,' le doy un ',puntos,sep='')
# >>>A Sao le doy un 9
# >>>A DrStone le doy un 10
# >>>A Your Lie in April le doy un 10
# >>>A Mira Que Eres Boba le doy un 0
# Aqui hay muchas cosas

# Primero, a.tiems() devuelve una lista con tuplas:
a.items()
# >>>dict_items([('Sao', 9), ('DrStone', 10), ('Your Lie in April', 10), ('Beastars', None), ('Mira Que Eres Boba', 0)])
# nombre, puntos se considera una especie de tupla
# Cada tupla de a.items() se guarda en nombre, puntos
# De esta forma, la primera tupla ('Sao', 9) se guarda
# nombre pilla 'Sao' y puntos guarda 9
# Se ejecuta el codigo
# Cuando termina esa iteracion, sigue con la tupla ('DrStone', 10) y asi

# if puntos == None:contine
# Esto hace que Beastars no se imprima
# Cuando puntos == None (el caso de Beastars) se ejecuta continue
# Cuando solo es 1 instruccion, puedes poner el codigo en la misma linea del if
# El continue es mas o menos un 'has terminado esta iteracion, ve a la siguiente'
# En vez de comprobar que puntos != None para imprimirlo,
# usamos continue para comprobar puntos == None

# print('A ',nombre,' le doy un ',punto,sep='')
# En el anterior, end= basicamente es lo que se pone al final del print
# Por defecto es un salto de linea, por eso cambiarlo lo quita
# Este sep es lo que se usa para saber que poner entre coma y coma
# Que esa es otra: no puedes hacer print('a' + 1)
# Pero puedes hacer print('a',1) # >>>'a 1'
print('a','b','c',sep='/')
# >>>a/b/c
# De esta forma, ya conoces el segundo truco del print
# Asi como el for y continue
# Ahora veremos el while, break y el else parte 2

# ///////////////////////////////////////

a = 100
while a > 0:
  print(a, end=';')
  a -= 1
else:
  print()
# >>>100;99;98;97;96;95;94;93;92;91;90;89;88;87;86;85;84;83;82;81;80;79;78;77;76;75;74;
#73;72;71;70;69;68;67;66;65;64;63;62;61;60;59;58;57;56;55;54;53;52;51;50;49;48;47;46;45;
#44;43;42;41;40;39;38;37;36;35;34;33;32;31;30;29;28;27;26;25;24;23;22;21;20;19;18;17;16;
#15;14;13;12;11;10;9;8;7;6;5;4;3;2;1;
# while, al contrario que for, no utiliza un iterable, utiliza una condicion
# Un ejemplo es esta:
a = True
while a:
  respuesta = input('Introduce "NO":') # Introduce cosas que no seas 'NO'
  if respuesta == 'NO': a = False
# Veras que no te deja de preguntar hasta que no pongas 'NO' exactamente
# Mira el if y veras porque
# Vamos ha hacer que el 'no', 'No' y 'nO' tambien funcionen
while a:
  respuesta = input('Introduce "NO":') # Introduce cosas que no seas 'NO'
  if respuesta.upper() == 'NO': a = False
# El upper() hace que lo que metas se ponga en MAYUSCULAS
# El lower() lo pone en minusculas
# Este no es el truco 3 del print, pero ahora te lo ensenno:
while a:
  respuesta = input('Introduce "NO":') # Introduce cosas que no seas 'NO'
  if respuesta == 'NO': a = False
  elif respuesta.upper() == 'NO': break
else:
  print('Bien hecho', 'esclavo', sep='\n')
# Ahora veras 2 cosas nuevas:
# La primera es que si usas 'NO' te llama esclavo
# Pero si usas 'no', 'No' o 'nO' simplemente se cierra
# La segunda es que el esclavo esta es otra linea, siendo que solo usamso un print

# Lo primero es porque el while se cerro de forma normal
# Si tanto un while como un for se cierran porque han terminado, el else se ejecuta
# Pero el break los cierra a la fuerza, causando que el else no se ejecute

# Lo segundo es por el \n
# \ es un caracter que permite usar caracteres especiales
print('\'Hola\' es un saludo')
# >>>'Hola' es un saludo
# \n es un salto de linea (enter)
# De resto, \ permite usar las mismas comillas tanto para el mensaje como para declarar el str
# Este era el tercer truco
# El truco secreto te lo ensenno en la clase de funciones

# ////////////////////////////////////////

# Ya es un meme el tema de los errores. Pues ahora aprenderas a manejarlos un poco
# La consola te dice cosas utliles
# Forcemos un error:

while True print('Hello world')
"""
File "<stdin>", line 1
    while True print('Hello world')
               ^^^^^
SyntaxError: invalid syntax
"""
# Lo primero que dice es DONDE ocurre el error. Archivo y linea
# Despues, sennala excatamente el lugar donde ocurrio el error
# ! OJO: no de donde procede, sino donde ocurrio.
# Es decir, si el error proviene de que el usuario mete una letra en vez de un numero
# el programa solo te dira donde es que esa letra causa un error
# Al final del todo te dice que tipo de error es, asi como una descripcion

# Hay mas errores, tan solo es cosa tuya buscar sus nombres
# O parchear tu codigo en las pruebas

# Ahora, gestionemos los errores:
while True:
    try: # La palabra para manejar errores
        x = int(input("Please enter a number: "))
        break
    except ValueError: # Lo que hara cuando ocurra ese error
        print("Oops!  That was no valid number.  Try again...")
# Tambien puedes poner varios tipos de errores a la vez:
try:
  a = int(input('Dime tu nombre'))
  print(a / 0)
except (ValueError, ZeroDivisionError): # Errores especificos. Una lista
  print('Lo siento. Somos tontos')
except IndexError: # Un solo error en especifico
  print('Como es esto posible?')
except: # Error generico
  print('No se que ha salido mal')

# De la misma forma, puedes crear tus propios tipos de errores y forzarlos
# Pero eso investigalo tu
# Todo lo que tienes que saber es:

try:
  raise ZeroDivisionError
except ZeroDivisionError:
  print('Pero... no hay ninguna division')
except:
  print('Que? Pero... SI MI CODIGO ES PERFECTO!')
# >>>Pero... no hay ninguna division

# ////////////////////////////////////////


# Antes de pasar a funciones, el pass
while True:
  pass
# Entras en bucle infinito
# Si quieres salir, usa Ctrl+C
# El pass permite que el codigo funcione aun si no lo has implementado
# Cuando demos los tipos de errores, lo cambiaremos
# Pero esto es util en general cuando queremos que el codigo se ejecute,
# pero no queremos que haga nada

def esperar():
  pass # Recuerda importar time e implementar esto
