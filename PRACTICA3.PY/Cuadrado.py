class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2


lado = float(input("Ingresa el lado: "))

area_cuadrado = Cuadrado(lado)
area = area_cuadrado.calcular_area()

print(f"El área es: {area}")
