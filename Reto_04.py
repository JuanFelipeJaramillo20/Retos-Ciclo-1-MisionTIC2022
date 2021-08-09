from functools import reduce

def transformar_lista(elemento) -> list:
    salida = []
    aux = []
    for elementox in elemento[1:]:
        aux.append(elementox[1])
    temp = [elemento[0], reduce(lambda acumulador = 0, elemento = 0: acumulador + elemento, aux)]
    salida= temp
    return salida

def informe(examenes_medicos: list) -> list:
    salida = list(map(transformar_lista, examenes_medicos))
    contador = 0
    for lista in examenes_medicos:
        for elemento in lista[1:]:
            if elemento[0] == "EL_PCOVID":
                contador += 1
    salida.append(contador)
    return salida