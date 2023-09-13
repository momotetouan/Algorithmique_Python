# coding: utf-8

import tkinter as tk
from threading import Event, Thread
from GUI import MotionPlanning
from priority_dict import priority_dict
import pickle


def creerObstaclesEtGraphesVisibilite(w, h, file=None):
    """Cette fonction retourne une liste de polygones, où chaque polygone
    est représenté par une liste de coordonnées (x,y) de ses sommets,
    où 0<=x<=w et 0<=y<=h.
    Exemple: [[(Ax1,Ay1), (Ax2,Ay2), ..., (Axk,Ayk)], [(Bx1,By1), (Bx2,By2), ..., (Bxt,Byt)], ...]
    La fonction retourne aussi la position initiale du robot (x,y) et la cible à atteindre (x,y).
    La fonction retourne le graphe de visibilité pondéré.
    """
    with open(file, "rb") as fichier:
        (polygons, positionRobot, positionSortie, G) = pickle.load(fichier)

    return polygons, positionRobot, positionSortie, G


def cheminD(gui, G, posInit, posFinal):
    """cette fonction prend en entrée l'interface graphique gui;
    le graphe de visibilité G, le sommet de départ du robot (posInit)
    et le sommet d'arrivée posFinal"""
    d=dict()
    p=dict()
    
    # Si vous souhaitez cacher les arêtes du graphes, supprimez les 3 lignes suivantes (ou mettez les en commentaires)
    
    F = priority_dict()
    # Commencer par programmer l'algorithme de Dijkstra
    for v in G:
        d[v]=float('+infinity')
        p[v]=None
        F[v]=float('+infinity')
    
    d[posInit]=0
   
    F[posInit]=d[posInit]
    while F:
        u = F.pop_smallest()
        
        for v in G[u]:
            if d[v]>d[u]+G[u][v]:
                d[v]=d[u]+G[u][v]
                p[v]=u
                F[v]=d[v]
                
    
    chemin=[posFinal]
    pred = p[posFinal]
    while pred != posInit :
        chemin.append(pred)
        pred=p[pred]
    chemin.reverse()
    
    for u in chemin:
        gui.deplacer_oscar(u)
    
                

        

def cheminB(gui, G, posInit, posFinal):
    d=dict()
    p=dict()
    
    # Si vous souhaitez cacher les arêtes du graphes, supprimez les 3 lignes suivantes (ou mettez les en commentaires)
    
    F = priority_dict()
    # Commencer par programmer l'algorithme de Dijkstra
    for v in G:
        d[v]=float('+infinity')
        p[v]=None
        F[v]=float('+infinity')
    
    d[posInit]=0
    for i in range(1,len(G)):
        for u in G:
            for v in G[u]:
                if d[v]>d[u]+G[u][v]:
                    d[v]=d[u]+G[u][v]
                    p[v]=u
                    F[v]=d[v]
                    
    for u in G:
        for v in G[u]:
            if d[v]>d[u]+G[u][v]:
                print("présence d'un cycle absorbant")
            
        
    
    chemin=[posFinal]
    pred = p[posFinal]
    while pred != posInit :
        chemin.append(pred)
        pred=p[pred]
    chemin.reverse()
    
    for u in chemin:
        gui.deplacer_oscar(u)
    
    
    # puis faire parcourir le plus court chemin par Oscar en utilisant la fonction gui.deplacer_oscar(v)

    ######################################################################################
    # à vous de jouer ci-dessous ! Vous pouvez programmer d'autres fonctions si besoin   #
    ######################################################################################
    


if __name__ == "__main__":
    # RIEN A MODIFIER ICI (excepté pour choisir la scene: scene1.pickle OU scene2.pickle)
    root = tk.Tk()
    width, height = 800, 600
    polygons, posInit, posFinal, graphe = creerObstaclesEtGraphesVisibilite(
        width, height, "scene1.pickle"
    )
    gui = MotionPlanning(root, width, height, polygons, posInit, posFinal)

    # Launch a Thread running the main program to move the robot
    def runwrapper():
        cheminB(gui, graphe, posInit, posFinal)

    th = Thread(target=runwrapper)
    th.daemon = True
    root.after(100, th.start)

    root.mainloop()
