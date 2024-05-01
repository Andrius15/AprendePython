# Vamos a aprender POO (Programacion Orientada a Objetos)
# Una forma de programas realmente util en proyectos grandes
# Y que es facil de escalar si lo aplicas bien

# Para hacer una analigia, un objeto es casi como un paquete, pero mejor
# Imagina que quieres hacer coches. Podrias crearlos desde cero cada vez, o puedes usar prefabs
# Creas un 'creador de coches' que tiene todo lo que tiene un coche generico
# Y cuando vayas a fabricar un coche, le das lo especial en el momento
# Las clases son mas o menos eso: una forma de crear un creador de cosas
# Pero, esta vez, de lo que te de la gana (siempre que puedas programarlo)

# Vamos a aprender a crear clases
# Igual que para una funcion utilizamos 'def', para clases utilizamos 'class'

class Coche(): # En vez de 'def', 'class'. Por conveniencia, utilizamos mayusculas
    # Aqui dentro podemos meterle lo que queramos que tenga y haga

    # Estas variables se comparten dentro de la clase
    kilometraje : int = 0
    encendido : bool = False
    # La notacion lo aprendiste en AprendePython_4_Funciones.py

    # Funciones. Aunque cuando estamos dentro de una clase lo llamamos metodo
    def arrancar(self) -> None: # Ponemos 'self' para que este metodo sepa que esta dentro de la clase
        print('El coche a arrancado')
        self.encendido = True # El self permite acceder a todo lo que la clase tiene

    def estado(self) -> bool:
        return self.encendido

# De esta forma, tenemos nuestra primera clase
# Ahora, podemos crear tantos coches como querramos
coche1 = Coche() # Utilizamos corchetes, como si estubieramos ejecutanto la clase
coche2 = Coche() # A esto se llama instanciar, porque cremos instancias (copias) de la clase

# Una vez instanciado (creado las copias), podemos usarlas
print(coche1.estado()) # Usamos el punto para acceder a lo que esta dentro del objeto
# >>>False (apagado)
coche1.arrancar()
# >>>El coche a arrancado
print(coche1.estado())
# >>>True (encendido)
print(coche2.estado())
# >>>False
# Como puedes ver, lo que hagamos en el coche1 no afecta al coche2
# En proyectos reales, esto no solo permite separar los distintos usuarios y procesos, por ejemplo,
# si no que permite guardar todas las funciones relacionadas y organizar nuestro codigo

# ////////////////////////////////////////

# Vale, crear objetos esta bien, pero yo prometi poder darle peculiaridades
# Y eso es lo que vamos a hacer

del Coche, coche1, coche2 # Borramos lo anterior para rehacerlo

class Coche():
    def __init__(self, matricula : str, marca : str) -> None:
        # El __init__ es un metodo que se ejecuta automaticamente al instanciar
        # Por lo que a partir de esto podemos darle detalles a los objetos
        self.matricula : str= matricula
        self.marca : str = marca
        # De esta forma, guardamos la variable unica de la funcion en una variable para todo el objeto
        self.en_marcha : bool = False # Tambien podemos darles valores fijos
    
    def arrancar(self) -> None:
        print('Se ha encendido el coche')
        self.en_marcha = True
    
    def estado(self) -> str:
        if self.en_marcha:
            return 'Encendido'
        else:
            return 'Apagado'

# Ahora, creemos unos cohes

coche1 = Coche('123A', 'Toyota') # Les metemos esto como si fuera una funcion
coche2 = Coche('321B', 'Tesla') # Y asi se guarda

coche1.arrancar() # >>>Se ha encendido el coche
print(coche2.estado()) # >>>Apagado
print(coche1.estado()) # >>>Encendido
# Hasta ahora, nada nuevo
# Pero eso es porque no lo hemos probado:
print(coche1.matricula) # >>>123A
print(coche2.marca) # >>>Tesla
# Esta vez, lo que le dimos a Coche() es lo que se guarda
# De esta forma, tenemos mucho potencial para creacion de proyectos
# En proyectos pequennos o que no modificaras mucho, a lo mejor las clases no te sirven
# Pero, como veras mas adelante, las clases son la clave si quieres:
# hacer tu codigo legible, ordenado y facilmente modificable

# ////////////////////////////////////////////////////

# Antes de pasar a un proyecto, aprendamos otra de las ventajas de POO
# Imagina que quieres hacer varias clases, pero que todas ellas compartan caracteristicas
# Aqui entra la Herencia
# Como en la realidad, lo que tenga el padre pasa al hijo
# Aprovechemos lo de antes

class Toyota(Coche): # Para heredar, metemos el padre aqui
    def __init__(self, matricula: str) -> None: # Esto reescribe lo que sea que tiene el padre
        super().__init__(matricula, 'Toyota') # Pero esto usa lo del padre antes de eso
        # Lo que hace es utilizar lo que tiene el padre metiendole esos datos
        # La matricula se pone a la hora de crear el coche,
        # pero la marca es fija para esta clase
        self.kilometros : int = 0 # Esto SOLO lo tendra esta clase, no la clase Coche()
    
    def kilometraje(self) -> int:
        return self.kilometros

    def moverse(self) -> None:
        if self.en_marcha:
            self.kilometros += 1
        else:
            print('Enciende el vehiculo')

class Tesla(Coche):
    def __init__(self, matricula: str) -> None:
        super().__init__(matricula, 'Tesla')
        self.energia : int = 2
    
    def bateria(self) -> int:
        return self.energia
    
    def cargar(self) -> None:
        print('Se ha cargado el coche')
        self.energia += 1
        print('Bateria actual:', self.bateria()) # Es mas profecional usar funciones para acceder a los datos
    
    def moverse(self) -> None:
        if self.energia > 0 and self.en_marcha:
            print('Te has movido')
            self.energia -= 1
        elif not self.en_marcha:
            print('Enciende el vehiculo')
        else:
            print('No tienes bateria')

# Ahora, probemos lo que acabamos de hacer
Alice = Toyota('223D') # Solo necesitamos esto
Bob = Tesla('675H')

# Ahora, mira esto:
Alice.moverse() # >>>Enciende el vehiculo
Alice.arrancar() # >>>Se ha encendido el coche
# Como es esto posible? No hemos definido arrancar() en la clase Toyota()
# Pues esa es la magia de la Herencia: no solo te haces rico, puedes usar lo que tus padre hicieron
# Pero Alice no puede cargar su coche, eso solo lo puede hacer Bob
Bob.cargar()
# >>>Se ha cargado el coche
# >>>Bateria actual: 3
Bob.estado()
# >>>Apagado
try:
    Alice.cargar()
except AttributeError:
    print('Alice no tiene un Tesla, por lo que su coche no necesita electricidad')
# >>>Alice no tiene un Tesla, por lo que su coche no necesita electricidad
# Como ves, las clases Toyota() y Tesla() tienen todo lo que tiene Coche()
# Mas todo aquello que se definen para ellos. Pero no lo que tiene el otro
# Esa es la magia del POO
# Y, si quisiera, seria capaz de crear un Tesla helicoptero
# Tan solo tendria que heredar la clase Tesla y crear un nuevo metodo moverse()
# Y annadir lo que sea que haga un helicoptero, sin necesidad de repetir el trabajo anterior

# /////////////////////////////////////////////////

# Antes de pasar al proyecto final, aprenderemos una ultima cosa:
# Que pasa si quiero saber cual es el tipo de coche de George?
# O si, para evitar problemas, impido a Bob a entra en un club por su coche?
# Para eso existe el isintance()

print(isinstance(Bob, Tesla)) # >>>True
print(isinstance(coche1, Coche)) # >>>True
print(isinstance(Alice, Coche)) # >>>True
print(isinstance(Alice, Tesla)) # >>>False
print(isinstance(coche1, Tesla)) # >>>False

# isinstance() toma en primer lugar un objeto. En segundo lugar, una clase
# Al final, devuelve True o False segun el objeto es una instancia de la clase
# Date cuenta que, necesariamente, si una clase es hijo de otra, las instancias se comparten
# Es decir, si Tesla hereda de Coche, todas las instancias de Tesla tambien lo son de Coche
# De ahi que Alice sea una instancia de Coche, anque hayamos usado Tesla() para la instancia

# //////////////////////////////////////////////////////

# Pues ya esta. Si ahora pasas a la carpeta 'Proyectos', veras que te espera tu ultima clase
# Ha sido un placer

