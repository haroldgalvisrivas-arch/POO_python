class Mascota:
    # 2. Dentro del constructor __init__ recibe y guarda tres atributos: nombre, especie y edad
    def __init__(self, nombre, especie, edad=0):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad  # Añadido para el reto final

    # 3. Crea un metodo presentarse() que imprima una frase con los datos de la mascota.
    def presentarse(self):
        print(f"Hola, soy {self.nombre} y soy un {self.especie}")

    # Reto final: metodo cumplir_anios() que sume 1 a la edad e imprima un mensaje.
    def cumplir_anios(self):
        self.edad += 1
        print(f"{self.nombre} ahora tiene {self.edad} años.")


# 4. llama a presentarse() en cada uno.
mascota1 = Mascota("Firulais", "perro", 3)
mascota2 = Mascota("Michi", "gato", 2)

mascota1.presentarse()
mascota2.presentarse()

print("\n--- PRUEBA DEL RETO FINAL ---")
# Crea una mascota y haz que cumpla años dos veces seguidas.
mascota3 = Mascota(
    "Firulais", "perro", 3
)  # Usando a Firulais con edad inicial de 3 años
mascota3.cumplir_anios()  # Sube a 4 años
mascota3.cumplir_anios()  # Sube a 5 años