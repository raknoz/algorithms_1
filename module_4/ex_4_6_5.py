'''
Consignas:
    Escribir funciones que resuelvan los siguientes problemas:
    a) Dado un año indicar si es bisiesto.
    Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.
    b) Dado un mes y un año, devolver la cantidad de días correspondientes.
    c) Dada una fecha (día, mes, año), indicar si es válida o no.
    d) Dada una fecha, indicar los días que faltan hasta fin de mes.
    e) Dada una fecha, indicar los días que faltan hasta fin de año.
    f) Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.
    g) Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido entre ambas, en años, meses y días.
    Nota: en todos los casos, invocar las funciones escritas previamente cuando sea posible.
'''
DIC_MESES_DIAS = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def es_bisiesto(y):
    if(y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        return True
    else:
        return False

def valida_bisiesto(y):
    if es_bisiesto(y):
        print('El año {} es biciesto'.format(y))
    else:
        print('El año {} no es biciesto'.format(y))


def contador_dias(m, y):

    if m < 1 or m > 12:
        print('El valor del mes tiene que estar entre 1 y 12')
        return
    
    if y < 1:
        print('El valor del año tiene que ser mayor a 1')
        return

    bisiesto = es_bisiesto(y)
    total_dias = 0
    
    for x in range(1, m + 1):
        total_dias+= DIC_MESES_DIAS.get(x)

    if bisiesto and m > 1:
        total_dias+=1

    return total_dias

def evalua_fecha(d, m, y):
    if  (d < 1 or d > 31) or (m < 1 or m > 12) or (y < 1):
        return False
    elif(m == 2 and not es_bisiesto(y) and d > 28):
        return False
    elif(m != 2 and d != DIC_MESES_DIAS.get(m)):
        return False
    return True

def valida_fecha(d, m, y):
    if  not evalua_fecha(d, m, y):
        return print('Fecha invalida!')
    print('Fecha válida')    
        
def fin_de_mes(d, m, y):
    dias_total = DIC_MESES_DIAS.get(m)
    if (m == 2 and es_bisiesto(y)):
        dias_total +=1
    return dias_total - d

def fin_de_anio(d, m, y):
    total_dias_anio = sum(DIC_MESES_DIAS.values())
    total_dias_mes = contador_dias(m, y)
    total_contador = total_dias_anio - total_dias_mes + fin_de_mes(d, m, y)
    if(es_bisiesto(y)):
        total_contador+= 1
    return total_contador

def dias_transcurridos(d, m, y):
    return (contador_dias(m, y) - DIC_MESES_DIAS.get(m - 1) + d)

def dias_transcurridos_hasta_fecha(d, m, y):
    if not evalua_fecha(d, m, y):
        return print('Fecha inválida')
    print('Transcurrieron {} días'.format((contador_dias(m, y) - DIC_MESES_DIAS.get(m - 1) + d)))




# valida_bisiesto(1997)
# valida_bisiesto(2012)
# print(contador_dias(12, 2012))
# valida_fecha(29,2,2012) 
# valida_fecha(28,2,2012) 
# valida_fecha(29,2,2011) 
# valida_fecha(31,3,2011)
# print('Faltan {} días para fin de mes'.format(fin_de_mes(1, 2, 2013))) 
# print('Faltan {} días para fin de mes'.format(fin_de_mes(1, 2, 2012))) 
# print('Faltan {} días para fin de mes'.format(fin_de_mes(5, 10, 2013)))
#print('Para fin de año faltan {} días'.format(fin_de_anio(1, 1, 2011)))
#print('Para fin de año faltan {} días'.format(fin_de_anio(1, 1, 2011)))
#dias_transcurridos_hasta_fecha(29, 2, 2011)