import math

#On crée et initialise la classe processus
class Processus:
    def __init__(self,id,prio,pred,enext):
        self.id=id
        self.prio=prio
        self.pred=pred
        self.enext=enext


#On crée et initialise la classe BasicQueue,on initialise le mode priorité a faux
class BasicQueue:
    def __init__(self):
        self.first=None
        self.__priority=False

#La methode add permet d'ajoueter un processus a la file, on différencie un premier ajout a la liste d'un ajout quelquonque et on place chaque nouvel élément en fin de liste
    def add(self,id,prio):
        toAdd=Processus(id,prio,None,None)
        if self.__isEmpty():
            self.first=toAdd
            self.first.enext=self.first
            self.first.pred=self.first
        else:
            last=self.first.pred
            toAdd.enext=self.first
            toAdd.pred=last
            self.first.pred=toAdd
            last.enext=toAdd
#Renvoie la priorité
    def __getPriority(self):
        return self.__priority
#Renvoie si la file est vide ou non
    def __isEmpty(self):
        if self.first==None:
            return True
#Renvoie la totalité des éléments de la file, on utilise d'abord une boucle while pour déterminer la longueur de la liste puis on crée une liste auquel on rajoute chacun des processus avec une boucle for
    def return_self(self):
        if self.__isEmpty():
            return "BasicQueue is empty"
        else:
            list=[]
            toreturn=self.first
            index=self.first.enext
            p=1
            while index!=self.first:
                p+=1
                index=index.enext
            for i in range (p):
                list.append(toreturn.id)
                toreturn=toreturn.enext
            return list
#Permet de faire sortir le prochain processus a devoir sortir de la file, on différencie les différents mode de priorité, et on affciche quand la file est vide, pour le mode priorité on utilise une boucle while pour déterminer le processus a sortir
    def pop(self):
        if self.__isEmpty():
            return "BasicQueue is empty"
        if self.first==self.first.enext:
            popout=self.first
            self.first=None
            return popout.id, popout.prio
        if self.__priority==False:
            popout=self.first
            self.first.enext.pred=self.first.pred
            self.first.pred.enext=self.first.enext
            self.first=self.first.enext
            return popout.id, popout.prio
        if self.__getPriority():
            popout = self.first
            index = self.first.enext
            while index != self.first:
                if index.prio > popout.prio:
                    popout = index
                index = index.enext
            if popout == self.first:
                self.first = self.first.enext
            popout.enext.pred = popout.pred
            popout.pred.enext = popout.enext
            return popout.id, popout.prio
#permet de changer le mode de priorité
    def setPriorityMode(self,priority=False):
        self.__priority=priority
