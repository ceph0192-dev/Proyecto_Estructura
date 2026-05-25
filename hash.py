_PRIMO = 31
_MODULO = 100000000

def generar_hash(matricula):
    acumulador = 7
    for caracter in matricula:
        acumulador = (acumulador * _PRIMO + ord(caracter)) % _MODULO
    return abs(acumulador) + 1 #para evitar el cero