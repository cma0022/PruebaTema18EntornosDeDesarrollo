import math

# Creamos la clase
class circulo:

    # Definimos las variables
    _radio:float

    # Constructor
    def __init__(self, radio:float) -> None:
        self._radio = radio


    # Método que calcula el área
    def area(self):
        resultado = math.pi*math.pow(self._radio,2)
        return resultado
        
    

    # Método que calcular la circunferencia
    def circunferencia(self):
        resultado = math.pi*2*self._radio
        return resultado
