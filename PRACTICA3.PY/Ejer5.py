class Alumno:
    

    def __init__(self, nombre, n_registro):
        self.nombre=str(nombre)
        self.n_registro=int(n_registro)
        self.edad=[]
        self.nota=[]
    
   
    def display(self):
        print(f'Nombre: {self.nombre}   Numero de registro: {self.n_registro}')

    def set_edad(self, edad):
        self.edad = edad

    def set_nota(self, nota):
        self.nota = nota
    
alumno1=Alumno('Oscar',11)
alumno1.set_edad(25)
alumno1.set_nota(20)

alumno1.display()
print(f'edad {alumno1.edad}')
print(f'nota {alumno1.nota}')