"""
Este módulo contiene funciones para utilizar en programas varios de Python.
"""

def validar_numero_positivo(numero):
    
    invalido = False

    while not invalido:

        for caracter in numero:

            if caracter not in '0123456789.' or numero[0] not in '123456789' or numero[-1] not in '0123456789':

                numero = input("Ingrese un valor numérico positivo: ")
                break
    
        invalido = True
        
    return float(numero)

def prueba():
    print("\nUd. está ejecutando un módulo de funciones.\n")

if __name__ == "__main__":
    prueba()