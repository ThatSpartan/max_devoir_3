def maxSequence(nombres):
    """max_sequence
    
    Fonction qui retourne la longeur de la sequence (une suite de nombre identique) maximal de la liste
    
    Arguments:
        nombres {list of int} -- Une liste contenant des integers
    
    Returns:
        int -- Returne la longeur de la séquence maximal
    """

    sequence = 1
    max_sequence = sequence
    # sois utiliser i+1 < len(nombres) OU range(len(nombres)-1) (ajouter le '-1')
    for i in range(len(nombres)):
        # vérifier chaque pair de nombre
        if i+1 < len(nombres) and nombres[i] == nombres[i+1]:
            # si la pair sont égale, la suite continue, sinon, la suite est 1 par défaut
            sequence += 1
            # si la séquence actuelle est plus grande que la séquence maximale, elle devient la nouvelle séquence maximale
            if sequence > max_sequence:
                max_sequence = sequence
        else:
            sequence = 1
    return max_sequence # retourner la longueur de la séquence maximale

# tests
# print(max_sequence([1, 1, 1, 1, 3, 5, 7])) # 4
# print(max_sequence([1, 1, 1, 1, 3, 3, 3, 3, 3, 5, 7])) # 5
# print(max_sequence([1, 1, 1, 1, 3, 3, 3, 3, 3, 5, 7, 7, 7, 7, 7, 7, 7, 7])) # 8

while True:
    print('\nCalculons la longeur de la séquence la plus longue.')
    mes_nombres = list(eval(input('Veuillez entrer plusieurs nombres séparés par des espaces ')))
    seq_max = maxSequence(mes_nombres)
    print(f"La séquence la plus longue contient {seq_max} nombres")
