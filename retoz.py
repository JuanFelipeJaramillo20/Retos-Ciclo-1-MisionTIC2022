def pago_mensual(datos_empleado:dict)->dict:
    if (datos_empleado["ventas"] <= 1000000):
        comision = 3
    elif (datos_empleado["ventas"] <= 3000000):
        comision = 5
    elif datos_empleado["ventas"] <= 5000000:
        comision = 8
    else:
        comision = 12
        pago=int(comision)*(datos_empleado["ventas"])/100
        dicSalida = {
            "nombreCompleto":(datos_empleado["nombre"]) + " " + (datos_empleado["apellido"]),
            "identificacion":(datos_empleado["id"]),
            "pagoTotal":pago,
            "felicitacion": "sino"
        }
        if (datos_empleado["ventas"] > 10000000):
            dicSalida["felicitacion"]= "Si"
        else:
            dicSalida["felicitacion"] = "No"
        return f"El pagp mensual de {dicSalida['nombreCompleto']} identificado con {dicSalida['identificacion']}"
datos_empleado = {
    "nombre":"Juan",
    "apellido":"Castro",
    "id":32778569,
    "salario_neto":945000,
    "ventas":2130000
}
print(pago_mensual(datos_empleado))