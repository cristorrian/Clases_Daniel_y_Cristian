# -*- coding: UTF-8 -*-

class productos:
    # region Método constructor para la creación de cada objeto, (producto).
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    # endregion

    # region Método setter para cambiar el precio de un producto.
    def cambiar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
    # endregion

    # region Método setter para cambiar el stock de un producto.
    def cambiar_stock(self, nuevo_stock):
        self.stock = nuevo_stock
    # endregion

    # region Método getter para obtener la información de un producto.
    def mostrar_info_producto(self):
        print('Nombre: ' + self.nombre)
        print('Precio: ' + "{0:.2f}".format(self.precio) + '€')
        print('Stock: ' + str(self.stock))
    # endregion

# region Creamos los objetos (productos), y modificamos sus atributos para reflejar los cambios en pantalla posteriormente.
producto1 = productos('CocaCola - 2L', 2.00, 500)
producto1.mostrar_info_producto()
producto1.cambiar_precio(1.50)
producto1.cambiar_stock(200)
print()
producto1.mostrar_info_producto()
print('\n------------------------------------\n')
producto2 = productos('Fanta - 2L', 1.50, 300)
producto2.mostrar_info_producto()
producto2.cambiar_precio(1.20)
producto2.cambiar_stock(100)
print()
producto2.mostrar_info_producto()
# endregion