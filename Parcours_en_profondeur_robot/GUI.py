from tkinter import Tk, PhotoImage, Label, NSEW
import time
from queue import Queue, Empty
from threading import Event, Thread

class GUI:

    def __init__(self, M, pos, rech):
        self.tk = Tk()
        self.photo_wall   = PhotoImage(file="wall.gif")
        self.photo_robot  = PhotoImage(file="robot.gif")
        self.photo_grass  = PhotoImage(file="grass.gif")
        self.photo_cookie = PhotoImage(file="cookie.gif")
        e={}
        for i in range(len(M)):
            for j in range(len(M[0])):
                e[i,j] = Label(self.tk, image=getattr(self, 'photo_'+M[i][j]))
                e[i,j].grid(row=i, column=j, columnspan=1, rowspan=1, sticky=NSEW)
        self.cells = e
        
        self.queue = Queue()
        self.deplacement_fini = Event()
        self.delai = 250

        def plus(e):
            self.delai = max(10, self.delai-50)
        self.tk.bind("+", plus)

        def minus(e):
            self.delai += 50
        self.tk.bind("-", minus)
        
        def quitter(e):
            self.tk.quit()
        self.tk.bind("q", quitter)

        self.tk.after(10, self.process_queue)

        def run():
            rech(M, pos, self)
        th = Thread(target=run)
        th.daemon = True
        self.tk.after(100, th.start)

        self.tk.mainloop()

    def process_queue(self):
        try:
            ch1,ch2 = self.queue.get(block=False)
            etapes = self.etapes_du_deplacement_d_oscar(ch1, ch2)
            etapes.reverse()
            self.tk.after(10, self.executer_etape, etapes)
        except Empty:
            self.tk.after(50, self.process_queue)

    def etapes_du_deplacement_d_oscar(self, chemin1, chemin2):
        steps = []
        pos = chemin1[-1]
        e = self.cells
        arriere = chemin1[:]
        while arriere:
            nxt = arriere.pop()
            steps.append((pos,nxt))
            pos = nxt
            if pos in chemin2:
                break
        i = chemin2.index(pos)
        avant = chemin2[i+1:]
        avant.reverse()
        while avant:
            nxt = avant.pop()
            steps.append((pos,nxt))
            pos = nxt
        return steps

    def executer_etape(self, etapes):
        pos1,pos2 = etapes.pop()
        self.cells[pos1].configure(image="")
        self.cells[pos2].configure(image=self.photo_robot)
        self.tk.update_idletasks()
        if etapes:
            self.tk.after(self.delai, self.executer_etape, etapes)
        else:
            self.tk.after(10, self.process_queue)
            self.deplacement_fini.set()

    def deplacer_oscar(self, chemin1, chemin2):
        self.deplacement_fini.clear()
        self.queue.put((chemin1, chemin2))
        self.deplacement_fini.wait()
