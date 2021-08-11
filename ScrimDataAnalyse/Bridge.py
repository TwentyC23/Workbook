import subprocess
import sys
import matplotlib.pyplot as plt
try:
    import xlrd
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'xlrd'])
    import xlrd
import Game
import datetime

class Bridge:
    def __init__(self):
        self.bridge()
        self.get_numberofwins()
        self.upload_games()

    def bridge(self):
        self.doc=xlrd.open_workbook(r"D:\Cours\Projet rating LOL\ScrimDataAnalyse\testdata.xlsx")
        self.data=self.doc.sheet_by_index(0)
        self.rows=self.data.nrows
        self.cols=self.data.ncols

    def show_data(self):
        for row_index in range(self.data.nrows):
            for col_index in range(self.data.ncols):
                print (xlrd.cellname(row_index,col_index))
                print (self.data.cell(row_index,col_index).value)

    def get_numberofwins(self):
        self.nbofwin=0
        self.win_col=self.data.col_values(3,1)
        for i in self.win_col:
            if i=='Win':
                self.nbofwin+=1
        return self.nbofwin

    def create_dictionarry(self):
        self.dic={}
        self.dic["Date"]=self.data.col_values(0,1)
        self.dic["Ennemyteam"]=self.data.col_values(1,1)
        self.dic["patch"]=self.data.col_values(2,1)
        self.dic["Win"]=self.data.col_values(3,1)
        self.dic["Time"]=self.data.col_values(4,1)
        self.dic["Side"]=self.data.col_values(5,1)
        self.dic["Top"]=self.data.col_values(6,1)
        self.dic["jun"]=self.data.col_values(7,1)
        self.dic["mid"]=self.data.col_values(8,1)
        self.dic["adc"]=self.data.col_values(9,1)
        self.dic["supp"]=self.data.col_values(10,1)
        self.dic["e_top"]=self.data.col_values(11,1)
        self.dic["e_jun"]=self.data.col_values(12,1)
        self.dic["e_mid"]=self.data.col_values(13,1)
        self.dic["e_adc"]=self.data.col_values(14,1)
        self.dic["e_supp"]=self.data.col_values(15,1)

    def upload_games(self):
        self.games=[]
        for i in range (1,self.rows):
            self.games.append(Game.Game(str(datetime.date(*xlrd.xldate_as_tuple(self.data.cell_value(i,0),self.doc.datemode)[:3]))\
            ,self.data.cell_value(i,1)\
            ,self.data.cell_value(i,2)\
            ,self.data.cell_value(i,3)\
            ,self.data.cell_value(i,4)\
            ,self.data.cell_value(i,5)\
            ,self.data.cell_value(i,6)\
            ,self.data.cell_value(i,7)\
            ,self.data.cell_value(i,8)\
            ,self.data.cell_value(i,9)\
            ,self.data.cell_value(i,10)\
            ,self.data.cell_value(i,11)\
            ,self.data.cell_value(i,12)\
            ,self.data.cell_value(i,13)\
            ,self.data.cell_value(i,14)\
            ,self.data.cell_value(i,15)))
