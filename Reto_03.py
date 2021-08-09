import datetime
aptos = [{'año': 2002, 'm2': 100, 'asc': True, 'gar': True, 'hab': 3, 'zona': 3},
{'año': 1985, 'm2': 80, 'asc': True, 'gar': True, 'hab': 3, 'zona': 4},
{'año': 2006, 'm2': 90, 'asc': False, 'gar': True, 'hab': 3, 'zona': 5},
{'año': 2012, 'm2': 180, 'asc': True, 'gar': True, 'hab': 4, 'zona': 2},
{'año': 1999, 'm2': 70, 'asc': False, 'gar': True, 'hab': 3, 'zona': 1},
{'año': 2003, 'm2': 220, 'asc': True, 'gar': True, 'hab': 5, 'zona': 6}]

def calcular_Precio (apto: dict):
    precioxmetro = 0
    aumentoGaraje = 0
    aumentoAscensor = 0
    aumentoHabitaciones = 0
    descuentoAntiguedad = 0
    if apto["zona"] == 1:
        precioxmetro = apto["m2"] * 800000
    elif apto["zona"] == 2:
        precioxmetro = apto["m2"] * 1200000
    elif apto["zona"] == 3:
        precioxmetro = apto["m2"] * 2200000
    elif apto["zona"] == 4:
        precioxmetro = apto["m2"] * 3400000
    elif apto["zona"] == 5:
        precioxmetro = apto["m2"] * 5200000
    elif apto["zona"] == 6:
        precioxmetro = apto["m2"] * 6400000
    if apto["asc"] == True:
        aumentoAscensor += 1500000
    if apto["gar"] == True:
        aumentoGaraje += 5000000
    aumentoHabitaciones = apto["hab"] * 1000000
    precioTotal = precioxmetro + aumentoAscensor + aumentoGaraje + aumentoHabitaciones
    descuentoAntiguedad = (datetime.datetime.now().year - apto["año"]) /100
    precioFinal = precioTotal - (precioTotal * descuentoAntiguedad)
    return int(precioFinal)

def buscar(inmu: list, presupuesto: int) -> list:
    salida = []
    for i in inmu:
        precio = calcular_Precio(i)
        if precio <= presupuesto:
            temp = {
                "año" : i["año"],
                "m2" : i["m2"],
                "asc" : i["asc"],
                "gar" : i["gar"],
                "hab" : i["hab"],
                "zona" : i["zona"],
                "pre" : precio
            }
            salida.append(temp)
    return salida

apto= [{'año': 2002, 'm2': 100, 'asc': True,
 'gar': True, 'hab': 3, 'zona': 3, 'pre': 185895000},
  {'año': 1985, 'm2': 80, 'asc': True, 'gar': True, 'hab': 3, 'zona': 4, 'pre': 180160000},
   {'año': 1985, 'm2': 80, 'asc': True, 'gar': True, 'hab': 3, 'zona': 4, 'pre': 180160000},
    {'año': 2012, 'm2': 180, 'asc': True, 'gar': True, 'hab': 4, 'zona': 2, 'pre': 206115000},
     {'año': 1999, 'm2': 70, 'asc': False, 'gar': True, 'hab': 3, 'zona': 1, 'pre': 49920000},
      {'año': 1999, 'm2': 70, 'asc': False, 'gar': True, 'hab': 3, 'zona': 1, 'pre': 49920000}]

print(buscar(aptos, 350000000))