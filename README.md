class LoLItem:
    def __init__(self, id, nombre, precio, tipo, penetracion=0, dano_magico=0, dano_critico=0):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        self.penetracion = penetracion
        self.dano_magico = dano_magico
        self.dano_critico = dano_critico

# Simulación de base de datos
items = []

def create_item(id, nombre, precio, tipo, penetracion, dano_magico, dano_critico):
    item = LoLItem(id, nombre, precio, tipo, penetracion, dano_magico, dano_critico)
    items.append(item)
    return item

def read_items():
    return items

def update_item(id, nombre, precio, tipo, penetracion, dano_magico, dano_critico):
    for item in items:
        if item.id == id:
            item.nombre = nombre
            item.precio = precio
            item.tipo = tipo
            item.penetracion = penetracion
            item.dano_magico = dano_magico
            item.dano_critico = dano_critico
            return item
    return None

def delete_item(id):
    global items
    items = [item for item in items if item.id != id]