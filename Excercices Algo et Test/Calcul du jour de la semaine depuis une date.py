from tkinter import *
import math

mod7mois=[0,3,3,6,1,4,6,2,5,0,3,5]
nomjour=['dimanche','lundi','mardi','mercredi','jeudi','vendredi','samedi']

def bis(annee):
    return (annee%100==0 and annee%400==0) or (not(annee%100==0) and annee%4==0)

def affiche(valeur):     #la valeur de scale est donnée à l'appel
    global mod7mois, nomjour
    jour=scale1.get()
    mois=scale2.get()
    offsetmois=mod7mois[mois-1]
    annee=scale3.get()
    diffannee=annee-1900
    moinsun=0;bistxt=''
    if bis(annee):
        if (mois==1 or mois==2):
            moinsun=-1;bistxt=' bissectile'
    correctif=(((annee//100)-20)//4)*-3-(annee//100)%4
    total=jour+offsetmois+diffannee+(diffannee//4)+correctif+moinsun
    total2=total % 7
    scale3.config(label='année'+bistxt+' :')
    #print(jour,offsetmois,annee,bis(annee),correctif,total,total2,nomjour[total2])
    v.set(nomjour[total2])

fenetre = Tk()

value1 = DoubleVar()
scale1 = Scale(fenetre, variable=value1, from_=1, to=31, orient='horizontal',command=affiche, label='jour :', activebackground='red', cursor='cross',troughcolor='blue')
scale1.pack()
value2 = DoubleVar()
scale2 = Scale(fenetre, variable=value2, from_=1, to=12, orient='horizontal',command=affiche, label='mois :', activebackground='red', cursor='exchange',troughcolor='green')
scale2.pack()
value3 = DoubleVar()
scale3 = Scale(fenetre, variable=value3, from_=1900, to=2050, orient='horizontal',command=affiche, label='année :', activebackground='red', cursor='heart',troughcolor='pink')
scale3.pack()
var = StringVar()
label = Label(fenetre, textvariable=var,pady=5)
var.set("Jour de la semaine")
label.pack()
v = StringVar()
v.set('lundi')
e = Entry(fenetre, textvariable=v, width=30, justify=CENTER)
e.pack(fill='both')
#e.place(x=100,y=100,height=100, width=100)

mainloop() 