def suma(a, b):
    try:
        return a + b
    except TypeError:
        raise ValueError("Error: Tipo de dato no válido.")

def resta(a, b):
    try:
        return a - b
    except TypeError:
        raise ValueError("Error: Tipo de dato no válido.")

def producto(a, b):
    try:
        return a * b
    except TypeError:
        raise ValueError("Error: Tipo de dato no válido.")

def division(a, b):
    try:
        if a == 0:
            raise ValueError("Error: No es posible dividir entre cero.")
        return a / b
    except TypeError:
        raise ValueError("Error: Tipo de dato no válido.")