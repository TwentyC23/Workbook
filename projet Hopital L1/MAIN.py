from tkinter import*
from classe import*
from database import *

fenetre=Tk()

def deftime():
    for b in fenetre.pack_slaves():
        b.destroy()
    global h2
    global h4
    h1=Label(fenetre,text="entrez l'heure: (0-23)")
    h2=Entry(fenetre)
    h3=Label(fenetre,text="entrez les minutes:(0-59)")
    h4=Entry(fenetre)        
    h5=Button(fenetre, text="Valider l'heure",command=time)
    h1.pack()
    h2.pack()
    h3.pack()
    h4.pack()
    h5.pack()
    h7=Button(fenetre, text="Continuer", command=valid).pack()

def time():
    global hour
    global minut
    hour1=h2.get()
    minut1=h4.get()
    hour=int(hour1)
    minut=int(minut1)
    if hour<0 or hour>=24:
        raise NonValidHourError('entrez une heure valide')
    elif minut<0 or minut>=60:
        raise NonValidHourError('entrez une heure valide')
    else:
        time=str(hour)+":"+str(minut)
        h6=Label(fenetre, text=time)
        h6.pack()



def a():
    for b in fenetre.pack_slaves():
        b.destroy()
    b12=Button(fenetre, text=s12.sy, command=p0).pack()
    b13=Button(fenetre, text=s13.sy, command=p1).pack()
    b14=Button(fenetre, text=s14.sy, command=p2).pack()
    b15=Button(fenetre, text=s15.sy, command=p3).pack()
    b16=Button(fenetre, text=s16.sy, command=p4).pack()
def z():
    for b in fenetre.pack_slaves():
            b.destroy()
    b17=Button(fenetre, text=s21.sy, command=p5).pack()
def c():
    for b in fenetre.pack_slaves():
            b.destroy()
    b18=Button(fenetre, text=s31.sy, command=p6).pack()
    b19=Button(fenetre, text=s32.sy, command=p7).pack()
    b20=Button(fenetre, text=s33.sy, command=p8).pack()
    b21=Button(fenetre, text=s33.sy, command=p9).pack()
def d():
    for b in fenetre.pack_slaves():
            b.destroy()
    b22=Button(fenetre, text=s41.sy, command=p10).pack()
    b23=Button(fenetre, text=s42.sy, command=p11).pack()
    b24=Button(fenetre, text=s43.sy, command=p12).pack()
    b25=Button(fenetre, text=s44.sy, command=p13).pack()
    b26=Button(fenetre, text=s45.sy, command=p14).pack()
def e():
    for b in fenetre.pack_slaves():
            b.destroy()
    b27=Button(fenetre, text=s51.sy, command=p15).pack()
    b28=Button(fenetre, text=s52.sy, command=p16).pack()
    b29=Button(fenetre, text=s53.sy, command=p17).pack()
    b30=Button(fenetre, text=s54.sy, command=p18).pack()
def f():
    for b in fenetre.pack_slaves():
            b.destroy()
    b31=Button(fenetre, text=s61.sy, command=p19).pack()
    b32=Button(fenetre, text=s62.sy, command=p20).pack()
    b33=Button(fenetre, text=s63.sy, command=p21).pack()
def g():
    for b in fenetre.pack_slaves():
            b.destroy()
    b34=Button(fenetre, text=s71.sy, command=p22).pack()
    b35=Button(fenetre, text=s72.sy, command=p23).pack()
    b36=Button(fenetre, text=s73.sy, command=p24).pack()
def h():
    for b in fenetre.pack_slaves():
            b.destroy()
    b37=Button(fenetre, text=s81.sy, command=p25).pack()
    b38=Button(fenetre, text=s82.sy, command=p26).pack()
    b39=Button(fenetre, text=s83.sy, command=p27).pack()
    b40=Button(fenetre, text=s84.sy, command=p28).pack()
    b41=Button(fenetre, text=s85.sy, command=p29).pack()
    
def i():
    for b in fenetre.pack_slaves():
            b.destroy()
    b42=Button(fenetre, text=s91.sy, command=p30).pack()
    b43=Button(fenetre, text=s92.sy, command=p31).pack()
    b44=Button(fenetre, text=s93.sy, command=p32).pack()
def j():
    for b in fenetre.pack_slaves():
            b.destroy()
    b45=Button(fenetre, text=s101.sy, command=p33).pack()
    b46=Button(fenetre, text=s102.sy, command=p34).pack()
    b47=Button(fenetre, text=s103.sy, command=p35).pack()
    b48=Button(fenetre, text=s104.sy, command=p36).pack()
    
def k():
    for b in fenetre.pack_slaves():
            b.destroy()
    b49=Button(fenetre, text=s111.sy, command=p37).pack()
    b50=Button(fenetre, text=s112.sy, command=p38).pack()
def p0():
    for b in fenetre.pack_slaves():
            b.destroy()
    f1=Label(fenetre, text="Vous avez rendez vous avec "+s12.m.nom+", "+s12.m.spec+" à l'étage n°"+str(s12.m.floor)+", salle "+str(s12.m.room)+s12.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p1():
    for b in fenetre.pack_slaves():
            b.destroy()    
    f2=Label(fenetre, text="Vous avez rendez vous avec "+s13.m.nom+", "+s13.m.spec+" à l'étage n°"+str(s13.m.floor)+", salle "+str(s13.m.room)+s13.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p2():
    for b in fenetre.pack_slaves():
            b.destroy()
    f3=Label(fenetre, text="Vous avez rendez vous avec "+s14.m.nom+", "+s14.m.spec+" à l'étage n°"+str(s14.m.floor)+", salle "+str(s14.m.room)+s14.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p3():
    for b in fenetre.pack_slaves():
            b.destroy()
    f4=Label(fenetre, text="Vous avez rendez vous avec "+s15.m.nom+", "+s15.m.spec+" à l'étage n°"+str(s15.m.floor)+", salle "+str(s15.m.room)+s15.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p4():
    for b in fenetre.pack_slaves():
            b.destroy()
    f5=Label(fenetre, text="Vous avez rendez vous avec "+s16.m.nom+", "+s16.m.spec+" à l'étage n°"+str(s16.m.floor)+", salle "+str(s16.m.room)+s16.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p5():
    for b in fenetre.pack_slaves():
            b.destroy()
    f6=Label(fenetre, text="Vous avez rendez vous avec "+s21.m.nom+", "+s21.m.spec+" à l'étage n°"+str(s21.m.floor)+", salle "+str(s21.m.room)+s21.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p6():
    for b in fenetre.pack_slaves():
            b.destroy()
    f7=Label(fenetre, text="Vous avez rendez vous avec "+s31.m.nom+", "+s31.m.spec+" à l'étage n°"+str(s31.m.floor)+", salle "+str(s31.m.room)+s31.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p7():
    for b in fenetre.pack_slaves():
            b.destroy()
    f8=Label(fenetre, text="Vous avez rendez vous avec "+s32.m.nom+", "+s32.m.spec+" à l'étage n°"+str(s32.m.floor)+", salle "+str(s32.m.room)+s32.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p8():
    for b in fenetre.pack_slaves():
            b.destroy()
    f9=Label(fenetre, text="Vous avez rendez vous avec "+s33.m.nom+", "+s33.m.spec+" à l'étage n°"+str(s33.m.floor)+", salle "+str(s33.m.room)+s33.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p9():
    for b in fenetre.pack_slaves():
            b.destroy()
    f10=Label(fenetre, text="Vous avez rendez vous avec "+s34.m.nom+", "+s34.m.spec+" à l'étage n°"+str(s34.m.floor)+", salle "+str(s34.m.room)+s34.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p10():
    for b in fenetre.pack_slaves():
            b.destroy()
    f11=Label(fenetre, text="Vous avez rendez vous avec "+s41.m.nom+", "+s41.m.spec+" à l'étage n°"+str(s41.m.floor)+", salle "+str(s41.m.room)+s41.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p11():
    for b in fenetre.pack_slaves():
            b.destroy()
    f12=Label(fenetre, text="Vous avez rendez vous avec "+s42.m.nom+", "+s42.m.spec+" à l'étage n°"+str(s42.m.floor)+", salle "+str(s42.m.room)+s42.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p12():
    for b in fenetre.pack_slaves():
            b.destroy()
    f13=Label(fenetre, text="Vous avez rendez vous avec "+s43.m.nom+", "+s43.m.spec+" à l'étage n°"+str(s43.m.floor)+", salle "+str(s43.m.room)+s43.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p13():
    for b in fenetre.pack_slaves():
            b.destroy()
    f14=Label(fenetre, text="Vous avez rendez vous avec "+s44.m.nom+", "+s44.m.spec+" à l'étage n°"+str(s44.m.floor)+", salle "+str(s44.m.room)+s44.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p14():
    for b in fenetre.pack_slaves():
            b.destroy()
    f15=Label(fenetre, text="Vous avez rendez vous avec "+s45.m.nom+", "+s45.m.spec+" à l'étage n°"+str(s45.m.floor)+", salle "+str(s45.m.room)+s45.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p15():
    for b in fenetre.pack_slaves():
            b.destroy()
    f16=Label(fenetre, text="Vous avez rendez vous avec "+s51.m.nom+", "+s51.m.spec+" à l'étage n°"+str(s51.m.floor)+", salle "+str(s51.m.room)+s51.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p16():
    for b in fenetre.pack_slaves():
            b.destroy()
    f17=Label(fenetre, text="Vous avez rendez vous avec "+s52.m.nom+", "+s52.m.spec+" à l'étage n°"+str(s52.m.floor)+", salle "+str(s52.m.room)+s52.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p17():
    for b in fenetre.pack_slaves():
            b.destroy()
    f18=Label(fenetre, text="Vous avez rendez vous avec "+s53.m.nom+", "+s53.m.spec+" à l'étage n°"+str(s53.m.floor)+", salle "+str(s53.m.room)+s53.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p18():
    for b in fenetre.pack_slaves():
            b.destroy()
    f19=Label(fenetre, text="Vous avez rendez vous avec "+s54.m.nom+", "+s54.m.spec+" à l'étage n°"+str(s54.m.floor)+", salle "+str(s54.m.room)+s54.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p19():
    for b in fenetre.pack_slaves():
            b.destroy()
    f20=Label(fenetre, text="Vous avez rendez vous avec "+s61.m.nom+", "+s61.m.spec+" à l'étage n°"+str(s61.m.floor)+", salle "+str(s61.m.room)+s61.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p20():
    for b in fenetre.pack_slaves():
            b.destroy()
    f21=Label(fenetre, text="Vous avez rendez vous avec "+s62.m.nom+", "+s62.m.spec+" à l'étage n°"+str(s62.m.floor)+", salle "+str(s62.m.room)+s62.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p21():
    for b in fenetre.pack_slaves():
            b.destroy()
    f22=Label(fenetre, text="Vous avez rendez vous avec "+s63.m.nom+", "+s63.m.spec+" à l'étage n°"+str(s63.m.floor)+", salle "+str(s63.m.room)+s63.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p22():
    for b in fenetre.pack_slaves():
            b.destroy()
    f23=Label(fenetre, text="Vous avez rendez vous avec "+s71.m.nom+", "+s71.m.spec+" à l'étage n°"+str(s71.m.floor)+", salle "+str(s71.m.room)+s71.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p23():
    for b in fenetre.pack_slaves():
            b.destroy()
    f24=Label(fenetre, text="Vous avez rendez vous avec "+s72.m.nom+", "+s72.m.spec+" à l'étage n°"+str(s72.m.floor)+", salle "+str(s72.m.room)+s72.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p24():
    for b in fenetre.pack_slaves():
            b.destroy()
    f25=Label(fenetre, text="Vous avez rendez vous avec "+s73.m.nom+", "+s73.m.spec+" à l'étage n°"+str(s73.m.floor)+", salle "+str(s73.m.room)+s73.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p25():
    for b in fenetre.pack_slaves():
            b.destroy()
    f26=Label(fenetre, text="Vous avez rendez vous avec "+s81.m.nom+", "+s81.m.spec+" à l'étage n°"+str(s81.m.floor)+", salle "+str(s81.m.room)+s81.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p26():
    for b in fenetre.pack_slaves():
            b.destroy()
    f27=Label(fenetre, text="Vous avez rendez vous avec "+s82.m.nom+", "+s82.m.spec+" à l'étage n°"+str(s82.m.floor)+", salle "+str(s82.m.room)+s82.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p27():
    for b in fenetre.pack_slaves():
            b.destroy()
    f28=Label(fenetre, text="Vous avez rendez vous avec "+s83.m.nom+", "+s83.m.spec+" à l'étage n°"+str(s83.m.floor)+", salle "+str(s83.m.room)+s83.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p28():
    for b in fenetre.pack_slaves():
            b.destroy()
    f29=Label(fenetre, text="Vous avez rendez vous avec "+s84.m.nom+", "+s84.m.spec+" à l'étage n°"+str(s84.m.floor)+", salle "+str(s84.m.room)+s84.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p29():
    for b in fenetre.pack_slaves():
            b.destroy()
    f30=Label(fenetre, text="Vous avez rendez vous avec "+s85.m.nom+", "+s85.m.spec+" à l'étage n°"+str(s85.m.floor)+", salle "+str(s85.m.room)+s85.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p30():
    for b in fenetre.pack_slaves():
            b.destroy()
    f31=Label(fenetre, text="Vous avez rendez vous avec "+s91.m.nom+", "+s91.m.spec+" à l'étage n°"+str(s91.m.floor)+", salle "+str(s91.m.room)+s91.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p31():
    for b in fenetre.pack_slaves():
            b.destroy()
    f32=Label(fenetre, text="Vous avez rendez vous avec "+s92.m.nom+", "+s92.m.spec+" à l'étage n°"+str(s92.m.floor)+", salle "+str(s92.m.room)+s92.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p32():
    for b in fenetre.pack_slaves():
            b.destroy()
    f33=Label(fenetre, text="Vous avez rendez vous avec "+s93.m.nom+", "+s93.m.spec+" à l'étage n°"+str(s93.m.floor)+", salle "+str(s93.m.room)+s93.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p33():
    for b in fenetre.pack_slaves():
            b.destroy()
    f34=Label(fenetre, text="Vous avez rendez vous avec "+s101.m.nom+", "+s101.m.spec+" à l'étage n°"+str(s101.m.floor)+", salle "+str(s101.m.room)+s101.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p34():
    for b in fenetre.pack_slaves():
            b.destroy()
    f35=Label(fenetre, text="Vous avez rendez vous avec "+s102.m.nom+", "+s102.m.spec+" à l'étage n°"+str(s102.m.floor)+", salle "+str(s102.m.room)+s102.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p35():
    for b in fenetre.pack_slaves():
            b.destroy()
    f36=Label(fenetre, text="Vous avez rendez vous avec "+s103.m.nom+", "+s103.m.spec+" à l'étage n°"+str(s103.m.floor)+", salle "+str(s103.m.room)+s103.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p36():
    for b in fenetre.pack_slaves():
            b.destroy()
    f37=Label(fenetre, text="Vous avez rendez vous avec "+s104.m.nom+", "+s104.m.spec+" à l'étage n°"+str(s104.m.floor)+", salle "+str(s104.m.room)+s104.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p37():
    for b in fenetre.pack_slaves():
            b.destroy()
    f38=Label(fenetre, text="Vous avez rendez vous avec "+s111.m.nom+", "+s111.m.spec+" à l'étage n°"+str(s111.m.floor)+", salle "+str(s111.m.room)+s111.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def p38():
    for b in fenetre.pack_slaves():
            b.destroy()
    f39=Label(fenetre, text="Vous avez rendez vous avec "+s112.m.nom+", "+s112.m.spec+" à l'étage n°"+str(s112.m.floor)+", salle "+str(s112.m.room)+s112.u.temps+'').pack()
    br=Button(fenetre, text="Retour", command=valid).pack()
    bhr=Button(fenetre, text="Retour à la selection de l'heure", command=deftime).pack()
def valid():
    global hour
    global minut
    for b in fenetre.pack_slaves():
            b.destroy()
    e3=Label(fenetre, text=('{}:{}').format(hour,minut)).pack()
    e1=Label(fenetre, text="Entrez le symptomes principal:").pack()
    b1=Button(fenetre, text=s1.sy, command=a).pack()
    b2=Button(fenetre, text=s2.sy, command=z)
    b2.pack()
    b3=Button(fenetre, text=s3.sy, command=c).pack()
    b4=Button(fenetre, text=s4.sy, command=d).pack()
    b5=Button(fenetre, text=s5.sy, command=e).pack()
    b6=Button(fenetre, text=s6.sy, command=f).pack()
    b7=Button(fenetre, text=s7.sy, command=g).pack()
    b8=Button(fenetre, text=s8.sy, command=h).pack()
    b9=Button(fenetre, text=s9.sy, command=i).pack()
    b10=Button(fenetre, text=s10.sy, command=j).pack()
    b11=Button(fenetre, text=s11.sy, command=k).pack()

Bien=Label(fenetre, text="Bienvenue dans le programme d'acceuil aux urgence")
Lan=Button(fenetre, text="Lancez le programme",command=deftime)
Bien.pack()
Lan.pack()


fenetre.mainloop()

