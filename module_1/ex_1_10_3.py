'''
Consigna:
    Escribir un programa que pregunte al usuario:
        a) su nombre, y luego lo salude.
        b) dos números, y luego muestre el producto.

Pre-requisitos:
    - Se deben ingresar solo números enteros postivos.
'''
def imprimir_datos():

    name = n1 = input("Ingrese su nombre: ")
    print(f'Hola {name}')

    n1 = int(input("Ingrese un número entero: "))
    n2 = int(input("Ingrese otro número entero: "))
    print(f'el producto de {n1} y {n2} es  { n1 * n2}') 

imprimir_datos()