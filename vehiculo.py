class Vehiculo:
    tipo = "Automovil"

    def __init__(self, nombre, modelo, cc):
        self.nombre=nombre
        self.modelo=modelo
        self.cc=cc

    def encender(self):
        return f"{self.nombre} esta listo para arrancar"

toyota=Vehiculo("Toyota","Corolla",2000)
ford=Vehiculo("Ford","Mustan GT",5000)

print(f"{toyota.nombre}: {toyota.tipo}")
print(f"{ford.nombre}: {ford.tipo}")

print(f"Marca: {toyota.nombre}, Modelo: {toyota.modelo}, CC: {toyota.cc}")
print(f"Marca: {ford.nombre}, Modelo: {ford.modelo}, CC: {ford.cc}")

print(toyota.encender())
print(ford.encender())