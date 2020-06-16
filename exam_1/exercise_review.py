import pprint

'''
    1) Escribir una funcion que sacuda una matriz. Es decir, que las filas pares, las rote un elemento hacia la derecha, y las filas impares, hacia la izquierda. 
    Esta función debe ser in-place, debe trabajar sobre la matriz recibida. La matriz esta representada como una lista de listas.
    Ejemplo:
    1 2 3 11    11 1 2 3
    4 5 6 12 -> 5 6 12 4
    7 8 9 13    13 7 8 9
'''

def sacudir(matriz):
    ''' Función que recibe una matriz y mueve una posición los elementos.'''
    for indice, fila in enumerate(matriz):
        if indice%2 == 0:
        #Inserto en la primera posición el elemento que saco del final
            fila.insert(0, fila.pop())
        else:
        #Inserto en la última posición el elemento de la posición inicial
            fila.append(fila.pop(0))
    return matriz
    

'''
    2) Escribir una función que dada una práctica y una lista de alumnos y sus ayudantes asignados, devuelva todos los nombres de los alumnos asignados a la práctica recibido. 
    Ejemplo
    Dada la práctica "Grace" y los alumnos: [(103456, "Juan", "Pérez", "Grace"), (103333, "Marta", "López", "Bárbara"), (103692, "Diana", "Rodríguez", "Grace"), (99264, "Pepito", "Martínez", "Alan")]
    Debe devolver: ["Juan Pérez", "Diana Rodríguez"]
'''

def filtra_alumnos(lista_alumnos, filtro_practica):
    '''Función que recibe una lista de alumnos l y una práctica pf y retorna los alumnos para esa práctica.'''
    resultado = []
    for codigo, nombre, apellido, practica in lista_alumnos:
        if practica == filtro_practica:
            resultado.append(f'{nombre} {apellido}')
    return resultado

'''
    3) Escribir una función que realice lo siguiente:
    - Le pida al usuario que ingrese una contraseña. Luego debe validar que la misma:
        - Tenga al menos dos numeros, pero no tenga más números que letras (a-z, A-Z, no es necesario incluir letras acentuadas o especiales de otros idiomas que no sea el ingles).
        - Tenga alguno de estos caracteres ("!", "@", "~", "/", "#") pero no más de tres.
    - Si no ingresa una contraseña válida debe volver a preguntarle hasta quedarse sin intentos.
    - Cuando adivine, se deben devolver la cantidad de intentos restante. 
    Si se acaban los intentos, debe mostrar un mensaje por pantalla y devolver -1.
'''

def valida_psw(psw):
    ''' Función que recive una password y valida que cumpla con ciertos requisitos, en caso de fallar devuelve -1.'''
    l_especiales = '!@~/#'
    num = 0
    let = 0
    esp = 0

    for c in psw:
        if c in l_especiales:
            esp +=1
        elif c.isdigit():
            num +=1
        elif c.isalpha():
            let +=1
        
    if num < 2 or num > let or esp == 0 or esp > 3:
        return False
    
    return True

def main(limite_intentos):
    ''' Función que recibe un limite de intentos y pide al usuario una password hasta que se agoten los mismos.'''
    intentos = 1

    while intentos <= limite_intentos:
        psw = input('Ingrese un password: ')
        if valida_psw(psw):
            break
        intentos +=1
        
    if intentos <= limite_intentos:
        print(f'Ingresó la password correctamente, le quedaron {limite_intentos - intentos} intentos.')
        return 0
    
    print('Agotó todas las posibilidades de ingresar la password.')
    return -1