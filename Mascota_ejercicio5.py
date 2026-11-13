from abc import ABC, abstractmethod

# 2. Creacion de la clase abstracta Animal
class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def hacer_sonido(self):
        pass

    # Reto final: Segundo metodo abstracto 'moverse()'
    @abstractmethod
    def moverse(self):
        pass


# 3. Clases hijas que heredan e implementan los metodos abstractos
class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"
    
    def moverse(self):
        return "corre"


class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"
    
    def moverse(self):
        return "camina sigilosamente"


class Vaca(Animal):
    def hacer_sonido(self):
        return "¡Muuu!"
    
    def moverse(self):
        return "camina pesadamente"


# Reto final: Clase Pajaro añadida sin alterar la estructura del ciclo principal
class Pajaro(Animal):
    def hacer_sonido(self):
        return "¡Pío!"
    
    def moverse(self):
        return "vuela"


# 4. Guardar un objeto de cada clase en una lista y recorrerla con un ciclo for
animales = [
    Perro("Firulais"),
    Gato("Michi"),
    Vaca("Lola"),
    Pajaro("Pablito")  # Añadido del reto final
]

print("--- SONIDOS (Polimorfismo) ---")
for animal in animales:
    print(f"{animal.nombre}: {animal.hacer_sonido()}")


print("\n--- MOVIMIENTOS (Segundo metodo abstracto del Reto) ---")
for animal in animales:
    print(f"El {animal.especie if hasattr(animal, 'especie') else animal.__class__.__name__.lower()} {animal.nombre} {animal.moverse()}.")


# 5. Intentar crear un objeto directamente de Animal y observar el error
print("\n--- PRUEBA DE CLASE ABSTRACTA ---")
try:
    # Las clases abstractas con metodos sin implementar no pueden instanciarse directamente
    animal_generico = Animal("ErrorTest")
except TypeError as e:
    print(f"Error capturado exitosamente: {e}")