    #On import tkinter et les deux fichier de fonction pour réaliser une Interface graphique
from tkinter import *
from BasicQueue import *
from LinkedHeapQueue import *


#On crée la fonction qui crée la fenetre tkinter et appelle la classe Interface
def main():
    Window=Tk()
    Window.geometry('500x300')
    g=Interface(Window)
    Window.mainloop()

#On utilise cette classe pour créer l'Interface graphique, on l'initie avec un écran d'acceuil
class Interface:
    def __init__(self,parent):
        self.parent=parent
        self.L1=Label(text="Bienvenue dans Iprocessus, votre résolveur de processus, powered by Prince T").pack(expand=1)
        self.L2=Button(text="Lancez le programme",command=self.P1).pack(expand=1)
#Premier page de l'Interface qui permet de choisir si l'on utilise une file classique ou en tas lié


    def P1(self):
        for b in self.parent.pack_slaves():
            b.destroy()
        self.L3=Label(text="Avant de commencer choissisez votre type de file d'attente:").pack(expand=1)
        self.L4=Button(text="File d'attente classique",command=self.P2).pack(expand=1)
        self.L5=Button(text="File d'attente en tas lié",command=self.P6).pack(expand=1)

#Page qui s'affiche si on choisit la file classique, on utilise des Label,Button et Entry ainsi que des Radiobutton qui permette de choisir le mode de priorité, on initie q en tant que BasicQueue
    def P2(self):
        for b in self.parent.pack_slaves():
            b.destroy()
        self.q=BasicQueue()
        L6=Label(text="Choissisez un mode de priorité:").pack()
        self.STVR=StringVar()
        self.L7A = Radiobutton(variable=self.STVR, text="Mode sans priorité", value="False", indicatoron=0)
        self.L7A.pack(expand=1)
        self.L7B=Radiobutton(variable=self.STVR, text="Mode priorité", value="True", indicatoron=0)
        self.L7B.pack()
        self.L8=Label(text="Entrez le nom du processus a ajouter:").pack()
        self.L9=Entry()
        self.L9.pack()
        self.L10=Label(text="Entrez le niveau de priorité du processus;").pack()
        self.L11=Entry()
        self.L11.pack()
        self.L12=Button(text="Ajouter un processus",command=self.P3).pack()
        self.L13=Button(text="Afficher la file", command=self.P4).pack()
        self.exist=None
        self.L15=Button(text="Faire sortir le premier Processus",command=self.P5).pack()
        self.exist2=None

#On utilise la methode add de BasicQueue pour ajouter un processus a la file.
    def P3(self):
        addid=self.L9.get()
        addprio=self.L11.get()
        try:
            addprio=int(addprio)
        except:
            raise ValueError("Entrez un entier pour la priorité")
        self.L9.delete(0,END)
        self.L11.delete(0,END)
        self.q.add(addid,addprio)

#On utilise la methode return_self de BasicQueue pour afficher la file.
    def P4(self):
        if self.exist==None:
            pass
        else:
            self.L14.destroy()
        self.L14=Label(text=str(self.q.return_self()))
        self.L14.pack()
        self.exist=True

#On utilise la methode pop pour sortir et afficher le processus a sortir de la file.
    def P5(self):
        if self.exist2==None :
            pass
        else:
            self.L16.destroy()
        mode=self.STVR.get()
        if mode=="True":
            self.q.setPriorityMode(True)
            self.L16=Label(text=self.q.pop())
            self.L16.pack()
            self.exist2=True
        else:
            self.q.setPriorityMode(False)
            self.L16=Label(text=self.q.pop())
            self.L16.pack()
            self.exist2=True
#Page qui s'affiche si on choisit la file en tas lié, similaire a P2

    def P6(self):
        for b in self.parent.pack_slaves():
            b.destroy()
        self.q=LinkedHeapQueue()
        L6=Label(text="Choissisez un mode de priorité:").pack()
        self.STVR=StringVar()
        self.L7A = Radiobutton(variable=self.STVR, text="Mode sans priorité", value="False", indicatoron=0)
        self.L7A.pack(expand=1)
        self.L7B=Radiobutton(variable=self.STVR, text="Mode priorité", value="True", indicatoron=0)
        self.L7B.pack()
        self.L8=Label(text="Entrez le nom du processus a ajouter:").pack()
        self.L9=Entry()
        self.L9.pack()
        self.L10=Label(text="Entrez le niveau de priorité du processus;").pack()
        self.L11=Entry()
        self.L11.pack()
        self.L12=Button(text="Ajouter un processus",command=self.P3).pack()
        self.L13=Button(text="Afficher la file", command=self.P4).pack()
        self.exist=None
        self.L15=Button(text="Faire sortir le premier Processus",command=self.P5).pack()
        self.exist2=None
#On lance la fonction main()
main()
