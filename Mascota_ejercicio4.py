# 1. Clase padre Mascota
class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo")


# 2. Clase Perro que hereda de Mascota
class Perro(Mascota):
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Reutiliza el constructor del padre
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")


# 3. Clase Gato que hereda de Mascota
class Gato(Mascota):
    def __init__(self, nombre, color):
        super().__init__(nombre)  # Reutiliza el constructor del padre
        self.color = color

    def maullar(self):
        print(f"{self.nombre} dice: ¡Miau!")


# Reto final: Clase Cachorro que hereda de Perro (herencia de dos niveles)
class Cachorro(Perro):
    def jugar(self):
        print(f"{self.nombre} está jugando")


# 4. Creacion de un perro y un gato, llamando a sus metodos
perro1 = Perro("Firulais", "Criollo")
gato1 = Gato("Michi", "Blanco")

perro1.comer()
perro1.ladrar()

gato1.comer()
gato1.maullar()


print("\n--- PRUEBA DEL RETO FINAL (Cachorro) ---")
# Comprobando que un cachorro puede usar comer(), ladrar() y jugar()
cachorro1 = Cachorro("Max", "Pug")
cachorro1.comer()   # Metodo heredado de Mascota
cachorro1.ladrar()  # Metodo heredado de Perro
cachorro1.jugar()   # Metodo propio de Cachorro


#De que clases hereda un Cachorro?
#Un objeto de la clase Cachorro hereda directamente de la clase Perro, y de manera indirecta (herencia multinivel) tambien hereda de la clase padre principal Mascota (debido a que Perro desciende de Mascota). Esto le permite acceder a los metodos y atributos de ambas clases superiores (comer, ladrar, etc.)