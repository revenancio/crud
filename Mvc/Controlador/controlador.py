from Modelo.Modelo import LolItem
from Modelo.Modelo import items
class Controlador :

#definimos la funcion initque  almacenara los objetos items en una lista
    def __init__(self):
        self.items = [] #lista donde se almacenan los nuevos objetos creados

#creamos funcion agregar ojetos para poder agregar objetos a la lista usando  
#append para agregar el objeto al final de la lista
    def agregar_objeto(self, id, nombre, precio, tipo, penetracion=0, danomagico=0, danocritico=0):
        nuevo_objeto = LolItem(id, nombre, precio, tipo, penetracion, danomagico, danocritico)
        self.items.append(nuevo_objeto)
        print(f"Objeto{nombre} agregado exxitosamente.")

#creamos la funcion leer objeto para poder buscar un objeto en la lista
#usamos un for para recorrer la lista y un if para comparar el id del objeto
#con el id que se busca
    def mostrar_objetos(self):
        if not self.items:
            print("No hay objetos para mostrar.")
        else:
            for item in self.items:
                print(f"ID: {item.id}, Nombre: {item.nombre}, Precio: {item.precio}, Tipo: {item.tipo}, "
                      f"Penetración: {item.penetracion}, Daño Mágico: {item.danomagico}, Daño Crítico: {item.danocritico}")

#creamos la funcion actualizar objeto para poder modificar un objeto en la lista
#usamos un for para recorrer la lista y un if para comparar el id del objeto
#con el id que se busca
    def actualizar_objeto(self, id, nuevo_precio, nueva_penetracion, nuevo_dano_magico, nuevo_dano_critico):
        for item in self.items:
            if item.id == id:
                item.precio = nuevo_precio
                item.penetracion = nueva_penetracion
                item.danomagico = nuevo_dano_magico
                item.danocritico = nuevo_dano_critico
                print(f"Objeto {item.nombre} actualizado exitosamente.")
                return
        print("Objeto no encontrado.")
#creamos la funcion eliminar objeto para poder eliminar un objeto en la lista
#usamos un for para recorrer la lista y un if para comparar el id del objeto
#con el id que se busca
    def eliminar_objeto(self, id):
        for item in self.items:
            if item.id == id:
                self.items.remove(item)
                print(f"Objeto {item.nombre} eliminado exitosamente.")
                return
        print("Objeto no encontrado.")