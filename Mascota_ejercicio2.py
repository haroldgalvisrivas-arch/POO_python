class Mascota:
    # 2. Atributo de clase
    reino = "Animal"
    
    # 3. Atributo de clase para llevar el conteo
    total_mascotas = 0

    def __init__(self, nombre, especie):
        # Atributos de instancia
        self.nombre = nombre
        self.especie = especie
        # Incrementa en 1 cada vez que se crea una mascota
        Mascota.total_mascotas += 1


    # Reto final: metodo mostrar_total()
    @classmethod
    def mostrar_total(cls):
        print(f"Hay {cls.total_mascotas} mascotas registradas")


# 4. Crea 3 mascotas
m1 = Mascota("Firulais", "perro")
m2 = Mascota("Michi", "gato")
m3 = Mascota("Piolin", "ave")

# Imprime el total de mascotas, el reino de dos de ellas y el nombre de cada una
print(f"Total de mascotas: {Mascota.total_mascotas}")
print(f"{m1.reino} {m2.reino}")
print(f"{m1.nombre} {m2.nombre} {m3.nombre}")

print("\n--- RETO FINAL ---")
Mascota.mostrar_total()

#1. Que pasa con el total si borras una mascota con del m1?
#Si usas del m1 sin modificar la clase, el objeto desaparece de la memoria, pero el contador total_mascotas se mantiene igual (no disminuye), ya que por defecto Python solo incremento el contador al instanciar el objeto en el metodo __init__, pero no cuenta con una instruccion automatica que reste al destruir el objeto.

#2. Como lo solucionarias?
#Se puede solucionar de dos formas principales:

#Automatica: Implementando el metodo destructor __del__(self) dentro de la clase para que cada vez que se elimine una instancia con del, se reste uno al contador (Mascota.total_mascotas -= 1).

#Manual / Logica de negocio: Si el borrado de una mascota representa una baja logica en el sistema, se puede crear un metodo personalizado (por ejemplo, dar_de_baja()) que reste explicitamente el contador antes de eliminar el objeto.