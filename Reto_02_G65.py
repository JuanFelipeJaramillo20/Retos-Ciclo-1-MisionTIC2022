def estado_nivel(datos_tanque: dict) -> str:
    if datos_tanque["sensor3"]==False:
        if datos_tanque["sensor2"]== False:
            if datos_tanque["sensor1"]== False:
                respuesta="nivel vacío"
            elif datos_tanque["sensor1"]==True:
                respuesta= "nivel bajo"
        elif datos_tanque["sensor2"]==True:
            respuesta="nivel medio"
    elif (datos_tanque["sensor2"]==True and datos_tanque["sensor3"]==True) and datos_tanque["sensor1"]==True:
        respuesta= "nivel alto"
    else:
        respuesta="revisar sensores"
    dic_salida = dict( codigoTanque = datos_tanque["codigo"], nivel = respuesta)
    return "Estado del nivel del líquido del tanque " + dic_salida["codigoTanque"] + ": " + dic_salida["nivel"]

print(estado_nivel(dict(codigo = "TA001", sensor1 = False,sensor2 = False, sensor3 = False)))