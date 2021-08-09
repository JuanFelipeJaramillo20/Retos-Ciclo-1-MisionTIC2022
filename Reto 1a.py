def calcula_metros(empresa: str, num_talla_S: int, num_talla_M: int, num_talla_L: int) -> str:
    metros = (num_talla_S*2) + (num_talla_M*2.5) + (num_talla_L*3)
    return f"Para fabricar {num_talla_S} trajes talla S, {num_talla_M} trajes talla M, {num_talla_L} trajes talla L, para la empresa {empresa} se necesitan {metros} metros de tela"

print(calcula_metros("Empresa1",2,3,4))
print(calcula_metros("Empresa2",25,3,4))
print(calcula_metros("Empresa3",2,67,4))
print(calcula_metros("Empresa4",2,3,34))
print(calcula_metros("Empresa5",10,20,32))