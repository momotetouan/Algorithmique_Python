def tri_a_bulles(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]

# Exemple d'utilisation
if __name__ == "__main__":
    ma_liste = [64, 34, 25, 12, 22, 11, 90]
    print("Liste non triée:", ma_liste)
    tri_a_bulles(ma_liste)
    print("Liste triée:", ma_liste)
