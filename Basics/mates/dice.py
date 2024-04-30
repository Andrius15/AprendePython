import random

def dado(c=6):
    return random.randint(1,c)

def dadoh(c=6,t=1000):
    d = {i:0 for i in range(1,c+1)}
    history = tuple(dado(c) for i in range(0,t))
    for i in history:
        for o in d:
            if i == o:
                d[i] += 1
    return d,history

def dados(n=2,c=6,t=1000):
    d = {i:0 for i in range(n,(c*n)+1)}
    history = []
    for XXXX in range(0,t):
        suma = 0
        for i in range(0,n):
            suma += dado(c)
        history.append(suma)
    for i in history:
        for o in d:
            if i == o:
                d[i] += 1
    history = tuple(history)
    return d,history

def P(dic,elem=None):
    if type(dic) != dict:
        try:
            dic = dic[0]
        except AttributeError:
            print('Dame un diccionario, por favor')
            return 0
        except:
            print('Alfo ha salido mal')
            return 0
    sum = [i for i in dic.values()]
    total = 0
    for i in sum:
        total += i
    del sum
    prob = {}
    for i in dic:
        prob[i] = round(dic[i]/total*100 ,2)
    if elem and elem in prob:
        return prob[elem]
    return prob

def bolsa(*elem):
    return random.choice(elem)

def bolsah(t=100,*elem):
    d = {i:0 for i in elem}
    history = tuple(random.choice(elem) for i in range(0,t))
    for i in history:
        for o in d:
            if i == o:
                d[i] += 1
    return d,history

# + Añadir un modulo 'Pn' o parecido para calcular probabilidades de listas (bolsas) sin tener el diccionario
# + Añadir un modulo (dados) pero que en vez de sumarlos, los reste