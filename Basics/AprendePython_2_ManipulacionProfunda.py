# Copio y pego las variables de antes

a = 'Andrius'
b = 'Kevin'
n1 = 1
n2 = 5.5
c = [1,2,3]
d = [4,3,'f', a, c]
A = (3,5,'g')
dic1 = {1: 3, 2: 'a', 'SAO': 'Anime', 3.14: 'PI', 7: 3}
dic2 = {'cosaf': dic1, 'mucho texto': (a,b,d), 'a': A}
a_ = {1,2,3,4,5}

# Ahora, un poco de manipulacion de variables (tuplas y diccionarios sobretodo)

# ////////////////////////////////////////////


A[0] = 'f'
# >>>TypeError
# Las tuplas no puede ser modificadas
b[2:4] = 'ra'
# >>>TypeError
# Los str no soportan este tipo de asignaciones

c.append(9)
c
# >>>[1, 2, 3, 9]
# El append annade un valor al final de la lista
c.pop()
# >>>9
c
# >>>[1, 2, 3]
# pop() elimina el ultimo valor y lo devuelve
n3 = c.pop()
c
# >>>[1, 2]
n3
# >>>3
# Las funciones que devuleven valores pueden ser guardadas
# Recuerda esto, porque lo usaremos cuando demos funciones

len(a)
# >>>7
len(c)
# >>>2
# len() devuelve la longitud de la cadena
# Funciona tanto en listas y tuplas como en str


# Puedes ver esto como que no estas usando las posiciones, si no los ESPACIOS
# 'Andrius'
# / A / n / d / r / i / u / s 
# 0   1   2   3   4   5   6
#-7  -6  -5  -4  -3  -2  -1
a[3:5]
# >>>'ri'
# Porque desde el 3 hasta el 5 estan esas letras
a[3:-2]
# >>>'ri'
# Porque sigue siendo esos los espacios
a[3:-5] 
# >>>''
# Porque sigues hacia delante
a[3:-5:-1] 
# >>>'r'
# Esta vez si

# Ahora, un pequenno adelanto
# Hazlo en otro documento en VS
a, b = 0, 1
while a <10:
  print(a)
  a, b = b, a+b

# Ahora veremos esto

