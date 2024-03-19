# Definición de la clase Punto2D
class Punto2D:
    def __init__(self, x, y):
        self.x = x  # Inicialización del atributo x
        self.y = y  # Inicialización del atributo y

    def traslacion(self, a, b):
        # Método para realizar una traslación del punto en el plano 2D
        self.x += a  # Incremento del atributo x
        self.y += b  # Incremento del atributo y

    def __str__(self):
        # Método especial para representar el punto como una cadena
        return ">>> X: {}; Y: {}".format(self.x, self.y)

# Definición de la clase Punto3D que hereda de Punto2D
class Punto3D(Punto2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)  # Llamada al constructor de la clase base
        self.z = z  # Inicialización del atributo z

    def traslacion(self, a, b, c):
        # Método para realizar una traslación del punto en el espacio 3D
        super().traslacion(a, b)  # Llamada al método de traslación de la clase base
        self.z += c  # Incremento del atributo z

    def __str__(self):
        # Método especial para representar el punto como una cadena, incluyendo la coordenada z
        return super().__str__() + "; Z: {}".format(self.z)

# Función para obtener un valor entero a partir de la entrada del usuario
def obtener_valor_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))  # Lectura de la entrada y conversión a entero
            return valor  # Retorno del valor obtenido
        except ValueError:
            print("Error: Meta un valor entero.")  # Manejo de excepción en caso de entrada inválida

# Función principal del programa
def main():
    print("Bienvenido al programa Punto3D")

    # Selección entre punto 2D y punto 3D
    opcion = input("\nSelecciona:\n1. Punto 2D\n2. Punto 3D\nOpcion: ")

    if opcion == "1":
        # Creación de un punto 2D
        x = obtener_valor_entero("Ingrese el valor de X: ")
        y = obtener_valor_entero("Ingrese el valor de Y: ")
        punto = Punto2D(x, y)
        print("Punto creado:", punto)

        # Menú para realizar traslaciones en el plano 2D
        while True:
            opcion = input("\nSeleccionar una opcion:\n1. Traslacion\n2. Salir\nRespuesta: ")
            if opcion == "1":
                a = obtener_valor_entero("Ingrese la traslación de X: ")
                b = obtener_valor_entero("Ingrese la traslación de Y: ")
                punto.traslacion(a, b)
                print("Punto trasladado:", punto)
            elif opcion == "2":
                print("Gracias")
                break
            else:
                print("Opcion inválida.")

    elif opcion == "2":
        # Creación de un punto 3D
        x = obtener_valor_entero("Ingrese el valor de X: ")
        y = obtener_valor_entero("Ingrese el valor de Y: ")
        z = obtener_valor_entero("Ingrese el valor de Z: ")
        punto = Punto3D(x, y, z)
        print("Punto creado:", punto)

        # Menú para realizar traslaciones en el espacio 3D
        while True:
            opcion = input("\nSeleccionar opcion:\n1. Traslacion\n2. Salir\nRespuesta: ")
            if opcion == "1":
                a = obtener_valor_entero("Ingrese la traslación de X: ")
                b = obtener_valor_entero("Ingrese la traslación de Y: ")
                c = obtener_valor_entero("Ingrese la traslación de Z: ")
                punto.traslacion(a, b, c)
                print("Punto trasladado:", punto)
            elif opcion == "2":
                print("Gracias")
                break
            else:
                print("Opción inválida.")

    else:
        print("Opción inválida.")

# Llamada a la función principal si este script es ejecutado directamente
if __name__ == "__main__":
    main()
