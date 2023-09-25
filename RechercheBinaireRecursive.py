def recherche_binaire_recursive(liste, element, debut=0, fin=None):
    if fin is None:
        fin = len(liste) - 1

    if debut > fin:
        return -1

    milieu = (debut + fin) // 2

    if liste[milieu] == element:
        return milieu
    elif liste[milieu] < element:
        return recherche_binaire_recursive(liste, element, milieu + 1, fin)
    else:
        return recherche_binaire_recursive(liste, element, debut, milieu - 1)

# Exemple d'utilisation
ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element_recherche = 6
resultat = recherche_binaire_recursive(ma_liste, element_recherche)

if resultat != -1:
    print(f"L'élément {element_recherche} a été trouvé à l'index {resultat}.")
else:
    print(f"L'élément {element_recherche} n'a pas été trouvé dans la liste.")
