class Mascota:
    def __init__(self, nombre, dueno, edad, peso=10):
        self.nombre = nombre        # 1. Atributo publico
        self._dueno = dueno         # 1. Atributo protegido (un guion bajo)
        self.__edad = edad          # 1. Atributo privado (dos guiones bajos)[cite: 3]
        self.__peso = peso          # Reto final: atributo privado __peso

    # 2. Metodo get_edad() que devuelva la edad[cite: 3]
    def get_edad(self):
        return self.__edad

    # 3. Metodo set_edad(nueva_edad) con validacion[cite: 3]
    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            print("Error: la edad no puede ser negativa")

    # Reto final: get_peso() y set_peso()
    def get_peso(self):
        return self.__peso

    def set_peso(self, nuevo_peso):
        # El peso debe ser mayor que 0 y no puede superar los 100 kg[cite: 4]
        if 0 < nuevo_peso <= 100:
            self.__peso = nuevo_peso
        else:
            print("Error: el peso no es valido. Debe ser mayor a 0 y maximo 100 kg")


# 4. Creacion del objeto e interacciones[cite: 3]
m = Mascota("Firulais", "Ana", 0)

# Leer el nombre (publico)[cite: 3]
print(m.nombre)

# Leer el dueño (protegido)[cite: 3]
print(m._dueno)

# Cambiar la edad a -5 y luego a 4[cite: 3]
m.set_edad(-5)
m.set_edad(4)

# Imprimir la edad mediante el metodo get_edad()[cite: 3]
print(m.get_edad())

# 4. Intentar imprimir __edad directamente genera un error (AttributeError)[cite: 3]
try:
    print(m.__edad)
except AttributeError:
    print("Nota: No se puede acceder a '__edad' directamente desde fuera de la clase debido al name mangling (ocultamiento).")


print("\n--- PRUEBA DEL RETO FINAL (Peso) ---")
m.set_peso(150)  # Invalido (> 100 kg)[cite: 4]
m.set_peso(-5)   # Invalido (<= 0 kg)[cite: 4]
m.set_peso(25)   # Valido
print(f"Peso actual de la mascota: {m.get_peso()} kg")