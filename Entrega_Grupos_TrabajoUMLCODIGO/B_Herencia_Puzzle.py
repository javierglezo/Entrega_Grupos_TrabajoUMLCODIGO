# Definición de la clase Base
class Base:
    def __init__(self, a, b, c):
        # Inicialización de los atributos 'a', 'b' y 'c' con los valores proporcionados
        self.a = a
        self.b = b
        self.c = c

    # Método para imprimir el valor del atributo 'a'
    def A(self):
        print(self.a)

    # Método para imprimir el valor del atributo 'b'
    def B(self):
        print(self.b)

    # Método para imprimir el valor del atributo 'c'
    def C(self):
        print(self.c)

# Definición de la clase Derivada que hereda de Base
class Derivada(Base):
    def __init__(self):
        # Inicialización del atributo 'a' con un valor específico
        self.a = "aa"
        # Llamada al constructor de la clase base con valores predeterminados para 'a', 'b' y 'c'
        super().__init__("a", "b", "c")
        # Asignación de un valor específico al atributo 'c'
        self.c = "cc"

    # Método B que sobrescribe el método B de la clase base
    def B(self):
        # Asignación de un nuevo valor al atributo 'b'
        self.b = "bb"
        # Llamada al método B de la clase base
        super().B()
        # Imprimir el nuevo valor del atributo 'b'

# Crear instancias de Base y Derivada
base = Base("a", "b", "c")
derivada = Derivada()

# Imprimir los valores de 'a' de ambas instancias
print("Valor de 'a' en base:", end=" ")
base.A()
print("Valor de 'a' en derivada:", end=" ")
derivada.A()
print()

# Imprimir los valores de 'b' de ambas instancias antes y después de llamar al método B()
print("Valor de 'b' en base antes de llamar a B():", end=" ")
base.B()
print("Valor de 'b' en derivada antes de llamar a B():", end=" ")
derivada.B()
print("Valor de 'b' en base después de llamar a B():", end=" ")
base.B()
print("Valor de 'b' en derivada después de llamar a B():", end=" ")
derivada.B()
print()

# Imprimir los valores de 'c' de ambas instancias
print("Valor de 'c' en base:", end=" ")
base.C()
print("Valor de 'c' en derivada:", end=" ")
derivada.C()

# Asignar la instancia de base a derivada
derivada = base

# Imprimir el valor de 'c' de derivada después de la asignación
print("Valor de 'c' en derivada después de la asignación:", end=" ")
derivada.C()
