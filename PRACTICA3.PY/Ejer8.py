import random

def generar_numeros():
    return [random.randrange(0, 101) for _ in range(20)]

def generar_lista(lista):
    print("Lista obtenida:", lista)

def mostrar(lista):
    lista_creada = sorted(lista)
    print("Lista:", lista_creada)