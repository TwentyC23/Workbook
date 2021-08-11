from tkinter import *
from Calculator import *
from Conditions import *

class Gui(Canvas):
    def __init__(self,root):
        self.root=root
        self.calc = Calculator()
        Canvas.__init__(self, self.root, width =  500 , height = 100, highlightthickness = 0)
        self.draw_buttons()
        self.L1.pack()
        self.L2.pack()
        self.B.pack()
        self.Date=None
        self.Patch=None
        self.Time=None
        self.Side=None
        self.Champ=None
        self.ChampE=None
        self.Team=None
    def draw_buttons(self):
        self.L1=Label(self.root,text="Bienvenue dans le programme d'aide a l'analyse de Scrim")
        self.L2=Label(self.root,text=Calculator.calc_winrate(self))
        self.B=Button(self.root, text="Lancer l'analyse avec conditions", command=self.B)
        self.B1=Button(self.root, text = "Date",  command=self.date)
        self.B2=Button(self.root, text = "Patch", command=self.patch)
        self.B3=Button(self.root, text = "Time" , command=self.time)
        self.B4=Button(self.root, text = "Side", command=self.side)
        self.B5=Button(self.root, text = "Champion", command=self.champ)
        self.B6=Button(self.root, text = "Champion en face", command=self.champE)
        self.B7=Button(self.root, text = "Ennemyteam", command=self.team)
        self.LDate=Label(self.root,text= "Entrez la date")
        self.EDate=Entry(self.root)
        self.BDate=Button(self.root,text="Valider la date",command=self.add_date)
        self.LPatch=Label(self.root,text= "Entrez le patch")
        self.EPatch=Entry(self.root)
        self.BPatch=Button(self.root,text="Valider le patch",command=self.add_patch)
        self.LTime=Label(self.root,text= "Entrez le temps")
        self.ETime=Entry(self.root)
        self.BTime=Button(self.root,text="Valider le temps",command=self.add_time)
        self.LSide=Label(self.root,text= "Entrez le Side")
        self.ESide=Entry(self.root)
        self.BSide=Button(self.root,text="Valider le side",command=self.add_side)
        self.LChamp=Label(self.root,text= "Entrez le champion")
        self.EChamp=Entry(self.root)
        self.BChamp=Button(self.root,text="Valider le champion",command=self.add_champ)
        self.LChampE=Label(self.root,text= "Entrez le champion ennemi")
        self.EChampE=Entry(self.root)
        self.BChampE=Button(self.root,text="Valider le champion ennemi",command=self.add_champE)
        self.LTeam=Label(self.root,text= "Entrez l'équipe ennemi")
        self.ETeam=Entry(self.root)
        self.BTeam=Button(self.root,text="Valider l'équipe ennemi",command=self.add_team)
        self.BSubmit=Button(self.root, text="Lancer l'analyse",command=self.analyze)

    def B(self):
        self.B1.pack()
        self.B2.pack()
        self.B3.pack()
        self.B4.pack()
        self.B5.pack()
        self.B6.pack()
        self.B7.pack()
        self.BSubmit.pack()

    def date(self):
        self.LDate.pack()
        self.EDate.pack()
        self.BDate.pack()

    def patch(self):
        self.LPatch.pack()
        self.EPatch.pack()
        self.BPatch.pack()

    def time(self):
        self.LTime.pack()
        self.ETime.pack()
        self.BTime.pack()

    def side(self):
        self.LSide.pack()
        self.ESide.pack()
        self.BSide.pack()

    def champ(self):
        self.LChamp.pack()
        self.EChamp.pack()
        self.BChamp.pack()

    def champE(self):
        self.LChampE.pack()
        self.EChampE.pack()
        self.BChampE.pack()

    def team(self):
        self.LTeam.pack()
        self.ETeam.pack()
        self.BTeam.pack()

    def add_date(self):
        self.calc.cond.Dateon=True
        self.Date=self.EDate.get()

    def add_patch(self):
        self.calc.cond.Patchon=True
        self.Patch=self.EPatch.get()

    def add_time(self):
        self.calc.cond.Timeon=True
        self.Time=self.ETime.get()

    def add_side(self):
        self.calc.cond.Sideon=True
        self.Side=self.ESide.get()

    def add_champ(self):
        self.calc.cond.Championon=True
        self.Champ=self.EChamp.get()

    def add_champE(self):
        self.calc.cond.Ennemychampon=True
        self.ChampE=self.EChampE.get()

    def add_team(self):
        self.calc.cond.Ennemyteamon=True
        self.Team=self.ETeam.get()

    def analyze(self):
        self.calc.valid_conditional_games(self.Date,self.Patch,self.Time,self.Side,self.Champ,self.ChampE,self.Team)
        self.calc.valid_conditional_games_choice()
        self.FinalL=Label(self.root,text=self.calc.calc_conditionnal_winrate())
        self.FinalL.pack()
