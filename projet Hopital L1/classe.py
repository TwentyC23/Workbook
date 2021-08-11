class medecin :
    def __init__(self,nom,spec,floor,room):
        self.nom=nom
        self.spec=spec
        self.floor=floor
        self.room=room

class pediatre (medecin):
    def __init__(self,s):
        self.spécialité_d_age=s
        medecin.__init__(self,nom,spec,floor,room)
        M1=pediatre("Nourisson")
        M7=pediatre("4-10_ans")

class generaliste (medecin):
     def __init__(self):
         medecin.__init__(self)
         M3=generaliste
         M4=generaliste
         M5=generaliste

class urgence:
    #Definie le niveau d'urgence#
    def __init__(self,lvl,exp,temps):
        self.lvl=lvl
        self.exp=exp
        self.temps=temps

class symptome:
    def __init__(self,sy):
        self.sy=sy

class fracture (symptome,urgence,medecin):
    def __init__(self,sy,u,m):
        self.sy=sy
        self.u=u
        self.m=m

class perte_des_eaux(symptome,urgence,medecin):
    def __init__(self,sy,u,m):
        self.sy=sy
        self.u=u
        self.m=m

class fièvre(symptome,urgence,medecin):
    def __init__(self,sy,u,m):
        self.sy=sy
        self.u=u
        self.m=m
class coupure (symptome,urgence,medecin):
    def __init__(self,sy,u,m):
        self.sy=sy
        self.u=u
        self.m=m
class brulure (symptome,urgence,medecin):
    def __init__(self,sy,u,m):
        self.sy=sy
        self.u=u
        self.m=m
class douleur_abdominal (symptome,urgence,medecin):
    def __init__(self,sy,u,m):
        self.sy=sy
        self.u=u
        self.m=m
class difficulté_respiratoire (symptome,urgence,medecin):
    def __init__(self,sy,u,m):
        self.sy=sy
        self.u=u
        self.m=m
class malaise (symptome,urgence,medecin):
    def __init__(self,sy,u,m):
        self.sy=sy
        self.u=u
        self.m=m
class vomi (symptome,urgence,medecin):
    def __init__(self,sy,u,m):
        self.sy=sy
        self.u=u
        self.m=m
class phsyco (symptome,urgence,medecin):
    def __init__(self,sy,u,m):
        self.sy=sy
        self.u=u
        self.m=m
class enfant (symptome,urgence,medecin):
    def __init__(self,sy,u,m):
        self.sy=sy
        self.u=u
        self.m=m
class NonValidHourError(Exception):
    pass
