# 1. importar librerias
import os
import re
import math

# 2. declaro constantes
POTENCIA = 2

# 3. funciones y/o clases

def validar_numero(num):
    try:
        return float(num)
    except:
        print('Dato ingresa no es número')
        num = input('Ingrese el número: ')
        return validar_numero(num)

class Operaciones:
    def __init__(self, num1, num2):
        # atributos de clase
        self.num1 = num1
        self.num2 = num2
    
    # creacion metodos de clase
    def sumar(self):
        return self.num1 + self.num2
    
    def restar(self):
        return self.num1 - self.num2
    
    def potencia(self, n):
        return math.pow(self.num1,n)

# 4. programa principal
if __name__ == "__main__":
    # Solicito el ingreso de 2 números
    n1 = validar_numero(input('Ingrese el primero número: '))
    n2 = validar_numero(input('Ingrese un segundo número: '))

    # Creo el objeto de la clase
    opp = Operaciones(n1, n2)

    # Imprimo resultados
    s = opp.sumar()
    r = opp.restar()
    p = opp.potencia(POTENCIA)

    print(f'La suma de los valores es: {s}')
    print(f'La resta de los valores es: {r}')
    print(f'La potencia de {opp.num1} elevedo a la 2 es : {p}')

