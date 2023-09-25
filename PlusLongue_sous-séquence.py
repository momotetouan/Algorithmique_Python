def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)

    # Créer une table pour stocker les résultats intermédiaires
    lcs_table = [[0] * (n + 1) for _ in range(m + 1)]

    # Remplir la table en utilisant la programmation dynamique
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                lcs_table[i][j] = 1 + lcs_table[i - 1][j - 1]
            else:
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])

    # Reconstruire la sous-séquence la plus longue
    i, j = m, n
    lcs = []
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif lcs_table[i - 1][j] > lcs_table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))

# Exemple d'utilisation
chaine1 = "AGGTAB"
chaine2 = "GXTXAYB"
resultat = longest_common_subsequence(chaine1, chaine2)

print(f"La sous-séquence la plus longue est : {resultat}")
