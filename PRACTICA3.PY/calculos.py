import operaciones


a = 40
b = 16


try:
    print(f"Resultado de suma: {operaciones.suma(a, b)}")
except ValueError as e:
    print(e)


try:
    print(f"Resultado de resta: {operaciones.resta(a, b)}")
except ValueError as e:
    print(e)


try:
    print(f"Resultado de producto: {operaciones.producto(a, b)}")
except ValueError as e:
    print(e)


try:
    print(f"Resultado de división: {operaciones.division(a, b)}")
except ValueError as e:
    print(e)
