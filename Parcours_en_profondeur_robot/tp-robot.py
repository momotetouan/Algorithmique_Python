# coding: utf-8

from GUI import GUI
import random


def voisins(G, pos):
    
    positions=[(-1,0),(1,0),(0,-1),(0,1)]
    listePos=[]
    for p in positions:
        if(G[pos[0]+p[0]][pos[1]+p[1]]!='wall'):
            listePos.append((pos[0]+p[0],pos[1]+p[1]))

    return listePos


def ParcoursRobot(G, depart, gui):
    atteint = set()
    chemin = {}
    P = [depart]
    chemin[depart]=[depart]
    prev_chemin=[depart]
    while P :
        u = P.pop(0)
        i,j=u
        if G[i][j]=='cookie':
            gui.deplacer_oscar(prev_chemin, chemin[u])
            break;
                
        if u not in atteint :
            atteint.add(u)
            gui.deplacer_oscar(prev_chemin, chemin[u])
            for v in voisins(G,u) :
                P.append(v)
                chemin[v]=chemin[u]+[v]
            prev_chemin = chemin[u]
                
    
                
    


def creer_grille(l, c):
    # Initialiser la grille avec des cellules d'herbe
    G = [['grass' for j in range(c)] for i in range(l)]

    # Placer des murs sur les bords de la grille
    for i in range(l):
        G[i][0] = 'wall'
        G[i][c-1] = 'wall'
    for j in range(c):
        G[0][j] = 'wall'
        G[l-1][j] = 'wall'

    # Placer des murs aléatoirement
    nb_murs = random.randint(0, l*c//4)  # On limite le nombre de murs pour éviter de bloquer le robot
    for i in range(nb_murs):
        x = random.randint(1, l-2)
        y = random.randint(1, c-2)
        G[x][y] = 'wall'

    # Placer le cookie
    cookie_place = False
    while not cookie_place:
        x = random.randint(1, l-2)
        y = random.randint(1, c-2)
        if G[x][y] == 'grass':
            G[x][y] = 'cookie'
            cookie_place = True

    # Placer Oscar
    robot_place = False
    while not robot_place:
        x = random.randint(1, l-2)
        y = random.randint(1, c-2)
        if G[x][y] == 'grass':
            G[x][y] = 'robot'
            robot_place = True
            robot_pos = (x,y)

    return G, robot_pos


    
    
    

if __name__ == '__main__':
    grille, pos_robot = creer_grille(12,20)
    GUI(grille, pos_robot, ParcoursRobot)
   


