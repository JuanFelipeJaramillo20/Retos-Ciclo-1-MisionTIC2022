"""
def notas(informacion:dict)-> dict:
    return informacion['id_nombre'] + str(informacion['id_codigo']) + str(informacion['id_calificacion']) + str(informacion['id_NMin']) + str(informacion['id_NMax']) 
    """
def promedio (info):
    m_i = (min(info['M1'],info['M2'],info['M3'],info['M4']))
    m_x = (max(info['M1'],info['M2'],info['M3'],info['M4']))
    #promedio = (info['M1']+info['M2']+info['M3']+info['M4'])/4
    n = 0
    n += info ['M1']
    n += info ['M2']
    n += info ['M3']
    n += info ['M4']
    promedio = (n/4)
    if promedio > 3.0 and promedio <= 3.5:
        id_calificacion ='Promedio básico'
    elif promedio > 3.5 and promedio <= 4.0:
        id_calificacion = 'Promedio intermedio'
    elif promedio > 4.0 and promedio <= 4.5:
        id_calificacion = 'Promedio superior'
    elif promedio > 4.5 and promedio == 5.0:
        id_calificacion = 'Promedio sobresaliente'
    else:
        id_calificacion = 'Los datos no estan dentro de los parametros de las asignaturas'
    p = {
        'id_calificacion': id_calificacion,
        'id_nombre': info ['id_nombre'],
        'id_codigo': info ['id_codigo'],
        'id_NMin': m_i,
        'id_NMax': m_x
    }
    return "Las calificaciones del estudiante: " + p["id_nombre"] + ". Identificado con el código: " + str(p["id_codigo"]) + ". Son: \n Promedio: " + p["id_calificacion"] + ".\n Nota máxima: " + str(p["id_NMax"]) + ".\n Nota mínima: " + str(p["id_NMin"])
info = {
    'id_nombre': 'Camilo',
    'id_codigo': 112971,
    'M1': 1,
    'M2': 2.5,
    'M3': 2,
    'M4': 2,
}
print(promedio(info))