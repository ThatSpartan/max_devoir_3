import random

def prepare_paquet(num):
    '''(int)->list of int
    Retourne une liste des entiers qui représentent le paquet étrange avec num valeurs.     

    >>> paquet=prepare_paquet(13)
   >>> paquet
   [101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404, 105, 205, 305, 405, 106, 206, 306, 406, 107, 207, 307, 407, 108, 208, 308, 408, 109, 209, 309, 409, 110, 210, 310, 410, 111, 211, 311, 411, 112, 212, 312, 412, 113, 213, 313, 413]

    >>> paquet=prepare_paquet(4)
    >>> paquet
    [101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404]
    
    '''

    paquet = []

    for valeur in range(1, num+1):
        for couleur in range(1, 5):
            paquet.append(couleur*100+valeur)
    
    return paquet

paquet = prepare_paquet(3)
print(paquet)

def shuffle_paquet(paquet):
    '''(list of int)->None
    Mélange le paquet pour changer l'ordre des cartes (l'ordre des entiers dans la liste paquet)

    Utiliser la fonction random.shuffle du module random.
    
    Parce que l'ordre dans la liste sera aléatoire, pour cette fonction
    votre résultat ne doit pas être le même que dans les exemples suivants:
   
    >>> paquet=[101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404]
    >>> shuffle_paquet(paquet)
    >>> paquet
    [102, 101, 302, 104, 304, 103, 301, 403, 401, 404, 203, 204, 303, 202, 402, 201]
    >>> shuffle_paquet(paquet)
    >>> paquet
    [402, 302, 303, 102, 104, 103, 203, 301, 401, 403, 204, 101, 304, 201, 404, 202]
    '''

    paquet.shuffle()


def donne_cartes_initiales(paquet):
    '''(list of int)-> list of int
    Retourne une liste qui représente la main initiale du joueur.
    On donne au joueur les premières 7 cartes de la liste paquet.
    Precondition: len(dec)>=7
    '''
    
    pass
     

def donne_nouvelles_cartes(paquet, joueur, num):
    '''(list of int, list of int, int)-> None
    Cette fonction prend le paquet qui reste, la main du joueur et un entier num,
    et donne num cartes au joueur, de haut du paquet.
    Si le nombre des cartes dans le paquet est inférieur au num, donne toute les cartes du paquet.

    Precondition: 1<=num<=52,  paquet et joueur sont de sub-sets disjoints du paquet étrange. 
    
    >>> paquet=[201, 303, 210, 407, 213, 313]
    >>> joueur=[302, 304, 404]
    >>> donne_nouvelles_cartes(paquet, joueur, 4)
    >>> joueur
    [302, 304, 404, 313, 213, 407, 210]
    >>> paquet
    [201, 303]
    >>>

    >>> paquet=[201, 303]
    >>> joueur=[302, 304, 404]
    >>> donne_nouvelles_cartes(paquet, joueur, 4)
    >>> joueur
    [302, 304, 404, 303, 201]
    >>> paquet
    []
    '''
    
    pass # remplacer par votre code


def print_paquet_deux_fois(main):
    '''(list)->None
    Affiche les éléments de la liste main deux fois.
    La première fois: ordonnée par couleur et après ca par valeur.
    La deuxième fois: ordonnée par valeurs.
    Precondition: main est un sub-set du paquet étrange.
    
    La fonction ne devrait pas changer l'ordre des éléments dans la liste main.
    Faîtes une copie de la liste et après ca appelez des fonctions de tri (sort).

    Exemple:
    >>> a=[311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]
    >>> print_paquet_deux_fois(a)
    101 104 105 202 204 301 303 305 306 311 313 401 407 408 409 410 
    101 301 401 202 303 104 204 105 305 306 407 408 409 410 311 313 
    >>> a
    [311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]

    '''

    pass # remplacer par votre code


def est_valide(cartes, joueur):
    '''(list of int, list of int)->bool
    La fonction retourne True si chaque carte dans la liste cartes est dans la main du joueur
    (dans la liste joueur).
    Sinon, elle affiche une message d'erreur et retourne False, comme dans les exemples suivantes.

    Precondition: cartes et joueur sont des sub-sets du paquet étrange.
    
    >>> est_valide([210,310],[201, 201, 210, 302, 311])
    310 n'est pas dans votre main. Entré invalide.
    False

    >>> est_valide([210,310],[201, 201, 210, 302, 310, 401])
    True
    '''
    for carte in cartes:
        if carte not in joueur:
            print(carte, "n'est pas dans votre main. Entré invalide.")
            return False
    return True

def est_valide_meme_valeur(cartes):
    '''(list of int)->True
    La fonction retourne True si les cartes dans la liste forment une combinaison valide
    de 2, 3 ou 4 carte de même valeur.
    Sinon elle retourne False. S'il n'y a pas assez des cartes pour former une combinaison valide,
    affiche un message, comme dans les exemples suivantes.
    
    Precondition: cartes est un sub-set du paquet étrange.

    Dans cette fonction, il ne faut pas convertir les cartes dans des chaines des caractères !!!
    
    >>> est_valide_meme_valeur([207, 107, 407])
    True
    >>> est_valide_meme_valeur([207, 107, 407])
    True
    >>> est_valide_meme_valeur([207, 107])
    Entré invalide. Les combinaisons valides de même valeur doit avoir au moins 2 cartes.
    False
    '''
    
    pass # remplacer par votre code
    


def est_valide_seq(cartes):
    '''(list of int)->True
    La fonction retourne True si la liste cartes contient une séquence qui est une combinaison valide.
    Sinon, affiche un message d'erreur et retourne False, comme dans les exemples suivantes.
    
    Precondition: cartes est un sub-set du paquet étrange.

    Dans cette fonction, il ne faut pas convertir les cartes dans des chaines des caractères !!!
    
    >>> est_valide_seq([313, 311, 312])
    True
    >>> est_valide_seq([311, 312, 313, 414])
    Entré invalide. Les séquences valides doit être de même couleur.
    False
    >>> est_valide_seq([201, 202])
    Entré invalide. Les séquences valides doit avoir au moins 3 cartes.
    False
    >>> est_valide_seq([])
    Entré invalide. Les séquences valides doit avoir au moins 3 cartes.
    False
    '''
    
    pass # remplacer par votre code


def manche_dé_1(joueur):
    '''(list of int)->None
    Cette fonction joue une manche, pour valeur 1 du dé. 
    Precondition: joueur un sub-set du paquet étrange.
    
    >>> manche_dé_1([201, 212, 102, 311])
    Défaussez une carte de votre choix.
    Quelle carte voulez-vous défausser? 103
    103
    Il n'y a pas cette carte dans votre main. Essayez encore une fois.
    Quelle carte voulez-vous défausser? 102
    Voici la main, affichée de deux manières:
    201 212 311 
    201 311 212
    '''
    
    pass # remplacer par votre code


def manche_dé_2_3_4_5_6(joueur):
    '''(list of int)->None
    Cette fonction joue une manche pour les valeurs 2, 3, 4, 5, ou 6 du dé.
    Precondition: joueur est un sub-set du paquet étrange.

    >>> manche_dé_2_3_4_5_6([401, 102, 403, 104, 203])
    Avez-vous une séquence de 3+ cartes de même couleur ou une combinaison de 2+ cartes de même valeur? (oui ou non) oui
    Quelle séquence de 3+ ou combinaison de 2+ carte de même valeur voulez-vous défausser? Entrez les cartes séparées par des espaces: 102 103 104
    103 n'est pas dans votre main. Entré invalide.
    Avez-vous une séquence de 3+ cartes de même couleur ou une combinaison de 2+ cartes de même valeur? (oui ou non)  oui
    Quelle séquence de 3+ ou combinaison de 2+ carte de même valeur voulez-vous défausser? Entrez les cartes séparées par des espaces: 403 203
    Voici la main, affichée de deux manières:
    102 104 401 
    401 102 104 
    Avez-vous une séquence de 3+ cartes de même couleur ou une combinaison de 2+ cartes de même valeur? (oui ou non)  non

    >>> manche_dé_2_3_4_5_6([211, 412, 411, 103, 413])
    Avez-vous une séquence de 3+ cartes de même couleur ou une combinaison de 2+ cartes de même valeur? (oui ou non) oui
    Quelle séquence de 3+ ou combinaison de 2+ carte de même valeur voulez-vous défausser? Entrez les cartes séparées par des espaces: 411 412 413
    Voici la main, affichée de deux manières:
    103 211 
    103 211 

    >>> manche_dé_2_3_4_5_6([211, 412, 411, 103, 413])
    Avez-vous une séquence de 3+ cartes de même couleur ou une combinaison de 2+ cartes de même valeur? (oui ou non) oui
    Quelle séquence de 3+ ou combinaison de 2+ carte de même valeur voulez-vous défausser? Entrez les cartes séparées par des espaces: 411 412
    Entré invalide. Les séquences valides doit avoir au moins 3 cartes.
    Avez-vous une séquence de 3+ cartes de même couleur ou une combinaison de 2+ cartes de même valeur? (oui ou non)  oui
    Quelle séquence de 3+ ou combinaison de 2+ carte de même valeur voulez-vous défausser? Entrez les cartes séparées par des espaces: 412 411 413
    Voici la main, affichée de deux manières:
    103 211 
    103 211 
    Avez-vous une séquence de 3+ cartes de même couleur ou une combinaison de 2+ cartes de même valeur? (oui ou non)  non
    
    >>> manche_dé_2_3_4_5_6([401, 102, 403, 104, 203])
    Avez-vous une séquence de 3+ cartes de même couleur ou une combinaison de 2+ cartes de même valeur? (oui ou non) ssd
    Avez-vous une séquence de 3+ cartes de même couleur ou une combinaison de 2+ cartes de même valeur? (oui ou non) o
    Avez-vous une séquence de 3+ cartes de même couleur ou une combinaison de 2+ cartes de même valeur? (oui ou non) non
    '''

    pass # remplacer par votre code

 
# programme pricipal (main)

# print("Bienvenue au jeu de rami.\n")
# change=input("Le paquet a 52 cartes: 13 valeurs x 4 couleurs.\nVoulez-vous changer le nombre des valeurs? ").strip().lower()

# AJOUTER VOTRE CODE
