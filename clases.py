# Atributos de clase: Son caracteristicas comunes a todos los objetos de una clase.
#Se define dentro de la clase pero fuera de cualquier metodo.
# Se accede a ellos mediante las clases o mediante un objeto de la clase.

class Perro:
    especie="cani familiaris" #Atributo de clase

    #Constructor de la clase: es el encargado de crearte el objeto
    def __init__(self, nombre, edad):
        # Atributos de instancia: propios de cada odjeto
        self.nombre=nombre
        self.edad=edad

    #Esto es un metodo de instancia; que es una funcion que pertenece a la clase y que puede acceder a los atributos de instancia y de clase. Siempre se define con verbos en infinitivo(ar,er,ir).
    def Ladrar(self): 
        #self hace referencia al nombre de la clase(Yo mismo)
        return f"{self.nombre} dice: ¡Guau!"


rex= Perro("Rex", 3)#Instancia de clase(Uso de los objetos)
luna = Perro("Luna", 5)

#Acceder a atributros de la clase
print(f"{rex.nombre}: {rex.especie}")
print(f"{luna.nombre}: {luna.especie}")

#Acceso a los atributos de instancia
print(f"{rex.nombre} tiene {rex.edad} años")
print(f"{luna.nombre} tiene {luna.edad} años")

#Lamada a metodos de instancia
print(rex.Ladrar())
print(luna.Ladrar())


class Contador:
    total = 0 # de clase
    def __init__(self):
        Contador.total += 1 # modifica el valor compartido
        self.numero = Contador.total # de instancia

a = Contador()
b = Contador()
print(a.numero, b.numero, Contador.total) # 1 2 2


class Mal:
    items = [] # compartida por todos: casi siempre un error

class Bien:
    def __init__(self):
        self.items = [] # una lista independiente por objeto


class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo # variable privada (__variable)

    def depositar(self, monto):
        if monto <= 0:
         raise ValueError("El monto debe ser positivo")
        self.__saldo += monto

    def retirar(self, monto):
        if monto > self.__saldo:
            raise ValueError("Fondos insuficientes")
        self.__saldo -= monto

    def consultar_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria("Ana", 1000)
cuenta.depositar(500)
print(cuenta.consultar_saldo()) # 1500
# print(cuenta.__saldo)  # AttributeError


class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius # pasa por el setter

    @property # es un decorador
    def celsius(self):
        return self._celsius # variable protegida (_variable)
    
    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("Por debajo del cero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self): # propiedad calculada, solo lectura
        return self._celsius * 9 / 5 + 32

t = Temperatura(25)
print(t.fahrenheit) # 77.0
t.celsius = 30 # usa el setter con validación