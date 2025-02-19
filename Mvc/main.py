from Controlador.controlador import Controlador

def menu():
    controlador_instance = Controlador()

    while True:
        print("\nOpciones:")
        print("1. Agregar un objeto")
        print("2. Mostrar todos los objetos")
        print("3. Actualizar un objeto")
        print("4. Eliminar un objeto")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id = input("Ingresa el ID: ")
            nombre = input("Ingresa el nombre del objeto: ")
            precio = int(input("Ingresa el precio del objeto: "))
            tipo = input("Ingresa el tipo de objeto: ")
            penetracion = int(input("Ingresa la penetración: "))
            dano_magico = int(input("Ingresa el daño mágico: "))
            dano_critico = int(input("Ingresa el daño crítico: "))
            controlador_instance.agregar_objeto(id, nombre, precio, tipo, penetracion, dano_magico, dano_critico)

        elif opcion == '2':
            controlador_instance.mostrar_objetos()

        elif opcion == '3':
            id = input("Ingresa el ID del objeto a actualizar: ")
            nuevo_precio = int(input("Ingresa el nuevo precio: "))
            nueva_penetracion = int(input("Ingresa la nueva penetración: "))
            nuevo_dano_magico = int(input("Ingresa el nuevo daño mágico: "))
            nuevo_dano_critico = int(input("Ingresa el nuevo daño crítico: "))  
            controlador_instance.actualizar_objeto(id, nuevo_precio, nueva_penetracion, nuevo_dano_magico, nuevo_dano_critico)

        elif opcion == '4':
            id = input("Ingresa el ID del objeto a eliminar: ")
            controlador_instance.eliminar_objeto(id)

        elif opcion == '5':
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Intenta nuevamente.")

if __name__ == '__main__':
    menu()
