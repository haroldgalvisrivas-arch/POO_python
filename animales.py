class Animal:
    Alimentacion="carnibora" #Atributo de clase

    #Constructor de la clase: es el encargado de crearte el objeto
    def __init__(self, nombre, especie, edad):
        # Atributos de instancia: propios de cada odjeto
        self.nombre=nombre
        self.especie=especie
        self.edad=edad

    #Esto es un metodo de instancia; que es una funcion que pertenece a la clase y que puede acceder a los atributos de instancia y de clase. Siempre se define con verbos en infinitivo(ar,er,ir).
    def Ladrar(self): 
        #self hace referencia al nombre de la clase(Yo mismo)
        return f"{self.nombre} dice: Hey chico tengo hambre"


rex= Animal("Rex","Leon", 3)#Instancia de clase(Uso de los objetos)
luna = Animal("Luna","Tigre", 5)

#Acceder a atributros de la clase
print(f"{rex.nombre}: {rex.Alimentacion}")
print(f"{luna.nombre}: {luna.Alimentacion}")

#Acceso a los atributos de instancia
print(f"{rex.nombre} tiene {rex.edad} años y es un {rex.especie}")
print(f"{luna.nombre} tiene {luna.edad} años y es un {luna.especie}")

#Lamada a metodos de instancia
print(rex.Ladrar())
print(luna.Ladrar())