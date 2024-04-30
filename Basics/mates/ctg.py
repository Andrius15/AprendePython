
# + 'encriptlv2' tiene arreglados y corregidos varios errores
# ! Si la clave es mayor a {len(abc)-abc.index(i)} da error

abc = [i for i in 'abcdefghijklmnñopqrstuvwxyz 0123456789']
abc_base = tuple(abc)

def add(add):
    for p in add:
        if not p in abc:
            abc.append(p)

def quit(quit):
    for l in quit:
        abc.remove(l)

def restart():
    abc[:] = list(abc_base)

# De frase normal a una sin sentido
def encriptar(frase,clave=0):
    cripto=[]
    for i in frase:
        if i in abc:
            try:
                cripto.append(abc[abc.index(i)-clave])
            except IndexError:
                clave = clave % len(abc)
                cripto.append(abc[abc.index(i)-clave])
            continue
        elif i.lower() in abc:
            try:
                cripto.append(abc[abc.index(i.lower())-clave].upper())
            except IndexError:
                clave = clave % len(abc)
                cripto.append(abc[abc.index(i.lower())-clave].upper())
            continue
        cripto.append(i)
    return ''.join(cripto)

# Cada frase con cana una de las claves (range(abc))
def Fbruta(frase):
    for o in range(0,27):
        cripto=[]
        print('Clave: ',o)
        for i in frase:
            if i in abc:
                try:
                    cripto.append(abc[abc.index(i)-o])
                except IndexError:
                    o = o % len(abc)
                    cripto.append(abc[abc.index(i)-o])
                continue
            elif i.lower() in abc:
                try:
                    cripto.append(abc[abc.index(i.lower())-o].upper())
                except IndexError:
                    o = o % len(abc)
                    cripto.append(abc[abc.index(i.lower())-o].upper())
                continue
            cripto.append(i)
        print(''.join(cripto))

# Dale la frase encriptada y te devolverá la original
# (si le das la clave o logras desencriptar una letra)
def desencrip(frase,clave=None):
    if not clave:
        print('Dame la equivalencia de una letra para poder calcular la clave')
        print('Solo escribe el dígito ya encriptado y su equivalente')
        print('Sin espacios ni nada. No es necesario')
        calcula_clave = input('=>')
        if calcula_clave:
            clave = abc.index(calcula_clave[1])-abc.index(calcula_clave[0])
        else:
            return ''.join(Fbruta(frase))

    cripto=[]
    for i in frase:
        if i in abc:
            try:
                cripto.append(abc[abc.index(i)-clave])
            except IndexError:
                clave = clave % len(abc)
                cripto.append(abc[abc.index(i)-clave])
            continue
        elif i.lower() in abc:
            try:
                cripto.append(abc[abc.index(i.lower())-clave].upper())
            except IndexError:
                clave = clave % len(abc)
                cripto.append(abc[abc.index(i.lower())-clave].upper())
            continue
        cripto.append(i)
    return ''.join(cripto)

from random import seed, randint
mr = 100

# De frase normal a una sin sentido, y pseudo-aleatoriamente
def encriplv2(frase,sd=None,inicio=None):
    if not sd:
        print('Se elegirá una semilla aleatoria entre 0 y', mr)
        sd = randint(0,100)
        print('La semilla elegida es:',sd)
    if not inicio:
        print('Se elegirá un inicio aleatorio entre 0 y', mr)
        inicio = randint(0,100)
        print('El inicio elegido es:',inicio)

    seed(sd)
    cripto=[]
    for EJEMPLO_NO_IMPORTA in range(0,inicio):
        randint(0,len(abc)-1)
    for i in str(frase):
        clave = randint(0,len(abc)-1)
        if i in abc:
            try:
                cripto.append(abc[abc.index(i)+clave])
            except IndexError:
                clave = clave % len(abc)
                try:
                    cripto.append(abc[abc.index(i)+clave])
                except IndexError:
                    clave = len(abc) - clave
                    cripto.append(abc[clave])
            continue
        elif i.lower() in abc:
            try:
                cripto.append(abc[abc.index(i.lower())+clave].upper())
            except IndexError:
                clave = clave % len(abc)
                try:
                    cripto.append(abc[abc.index(i.lower())+clave].upper())
                except IndexError:
                    clave = len(abc) - clave
                    cripto.append(abc[clave].upper())
            continue
        cripto.append(i)
    return ''.join(cripto)

# Cada frase con cada una de las semillas hasta la 27
# Y un extra de inicio desde 0 hasta 10
def Fbrutalv2(frase,sd=None,inicio=None,maxSd=mr,maxIni=mr):
    cripto = {}
    if not maxSd:
        if sd:
            maxSd = sd
        else:
            maxSd = mr
    if not maxIni:
        if inicio:
            maxIni = inicio
        else:
            maxIni = mr
    if not inicio:
        inicio = 0
    if not sd:
        sd = 0
    if maxSd < sd:
        print('Usaré la semilla como máximo y también como mínimo')
        sd = maxSd
    for o in range(sd,maxSd+1):
        cripto[f'Semilla {o}'] = {}
        for ini in range(inicio,maxIni+1):
            cripto[f'Semilla {o}'][f'Inicio {ini}'] = []
            seed(o)
            for EJEMPLO_NO_IMPORTA in range(0,ini):
                randint(0,len(abc)-1)
            for i in frase:
                clave = randint(0,len(abc)-1)
                if i in abc:
                    try:
                        cripto[f'Semilla {o}'][f'Inicio {ini}'].append(abc[abc.index(i)-clave])
                    except IndexError:
                        clave = clave % len(abc)
                        cripto[f'Semilla {o}'][f'Inicio {ini}'].append(abc[abc.index(i)-clave])
                    continue
                elif i.lower() in abc:
                    try:
                        cripto[f'Semilla {o}'][f'Inicio {ini}'].append(abc[abc.index(i.lower())-clave].upper())
                    except IndexError:
                        clave = clave % len(abc)
                        cripto[f'Semilla {o}'][f'Inicio {ini}'].append(abc[abc.index(i.lower())-clave].upper())
                    continue
                cripto[f'Semilla {o}'][f'Inicio {ini}'].append(i)
    for semillas in cripto:
        for inicios in cripto[semillas]:
            for desencrip in cripto[semillas][inicios]:
                cripto[semillas][inicios] = ''.join(cripto[semillas][inicios])
    return cripto

def desenlv2(frase,sd=None,inicio=None,fb=False,maxsd=None,maxini=None):
    FB = [False,False]
    if not sd:
        FB[0] = True
        print('Dame la semilla mínima')
        print('Si no, utilizaré la semilla mínima "0"')
        seed_post = input('=>')
        if seed_post:
            sd = int(seed_post)
        else:
            print('Ok, entonces será el 0')
            sd = 0

    if not inicio:
        FB[1] = True
        print('Dame el inicio mínimo')
        print('Si no, utilizaré el inicio mínimo 0')
        ini_post = input('=>')
        if ini_post:
            inicio = int(ini_post)
        else:
            print('Ok, entonces será el 0')
            inicio = 0

    if FB[0] or FB[1] or fb:
        return Fbrutalv2(frase,sd,inicio,maxsd,maxini)

    seed(sd)
    cripto=[]
    for EJEMPLO_NO_IMPORTA in range(0,inicio):
        randint(0,len(abc)-1)
    for i in str(frase):
        clave = randint(0,len(abc)-1)
        if i in abc:
            try:
                cripto.append(abc[abc.index(i)-clave])
            except IndexError:
                clave = clave % len(abc)
                cripto.append(abc[abc.index(i)-clave])
            continue
        elif i.lower() in abc:
            try:
                cripto.append(abc[abc.index(i.lower())-clave].upper())
            except IndexError:
                clave = clave % len(abc)
                cripto.append(abc[abc.index(i.lower())-clave].upper())
            continue
        cripto.append(i)
    return ''.join(cripto)


# Un funcion que comprueba si dentro de las combinaciones probadas hay una combinación especificada
def busca(frase,var_dict):
    for i in var_dict:
        for o in var_dict[i]:
            if var_dict[i][o] == frase:
                print('Semilla:',i)
                print('Inicio:',o)

"""
print('Haz la versión "2.1"')
# La combinación de la versión 1 y 2
# Crear una lista con cada combinación de letras posibles
# ? Ejemplo:
# ? En el caso de un solo caracter ('a'), una lista donde la clave va desde el 0 hasta 'len(abc)'
# ? En el caso de dos ('ab'), una lista donde la clave sea 'x' para (a) e 'y' para (b)
# ! Se puede dar los casos ('aa')/('bb'), o casos donde las claves sean (1,1)/(5,0)/(26,2)
# TODO Aquí están literalmente todas las combinaciones posibles, y más si añadimos caracteres a "(abc)"
@aut_h.a_h()
def encriplv2_1(frase):
    cripto = {}
    for i in frase:
        cripto[i] = {}
        for o in range(0,len(abc)):
            cripto[i][o]=abc[abc.index(i)+o-len(abc)]
    return cripto
"""
