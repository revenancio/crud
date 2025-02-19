#creamos el molde de los objetos que se van a crear
class LolItem: 
    def __init__(self, id, nombre, precio, tipo, penetacion=0, dano_magico=0, danocritico=0):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        self.penetacion = penetacion
        self.dano_magico = dano_magico
        self.danocritico = danocritico

#simulacion de base de datos 
items = [] #lista donde se almacenan los nuevos objetos creados

#creamos las funciones del crud 
#CRUD
#Create - Read - Update - Delete
def create_item(id, nombre, precio, tipo, penetacion=0, dano_magico=0, danocritico=0):
    item = LolItem(id, nombre, precio, tipo, penetacion, dano_magico, danocritico)
    items.append(item)
    return item
def read_item(id):
    for item in items:
        if item.id == id:
            return item
    return None

def update_item(id, nombre, precio, tipo, penetacion, dano_magico, danocritico):
    for item in items:
        if item.id == id:
            item.nombre = nombre
            item.precio = precio
            item.tipo = tipo
            item.penetacion = penetacion
            item.dano_magico = dano_magico
            item.danocritico = danocritico
            return item
        
def delete_item(nombre):
    global items
    item = [item for item in items if item.nombre != nombre]