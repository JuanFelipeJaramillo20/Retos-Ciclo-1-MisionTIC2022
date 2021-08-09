import pandas as pd

def ventas(ruta_archivo: str, codigo: int) -> dict:
    df = pd.read_csv(ruta_archivo, sep=",", names=["id_cliente","Nombre","codigo_producto","Cantidad"])
    salida = dict()
    salida[codigo] = 0
    contador = 0
    entrada = df.values.tolist()
    for venta in entrada:
        if venta[2] == codigo:
            salida[codigo] += venta[3]
            contador += venta[3]
    return salida
