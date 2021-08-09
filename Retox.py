def reportarNivel(dicSalida):
    return f"Estado del nivel del líquido del tanque {dicSalida['codigoTanque']}: {dicSalida['nivel']}"
def estado_nivel(datos_tanque):
        
    if  (datos_tanque["sensor1"]==True and datos_tanque["sensor2"]==True and datos_tanque["sensor3"]==False):
            nivel = "nivel medio"
            Salida = {  "codigoTanque":datos_tanque["codigo"],  
                    "nivel":nivel
                    }
    else:

        if (datos_tanque["sensor1"]==False and datos_tanque["sensor2"]==False and datos_tanque["sensor3"]==False):
            nivel = "Vacío"
            Salida = {  "codigoTanque":datos_tanque["codigo"],  
                    "nivel":nivel
                    }
        else:
            if  (datos_tanque["sensor1"]==True and datos_tanque["sensor2"]==False and datos_tanque["sensor3"]==False):
                nivel = "nivel bajo"
                Salida = {  "codigoTanque":datos_tanque["codigo"],  
                    "nivel":nivel
                    }
            else:
                if  (datos_tanque["sensor1"]==True and datos_tanque["sensor2"]==True and datos_tanque["sensor3"]==True):
                    nivel = "nivel alto"
                    Salida = {  "codigoTanque":datos_tanque["codigo"],  
                    "nivel":nivel
                    }

    return Salida
    
datos_tanque = {'codigo':'TA001', 'sensor1': bool(True), 'sensor2':bool(True), 'sensor3':bool(False)}

print(reportarNivel(estado_nivel(datos_tanque)))
#print(estado_nivel(datos_tanque))