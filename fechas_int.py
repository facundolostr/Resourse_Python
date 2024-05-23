
"""
aaaamm|-> dd
"""
def el_dia(aaaammdd):
    return aaaammdd%100

"""
aaaa <-|mmdd
"""
def el_anio(aaaammdd):
    return aaaammdd//10000

"""
aaaamm <- |dd
aaaa| -> mm
"""
def el_mes(aaaammdd):
    return (aaaammdd//100)%100


def str_fecha(aaaammdd):
    dia = el_dia(aaaammdd)
    mes = el_mes(aaaammdd)
    anio = el_anio(aaaammdd)
    return f"{dia:02}/{mes:02}/{anio:04}"

def es_bisiesto(anio):
    return anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0

def obtener_cantidad_dias_mes(mes,anio):
    dias = (0,31,28,31,30,31,30,31,31,30,31,30,31)
    #index  0  1  2  3  4  5  6  7  8  9 10 11 12

    if mes == 2 and es_bisiesto(anio):
        return 29
    
    return dias[mes]    

def es_fecha_valida(aaaammdd):
    
    anio = el_anio(aaaammdd)
    if anio < 1 or anio > 2500:
        return False
    
    mes = el_mes(aaaammdd)
    if mes < 1 or mes > 12:
        return False

    dia = el_dia(aaaammdd)
    if dia < 1 or dia > obtener_cantidad_dias_mes(mes,anio):
        return False
    
    return True

def test():
    fecha = 19630101
    for fecha in range(20010101,20011232):
        if es_fecha_valida(fecha):
            print(str_fecha(fecha))



if __name__ == '__main__':
    print(__name__)
    test()






