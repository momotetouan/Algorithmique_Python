def recherche_binaire(liste, element):
    debut = 0
    fin = len(liste) - 1

    while debut <= fin:
        milieu = (debut + fin) // 2
        if liste[milieu] == element:
            return milieu  # L'élément a été trouvé, retourne son indice
        elif liste[milieu] < element:
            debut = milieu + 1
        else:
            fin = milieu - 1

    return -1  # L'élément n'a pas été trouvé dans la liste

# Exemple d'utilisation
if __name__ == "__main__":
    ma_liste = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    element_recherche = 11
    indice = recherche_binaire(ma_liste, element_recherche)
    if indice != -1:
        print(f"L'élément {element_recherche} a été trouvé à l'indice {indice}.")
    else:
        print(f"L'élément {element_recherche} n'a pas été trouvé dans la liste.")
