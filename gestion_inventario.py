"""
Examen: Gestión de Inventario con Persistencia JSON y Programación Orientada a Objetos
Autor/a: Iván Gómez Jiménez_______________________________________
Fecha: _04/11/2025_________________________________________

Objetivo:
Desarrollar una aplicación orientada a objetos que gestione un inventario de productos
con persistencia de datos en ficheros JSON y uso de listas y diccionarios anidados.

Clases requeridas:
- Proveedor
- Producto
- Inventario

"""

import json
import os


# ======================================================
# Clase Proveedor
# ======================================================

class Proveedor:
    def __init__(self, codigo:str, nombre:str, contacto:str):
        self.codigo = codigo
        self.nombre = nombre
        self.contacto = contacto

    def __str__(self):
        return f"Codigo: {self.codigo} Nombre: {self.nombre} Contacto: {self.contacto}"


# ======================================================
# Clase Producto
# ======================================================

class Producto:
    def __init__(self, codigo, nombre, precio, stock, proveedor):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.proveedor = proveedor

    def __str__(self):

        return f"[{self.codigo}] {self.nombre} - {self.precio} € | Proveedor {self.proveedor.nombre} ({self.proveedor.contacto})"
        # TODO: devolver una representación legible del producto
        # Ejemplo: "[P001] Teclado - 45.99 € (10 uds.) | Proveedor: TechZone (ventas@techzone.com)"


# ======================================================
# Clase Inventario
# ======================================================

class Inventario:
    def __init__(self, nombre_fichero:str):
        self.nombre_fichero = nombre_fichero
        self.productos = []

    def cargar(self):
        """
        Carga los datos del fichero JSON si existe y crea los objetos Producto y Proveedor.
        Si el fichero no existe, crea un inventario vacío.
        """
        try:
            with open("inventario.json", "r") as f:
                datos = json.load(f)
            for producto in datos:
                proveedor = Proveedor(producto["proveedor"]["codigo"], producto["proveedor"]["nombre"], producto["proveedor"]["contacto"])
                p1 = Producto(producto["codigo"], producto["nombre"], producto["precio"], producto["stock"], proveedor)
                self.productos.append(p1)
        except FileNotFoundError:
            self.productos = []

        # TODO: implementar la lectura del fichero JSON y la creación de objetos
        pass

    def guardar(self):
        """
        Guarda el inventario actual en el fichero JSON.
        Convierte los objetos Producto y Proveedor en diccionarios.
        """
        datos = []

        for producto in self.productos:
            productodict = {"codigo":producto.codigo, "nombre": producto.nombre, "precio": producto.precio, "stock":producto.stock, "proveedor": {"codigo": producto["proveedor"]["codigo"], "nombre": producto["proveedor"]["nombre"], "contacto": producto["proveedor"]["contacto"]}}
            datos.append(productodict)

        with open("inventario.json", "w", encoding="utf-8") as f:
            json.dump(f, datos, indent=4, ensure_ascii=False) 

        # TODO: recorrer self.productos y guardar los datos en formato JSON

    def anadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario si el código no está repetido.
        """
        # TODO: comprobar si el código ya existe y, si no, añadirlo

        for p in self.productos:
            if p.codigo == producto.codigo:
                print("El producto ya esta añadido en la lista")    
                return
        
        self.productos.append(producto)
        print("Producto añadido")

    def mostrar(self):
        """
        Muestra todos los productos del inventario.
        """
        # TODO: mostrar todos los productos almacenados
        for producto in self.productos:
           print(producto)

    def buscar(self, codigo):
        """
        Devuelve el producto con el código indicado, o None si no existe.
        """
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto

    def modificar(self, codigo, nombre=None, precio=None, stock=None):
        """
        Permite modificar los datos de un producto existente.
        """
        # TODO: buscar el producto y actualizar sus atributos
        

    def eliminar(self, codigo):
        """
        Elimina un producto del inventario según su código.
        """
        # TODO: eliminar el producto de la lista
        pass

    def valor_total(self):
        """
        Calcula y devuelve el valor total del inventario (precio * stock).
        """
        # TODO: devolver la suma total del valor del stock
        pass

    def mostrar_por_proveedor(self, nombre_proveedor):
        """
        Muestra todos los productos de un proveedor determinado.
        Si no existen productos de ese proveedor, mostrar un mensaje.
        """
        # TODO: filtrar y mostrar los productos de un proveedor concreto
        pass


# ======================================================
# Función principal (menú de la aplicación)
# ======================================================

def main():
    # TODO: crear el objeto Inventario y llamar a los métodos según la opción elegida
    i1 = Inventario("inventario.json")
    i1.cargar()
    while True:
        print("\n=== GESTIÓN DE INVENTARIO ===")
        print("1. Añadir producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Calcular valor total")
        print("7. Mostrar productos de un proveedor")
        print("8. Guardar y salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            codigo = input("Introduce el codigo")
            nombre = input("Introduce el nombre")
            precio = float(input("Introduce el precio"))
            stock = int(input("Introduce el stock"))

            pr1 = Proveedor(None, None, None)
            p = Producto(codigo, nombre, precio, stock, pr1)
            i1.anadir_producto(p)
        elif opcion == 2:
            i1.mostrar()
        elif opcion == 3:
            codigo_buscado = input("Introduce un codigo")
            print(i1.buscar(codigo_buscado))
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass
        elif opcion == 8:
            i1.guardar()
            break



if __name__ == "__main__":
    main()
