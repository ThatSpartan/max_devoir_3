def sequenceDesDeux(nombres):
    for i in range(len(nombres)):
        if i+1 < len(nombres) and nombres[i] == nombres[i+1]:
            return True
    return False

while True:
    mes_nombres = [int(x) for x in input().split()]
    n=sequenceDesDeux(mes_nombres)
    print(n)
