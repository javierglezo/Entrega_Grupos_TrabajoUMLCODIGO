# Definición de la clase A
class A:
    def __init__(self, a):
        # Inicialización del atributo 'a'
        self.a = a

# Definición de la clase B que hereda de A
class B(A):
    def __init__(self, a, b):
        # Llamada al constructor de la clase base A
        super().__init__(a)
        # Inicialización del atributo 'b'
        self.b = b

# Definición de la clase C que hereda de A
class C(A):
    def __init__(self, a, c):
        # Llamada al constructor de la clase base A
        super().__init__(a)
        # Inicialización del atributo 'c'
        self.c = c

# Definición de la clase D que hereda de B y C
class D(B, C):
    def __init__(self, a, b, c):
        # Inicialización de los atributos 'a', 'b' y 'c'
        self.a = a
        self.b = b
        self.c = c

# Función principal
def main():
    # Solicitar al usuario que ingrese valores para los puntos a, b y c
    punto_a = int(input("Ingrese el punto a: "))
    punto_b = int(input("Ingrese el punto b: "))
    punto_c = int(input("Ingrese el punto c: "))

    # Crear una instancia de la clase D con los valores proporcionados
    punto = D(punto_a, punto_b, punto_c)

    # Imprimir si la instancia es una instancia de las clases A, B, C y D
    print(f"Vamos a comprobar si el punto ({punto.a},{punto.b},{punto.c}) es una instancia de:\n" +
          f"Clase A: {isinstance(punto, A)}\n" +
          f"Clase B: {isinstance(punto, B)}\n" +
          f"Clase C: {isinstance(punto, C)}\n" +
          f"Clase D: {isinstance(punto, D)}\n" 
          )

if __name__ == "__main__":
    main()
