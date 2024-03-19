# Definición de la clase Pared
class Pared:
    def __init__(self, orientacion):
        # Inicialización de la orientación de la pared
        self.orientacion = orientacion
        # Lista para almacenar las ventanas asociadas a la pared
        self.ventanas = []

# Definición de la clase ParedCortina que hereda de Pared
class ParedCortina(Pared):
    def __init__(self, orientacion, superficie_acristalada):
        # Llamada al constructor de la clase base Pared
        super().__init__(orientacion)
        # Atributo específico de ParedCortina: superficie acristalada
        self.superficie_acristalada = superficie_acristalada

# Definición de la clase Ventana
class Ventana:
    def __init__(self, pared, superficie, proteccion = None):
        # Asignación de la pared a la ventana
        self.pared = pared
        # Superficie de la ventana
        self.superficie = superficie
        # Protección de la ventana (por defecto, None)
        if proteccion is None:
            raise Exception("Protección obligatoria")
        self.proteccion = proteccion
        # Asociar la ventana con la pared
        pared.ventanas.append(self)

# Definición de la clase Casa
class Casa:
    def __init__(self, paredes):
        # Lista de paredes que componen la casa
        self.paredes = paredes

    # Método para calcular la superficie total acristalada de la casa
    def superficie_acristalada(self):
        total_acristalada = 0
        for pared in self.paredes:
            if isinstance(pared, ParedCortina):
                total_acristalada += pared.superficie_acristalada
            for ventana in pared.ventanas:
                total_acristalada += ventana.superficie
        return total_acristalada

# Función para comprobar si una ventana ha sido definida
def comprobar_ventana(ventana):
    try:
        ventana
    except Exception as e:
        print(e)

# Función para definir la superficie de una ventana
def definir_superficie(ventana):
    superficie = int(input(f"Dime la superficie de la ventana {ventana}: "))
    while superficie <= 0:
        print("\nEse número no sirve, introduzca otro. \n")
        superficie = int(input(f"Dime la superficie de la ventana {ventana}: "))
    return superficie

# Función principal
def main():
    # Instanciación de las paredes
    pared_norte = Pared("NORTE")
    pared_oeste = Pared("OESTE")
    pared_sur = Pared("SUR")
    pared_este = Pared("ESTE")

    # Instanciación de las ventanas y sus comprobaciones
    ventana_norte = Ventana(pared_norte, definir_superficie("norte"), "Estor")
    ventana_oeste = Ventana(pared_oeste, definir_superficie("oeste"), "Estor")
    ventana_sur = Ventana(pared_sur, definir_superficie("sur"), "Persiana")
    ventana_este = Ventana(pared_este, definir_superficie("este"), "Persiana")

    comprobar_ventana(ventana_norte)
    comprobar_ventana(ventana_oeste)
    comprobar_ventana(ventana_sur)
    comprobar_ventana(ventana_este)
    print()
    # Imprimir información sobre las ventanas
    print(f">>> La ventana en la pared norte tiene una superficie de {ventana_norte.superficie} y su protección es: {ventana_norte.proteccion}\n"
          f">>> La ventana en la pared oeste tiene una superficie de {ventana_oeste.superficie} y su protección es: {ventana_oeste.proteccion}\n"
          f">>> La ventana en la pared sur tiene una superficie de {ventana_sur.superficie} y su protección es: {ventana_sur.proteccion}\n"
          f">>> La ventana en la pared este tiene una superficie de {ventana_este.superficie} y su protección es: {ventana_este.proteccion}\n"
          )
    
    # Instanciación de la casa con las 4 paredes
    casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])
    # Imprimir la superficie total acristalada de la casa
    print(f"La superficie total de la casa es de: {casa.superficie_acristalada()} metros cuadrados")


if __name__ == "__main__":
    main()
