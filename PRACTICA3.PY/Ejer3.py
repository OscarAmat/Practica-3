import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)


def main():
   
    radio_circulo = float(input("Ingrese el radio: "))
    nuevo_circulo = Circulo(radio_circulo)

  
    area_del_circulo = nuevo_circulo.calcular_area()
    print(f"El área del círculo es: {area_del_circulo:.2f}")

if __name__ == "__main__":
    main()

