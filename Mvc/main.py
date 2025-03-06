import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from Controlador.controlador import Controlador

class CRUDApp(QWidget):
    def __init__(self):
        super().__init__()
        self.controlador = Controlador()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('OBJJETOS DE LOL')
        self.setGeometry(400, 400, 800, 600)

        layout = QVBoxLayout()

        self.id_input = QLineEdit(self)
        self.id_input.setPlaceholderText('ID')
        layout.addWidget(self.id_input)

        self.nombre_input = QLineEdit(self)
        self.nombre_input.setPlaceholderText('Nombre')
        layout.addWidget(self.nombre_input)

        self.precio_input = QLineEdit(self)
        self.precio_input.setPlaceholderText('Precio')
        layout.addWidget(self.precio_input)

        self.tipo_input = QLineEdit(self)
        self.tipo_input.setPlaceholderText('Tipo')
        layout.addWidget(self.tipo_input)

        self.penetracion_input = QLineEdit(self)
        self.penetracion_input.setPlaceholderText('Penetración')
        layout.addWidget(self.penetracion_input)

        self.dano_magico_input = QLineEdit(self)
        self.dano_magico_input.setPlaceholderText('Daño Mágico')
        layout.addWidget(self.dano_magico_input)

        self.dano_critico_input = QLineEdit(self)
        self.dano_critico_input.setPlaceholderText('Daño Crítico')
        layout.addWidget(self.dano_critico_input)

        self.agregar_btn = QPushButton('Agregar Objeto', self)
        self.agregar_btn.clicked.connect(self.agregar_objeto)
        layout.addWidget(self.agregar_btn)

        self.mostrar_btn = QPushButton('Mostrar Objetos', self)
        self.mostrar_btn.clicked.connect(self.mostrar_objetos)
        layout.addWidget(self.mostrar_btn)

        self.actualizar_btn = QPushButton('Actualizar Objeto', self)
        self.actualizar_btn.clicked.connect(self.actualizar_objeto)
        layout.addWidget(self.actualizar_btn)

        self.eliminar_btn = QPushButton('Eliminar Objeto', self)
        self.eliminar_btn.clicked.connect(self.eliminar_objeto)
        layout.addWidget(self.eliminar_btn)

        self.setLayout(layout)

    def agregar_objeto(self):
        id = self.id_input.text()
        nombre = self.nombre_input.text()
        precio = int(self.precio_input.text())
        tipo = self.tipo_input.text()
        penetracion = int(self.penetracion_input.text())
        dano_magico = int(self.dano_magico_input.text())
        dano_critico = int(self.dano_critico_input.text())
        self.controlador.agregar_objeto(id, nombre, precio, tipo, penetracion, dano_magico, dano_critico)
        QMessageBox.information(self, 'Información', f'Objeto {nombre} agregado exitosamente.')

    def mostrar_objetos(self):
        objetos = self.controlador.mostrar_objetos()
        if not objetos:
            QMessageBox.information(self, 'Información', 'No hay objetos para mostrar.')
        else:
            info = '\n'.join([f'ID: {item.id}, Nombre: {item.nombre}, Precio: {item.precio}, Tipo: {item.tipo}, '
                              f'Penetración: {item.penetracion}, Daño Mágico: {item.dano_magico}, Daño Crítico: {item.dano_critico}'
                              for item in objetos])
            QMessageBox.information(self, 'Objetos', info)

    def actualizar_objeto(self):
        id = self.id_input.text()
        nuevo_precio = int(self.precio_input.text())
        nueva_penetracion = int(self.penetracion_input.text())
        nuevo_dano_magico = int(self.dano_magico_input.text())
        nuevo_dano_critico = int(self.dano_critico_input.text())
        self.controlador.actualizar_objeto(id, nuevo_precio, nueva_penetracion, nuevo_dano_magico, nuevo_dano_critico)
        QMessageBox.information(self, 'Información', f'Objeto {id} actualizado exitosamente.')

    def eliminar_objeto(self):
        id = self.id_input.text()
        self.controlador.eliminar_objeto(id)
        QMessageBox.information(self, 'Información', f'Objeto {id} eliminado exitosamente.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CRUDApp()
    ex.show()
    sys.exit(app.exec_())