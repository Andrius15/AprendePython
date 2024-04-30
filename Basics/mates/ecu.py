from math import sqrt,gcd,fabs

# Minimo Comun Multiplo
def MCD(*n):
    if n[0] < 0:
        alln = True
    else:
        alln = False
    for i in n[1:]:
        if i > 0 and alln:
            alln = False
            break
    if alln:
        return -gcd(*n)
    return gcd(*n)

# Maximo Comun Divisor
def MCM(*n):
    r = 1
    for i in n:
        r *= i
    return r / gcd(*n)

# Divisores de un numero
def div(n):
    n = int(fabs(n))
    div_l = []
    for i in range(1,n+1):
        if n%i == 0:
            div_l.append(i)
    return div_l

# Divisores de un numero incluyendo negativos
def divT(n):
    n = int(fabs(n))
    div_l = []
    for i in range(1,n+1):
        if n%i == 0:
            div_l.append(i)
            div_l.append(i*(-1))
    return div_l

# Ecuacion de primer grado (y = ax + b)
def ec1(a=1,b=1):
    if b >= 0: s = '+'
    else: s = ''
    fx = f'{a}x{s}{b} = 0'
    try:
        return fx, (-b)/a
    except ZeroDivisionError:
        print('El procedimiento me da division de 0')
    return f'La funcion que introdujiste era: "{fx}"'

# Ecuacion de segundo grado (ax^2 + bx +c)
def ec2(a,b=0,c=0):
    if b >= 0: s1 = '+'
    else: s1 = ''
    if c >= 0: s2 = '+'
    else: s2 = ''
    fx = f'{a}x²{s1}{b}x{s2}{c} = 0'
    v1, v2 = None, None
    try:
        v1 = ((-b)+(sqrt((b**2)-(4*a*c))))/(2*a)
        v2 = ((-b)-(sqrt((b**2)-(4*a*c))))/(2*a)
        if v1 == v2:
            return fx, v1
        return fx, (v1,v2)
    except ZeroDivisionError:
        print('El procedimiento me da division de 0')
    except ValueError:
        print('He tenido que hacer una raiz cuadrada de un numero negativo')
        print('Esta calculadora no está diseñada para eso')
    except:
        print('Ha ocurrido un error')
    return f'La funcion que introdujiste era: "{fx}"'

def ec2t1(a=0,c=0):
    if c >= 0: s2 = '+'
    else: s2 = ''
    fx = f'{a}x²{s2}{c} = 0'
    try:
        if sqrt((-c)/a) == int(sqrt((-c)/a)):
            v1 = int(sqrt((-c)/a)),int(sqrt((-c)/a))*-1
        else:
            v1 = sqrt((-c)/a),sqrt((-c)/a)*-1
        return fx, v1
    except ZeroDivisionError:
        print('El procedimiento me da division de 0')
    except ValueError:
        print('He tenido que hacer una raiz cuadrada de un numero negativo')
        print('Esta calculadora no está diseñada para eso')
    except:
        print('Ha ocurrido un error')
    return f'La funcion que introdujiste era: "{fx}"'

def ec2t2(a=0,b=0):
    if b >= 0: s1 = '+'
    else: s1 = ''
    fx = f'{a}x²{s1}{b}x = 0'
    d = MCD(a,b)
    v1 = 0
    v2 = [int(a/d),int(b/d)]
    print(f'{v2[0]}x{s1}{v2[1]} = 0')
    v2 = ec1(v2[0],v2[1])
    return fx, (0,v2[1])

# Polinomio. De izquierda a derecha, crea un polinomio de grado len(divs)
def pol(*divs): #Divisor como una lista, diviendo como diccionario
    divs = list(divs)
    divs.reverse() # Invierte la ecuación
    g = 0
    fx = [] # Crea el lugar para guardar las ecuaciones
    # divs = divisor
    for i in divs:
        if i == 0: pass
        elif g == 0: # Si es el termino independiente, lo añade sin mas
            if i > 0: fx.append('+' + str(i))
            else: fx.append(str(i))
        elif g == 1:
            if i<0:
                fx.append(f'{i}x')
            else:
                fx.append(f'+{i}x')
        else:
            if i<0:
                fx.append(f'{i}x^{g}')
            else:
                fx.append(f'+{i}x^{g}')
        g += 1
    fx.reverse()
    fx = ' '.join(fx)
    return fx

# Lo contrario a lo de arriba: recive un polinomio y lo desglosa en raices
def unpol(divs):
    divs = divs.split() # Divide en monomios
    for i in range(0,len(divs)):
        divs[i] = divs[i].split('^') # Etiueta cada monomio segun su grado
        if 'x' in divs[i][0]: # Si no se ha puesto su grado, le pone grado 1
            if len(divs[i]) < 2: divs[i].append(1)
            continue
        divs[i].append(0) # Si nisiquiera tiene parte literal, le pone grado 0
    Ddivs = {}
    for i in divs:
        try:
            Ddivs[i[1]] += int(i[0][:-1])
        except KeyError:
            Ddivs[i[1]] = 0
            try:
                Ddivs[i[1]] += int(i[0][:-1])
            except ValueError:
                Ddivs[i[1]] += int(i[0])
        except:
            print('Algo ha salido mal')
    return Ddivs

# unpol('+2x^2 -2x -2x +4x^2 +1')

# Hace ruffini. Devuelve ['original', ('divisores', resto)]
def ruffi(a,*ixn):
    fxs = [pol(*ixn),[]]
    xn = 0
    for i in ixn:
        xn += i
        fxs[1].append(xn)
        xn *= a
    fxs[1] = pol(*fxs[1][:-1]), fxs[1][-1]
    return fxs

# Lo mismo de arriva, pero en lenguaje humano
def ruffiL(a,*ixn):
    fxs = ruffi(a,*ixn)
    print('Polinomio original:',fxs[0])
    if a > 0: print(f'Divisor: (x-{a})')
    elif a == 0: print('Divisor: x')
    else: print(f'Divisor: (x+{a*-1})')
    print('Resultado:',fxs[1][0])
    if fxs[1][1] == 0: print('¡Es exacta!')
    else: print('Resto:', fxs[1][1])

# Un generador que devuelve lo que rufini
def forru(*ixn):
    for i in divT(ixn[-1]):
        yield ruffi(i,*ixn),i

# Ejecuta el for directamente
def forruf(*ixn):
    for i in forru(*ixn):
        print(i)

# Factoriza un polinomio
def facPol(*pol):
    a = forru(*pol)
    for i in a:
        if not i[0][1][-1]:
            print(i[-1])
