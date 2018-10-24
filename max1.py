def compte_pos(nombres):
    nombre_positif = 0
    for nombre in nombres:
        if nombre > 0:
            nombre_positif += 1
    return nombre_positif

while True:
    mes_nombres = [int(x) for x in input('nombre ').split()]
    print(compte_pos(mes_nombres))
