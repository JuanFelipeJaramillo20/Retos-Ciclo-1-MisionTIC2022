def pago_mensual(datos_empleado: dict) -> str:
    comision = 0
    if datos_empleado["ventas"] <= 1000000:
        comision = datos_empleado["ventas"]* 0.03
    elif datos_empleado["ventas"] > 1000000 and datos_empleado["ventas"] <= 3000000:
        comision = datos_empleado["ventas"] * 0.05
    elif datos_empleado["ventas"] > 3000000 and datos_empleado["ventas"] <= 5000000:
        comision = datos_empleado["ventas"] * 0.08
    elif datos_empleado["ventas"] > 5000000:
        comision = datos_empleado["ventas"] * 0.12
    else:
        pass

    if datos_empleado["ventas"] >= 10000000:
        felicitacion = "Si"
    else:
        felicitacion = "No"
    dic_salida = dict(nombreCompleto = datos_empleado["nombre"] + " " + datos_empleado["apellido"], identificacion = str(datos_empleado["id"]), pagoTotal = str( int(datos_empleado["salario_neto"] + comision)), felicitacion =felicitacion )
 
    salida = "El pago mensual de " + dic_salida["nombreCompleto"] + " identificado con " + dic_salida["identificacion"] + " es: " + dic_salida["pagoTotal"] + ". Felicitaciones por ventas: " + dic_salida["felicitacion"]
    return salida