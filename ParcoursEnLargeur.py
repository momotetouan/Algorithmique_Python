def ParcoursLargeur(G,s):
    etat = dict() # etat est un dictionnaire (vide pour le moment)
    F=[]
    for u in G:
        etat[u]="non atteint"
        
    etat[s]="atteint"
    F=[s]
    while F: # pour tester si la file est vide, ou de façon explicite : while len(F)!=0
        u=F.pop(0) # pour extraire (et supprimer) le premier élément de la file F
        for v in G[u]:
            if etat[v]=="non atteint":
                etat[v]="atteint"
                F.append(v)
        etat[u]="traité"
        print("Le sommet",u,"est traité")