# Esta clase es necesaria para avanzar a proyectos
# Debido a que se usan muchas cosas importadas
# Asi que ya es hora de saber que significan


# En general, los modulos son otros archivos de los que extraemos funciones
# Por ejemplo, del modulo os usamos system()
# Eso significa que dentro del archivo de os, hay una funcion llamada system
# Usemos ejemplos reales
import math

import mates.ctg
import mates.dice
# Esto nos permite usar todo lo que tiene math
math.pi
# >>>3.141592653589793
math.e
# >>>2.718281828459045
math.sin(math.pi/2)
# El seno de pi/2, es decir, sen(90)
# >>>1.0

# Como podemos ver, estamos usando lo que tiene math
# Pero siempre poniendo su nombre, un punto y lo que usamos
# Eso es proque importamos el archivo entero
# Es posible importar cosas especificas

from math import pi, e, sin
pi
# >>>3.141592653589793
e
# >>>2.718281828459045
sin(math.pi/2)
# >>>1.0

# La esta vez, DESDE (from) math importamos unicamente pi, e y sin
# Si intentamos usar otra cosa, falla
math.cos(0)
# >>>1.0
cos(0)
# >>>NameError: name 'cos' is not defined
# Esto es porque cos no esta definido EN GENERAL, pero cos si que existe DENTRO DE math
# Ese punto es 'dentro de esto, usa esto otro'
# De ahi que 'abc'.upper() exista, pero upper('abc') no
# Porque upper() solo existe dentro de las strings (un objeto)
# ! Lo de 'dentro de las strings (un objeto)' es importante cuando demos POO
# Programacion orientada a objetos
# Pero eso en futuros archivos


# Pues eso es en general los modulos de LA LIBRERIA ESTANDAR
# Para mas cosas, investigar pip y la documentacion/internet
# Lo primero para tener mas librerias. Lo segundo para conocer las librerias

# Ahora, porque no creamos nuestros propios modulos?

# //////////////////////////////////////////

# Para esto, es OBLIGATORIO un editor de codigo
# Se puede usar consola, pero es mucho lio
# Ademas, necesitas archivos
# Sin embargo, seguire explicando como hasta ahora:
# como escribiendo en consola
# Si quieres solo usar editor, recuerda usar el print()

# Creamos el archivo AP_6.py
# ! Importante que acabe en .py

from AP_6 import *
# Esa estrella significa importarlo TODO
# Segun lo que ya aprendiste antes
# Pues ahora podemos usar lo escrito alli

suma(4, 8)
# >>>12

favs['Sapiens']
# >>>10

# Podemos usa lo ahi escrito como si nada
# Si hubieramos puesto
import AP_6
# Pues es lo mismo pero poniendo AP_6.

AP_6.suma(4, 8)
# >>>12

AP_6.favs['Sapiens']
# >>>10

# Pero si el nombre es muy raro, muy largo, o ambas cosas:

import AP_6 as AP # Usas el nombre que te de la gana

AP.suma(4, 8)
# >>>12

AP.favs['Sapiens']
# >>>10



# Pero tambien se pueden hacer mas cosas
# Usare un ejemplo real
# El modulo "mates" es una coleccion de distintos programas que cree en cuarto de la ESO
# Tiene muchas funciones, asique utilicemoslas

# Por cierto: el __init__.py es OBLIGATORIO para que python reconosca a "mates" como un paquete

import mates.dice, mates.ctg

mates.dice.dado(6)
# Una funcion que devuelve un numero aleatorio entre 1 y 6

mates.ctg.encriptar('Hola', 1)
# >>>'Gñk9'

# Lo que estamos haciendo es ir al paquete "mates" e importar los archivos
# Hay que poner todo el nombre, a no ser que le pongamos un pote
import mates.dice as dice, mates.ctg as ctg

dice.dado(6)
# Una funcion que devuelve un numero aleatorio entre 1 y 6

ctg.encriptar('Hola', 1)
# >>>'Gñk9'

# Te regalo el modulo. Usalo segun consideres
# Lo mas util es ecu (modulo de calculo de polinomios)
# Advertencia: matematicas + programador novato = poco legible

# Ahora, un ultimo regalo