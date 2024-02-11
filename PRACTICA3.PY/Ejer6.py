class Producto:
    def __init__(self, nombre, precio, año, marca, origen):
        self.nombre = nombre
        self.precio = precio
        self.año = año
        self.marca = marca
        self.origen = origen

    def __str__(self):
        return f"{self.nombre} - {self.marca} - {self.año} - {self.precio} - {self.origen}"


class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def filtrar_año(self, año):
        return [producto for producto in self.productos if producto.año == año]


catalogo = Catalogo()

producto1 = Producto("retroviores", 500 , 2019, "Honda", "Japon")
catalogo.agregar_producto(producto1)
producto2 = Producto("Llanta", 320, 2022, "Porche", "Alemania")
catalogo.agregar_producto(producto2)
producto3 = Producto("Timon", 170, 1975, "Chevrolet", "USA")
catalogo.agregar_producto(producto3)
producto4 = Producto("Tubo de escape", 420, 1998, "Ferrari", "Italia")
catalogo.agregar_producto(producto4)



print("Todos los productos:")
catalogo.mostrar_productos()

print("\nProductos filtrados por año 1998:")
productos_filtrados_por_año = catalogo.filtrar_año (1998)
for producto in productos_filtrados_por_año:
    print(producto)