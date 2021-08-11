#Cette partie est essentiellement identique a la BasicQueue, à l'exception qu'on utilise une liste en guise de tas, ce qui entraine des petites modifications dans le code des methodes
class _Processus:
    def __init__(self, id, prio, pred, enext):
        self.id = id
        self.prio = prio
        self.pred = pred
        self.enext = enext

class LinkedHeapQueue:
    def __init__(self):
        self.first = None
        self.__body = list()
        self.__priority = False

    def add(self, id, prio):
        toAdd = _Processus(id, prio,None,None)
        if self.__isEmpty():
            self.first = toAdd
            self.first.enext = self.first
            self.first.pred = self.first
        else:
            last_element = self.first.pred
            toAdd.pred = last_element
            toAdd.enext = self.first
            self.first.pred = toAdd
            last_element.enext = toAdd
        self.__body.append(toAdd)
        self.__body.sort(key = lambda x: x.prio, reverse = True)

    def __getPriorityMode(self):
        return self.__priority

    def __isEmpty(self):
        if self.first==None:
            return True

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

    def pop(self):
        if self.__isEmpty():
            return "LinkedHeapQueue is empty"
        if self.first == self.first.enext:
            popout = self.first
            self.first = None
            self.__body = list()
            return popout.id, popout.prio
        if not self.__getPriorityMode():
            popout = self.first
            self.__body = list(filter(lambda x: x != self.first, self.__body))
            self.first.enext.pred = self.first.pred
            self.first.pred.enext = self.first.enext
            self.first = self.first.enext
            return popout.id, popout.prio
        if self.__getPriorityMode():
            toPop = self.__body.pop(0)
            popout = self.first
            for m in range(len(self.__body) + 1):
                if popout == toPop:
                    break
                else: popout = popout.enext
            if popout == self.first:
                self.first = self.first.enext
            popout.enext.pred = popout.pred
            popout.pred.enext = popout.enext
            return popout.id, popout.prio

    def setPriorityMode(self, priority):
        self.__priority = priority
