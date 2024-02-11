class rectangulo:
    def __init__(self, ancho, alto):
        self.ancho =  ancho
        self.alto = alto

    def area(self):
        a=self.ancho*self.alto
        print(f'El area es:{a}')

rectangulo_1 = rectangulo(10,20)
rectangulo_1.area()   
