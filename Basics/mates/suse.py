
## Susecion de fibonachi
def F(n):
    a,b=0,1
    while a<=n:
        print(a,end=' / ')
        a,b=b,a+b
    print()

def nF(n):
    a,b=0,1
    for i in range(0,n):
        print(a,end=' / ')
        a,b=b,a+b
    print()

## Pregresiones matematicas
# Aritmeticas
def an(a1,d,n): # La normal
    an = a1+(n-1)*d
    return an

def a1(an,d,n): # Descubrir a1
    a1 = an-(n-1)*d
    return a1

def ad(a1,an,n): # Descubrir d
    d =(an-a1)/(n-1)
    return d

def na(a1,an,d): # Descubrir n
    n = ((an-a1+d)/d)
    return n

def Sa(a1,d,n): # La suma
    Sn=((a1+ an(a1,d,n) )*n)/2
    return Sn

# Geometricas
def gn(g1,r,n): # La normal
    gn = g1*r**(n-1)
    return gn

def Sg(g1,r,n): # La suma
    Sn = (g1*((r**n)-1))/(r-1)
    if r<1:
        print(f'La suma infinita es {g1}/{1-r}')
    return Sn
