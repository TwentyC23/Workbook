from Bridge import Bridge
from Conditions import Conditions

class Calculator():
    def __init__(self):
        self.bridge=Bridge()
        self.cond=Conditions()
        self.calc_winrate()
        self.dv=[]
        self.dp=[]
        self.dt=[]
        self.ds=[]
        self.dc=[]
        self.dcE=[]
        self.dte=[]
    def calc_winrate(self):
        self.win=Bridge().get_numberofwins()
        self.winrate=(self.win/(Bridge().rows-1)*100)
        return f"Le pourcentage de victoire de la base de donnée est: {self.winrate}"

    def valid_conditional_games(self,date,patch,time,side,champ,champE,team):
        for i in range (len(self.bridge.games)):
            if self.cond.Dateon==True:
                if self.bridge.games[i].date==date:
                    self.dv.append(True)
                else: self.dv.append(False)
            else: self.dv.append(True)
            if self.cond.Patchon==True:
                if self.bridge.games[i].patch==patch:
                    self.dp.append(True)
                else: self.dp.append(False)
            else: self.dp.append(True)
            if self.cond.Timeon==True:
                if self.bridge.games[i].time==time:
                    self.dt.append(True)
                else: self.dt.append(False)
            else: self.dt.append(True)
            if self.cond.Sideon==True:
                if self.bridge.games[i].side==side:
                    self.ds.append(True)
                else: self.ds.append(False)
            else: self.ds.append(True)
            if self.cond.Championon==True:
                if self.bridge.games[i].top==champ or self.bridge.games[i].jun==champ or self.bridge.games[i].mid==champ or self.bridge.games[i].adc==champ or self.bridge.games[i].supp==champ:
                    self.dc.append(True)
                else: self.dc.append(False)
            else: self.dc.append(True)
            if self.cond.Ennemychampon==True:
                if self.bridge.games[i].e_top==champE or self.bridge.games[i].e_jun==champE or self.bridge.games[i].e_mid==champE or self.bridge.games[i].e_adc==champE or self.bridge.games[i].e_supp==champE:
                    self.dcE.apppend(True)
                else: self.dcE.append(False)
            else: self.dcE.append(True)
            if self.cond.Ennemyteamon==True:
                if self.bridge.games[i].patch==team:
                    self.dte.append(True)
                else: self.dte.append(False)
            else: self.dte.append(True)
    def valid_conditional_games_choice(self):
        self.valid_games=[]
        for i in range (len (self.bridge.games)):
            if all([self.dv[i],self.dp[i],self.dt[i],self.ds[i],self.dc[i],self.dcE[i],self.dte[i]]):
                self.valid_games.append(self.bridge.games[i])

    def calc_conditionnal_winrate(self):
        if self.valid_games==[]:
            return "Aucune partie ne correspond au critère choisis"
        else:
            self.cwin=0
            for i in range (len(self.valid_games)):
                if self.valid_games[i].win=="Win":
                    self.cwin+=1
            self.cwinrate=(self.cwin/len(self.valid_games)*100)
            return f"Le pourcentage de victoire avec ces conditions est  {self.cwinrate}"
