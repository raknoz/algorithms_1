'''
Consigna:
    Escribir un programa que le pregunte al usuario una cantidad de pesos, una tasa de interés y un número de años y muestre como resultado el monto final a obtener. La fórmula
    a utilizar es: C * ((1 + (X/100)) ** N)
'''

def calculo_interes(capital, tasa, tiempo):
    '''
        Función que recibe el capital, la tasa y el tiempo e imprime el cálculo del dinero total a pagar.
    '''
    print('El monto final a obtener es: {}'.format(capital * ((1 + (tasa/100)) ** tiempo)))

def main():
    '''
        Función principal que pide lo datos al usuario para procesarlos.
    '''
    capital = float(input('Ingrese el monto del capital: '))
    tasa = float(input('Ingrese el monto del tasa de interes: '))
    tiempo = float(input('Ingrese el tiempo a calcular: '))
    calculo_interes(capital, tasa, tiempo)

main()