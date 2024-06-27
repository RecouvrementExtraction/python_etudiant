from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import *
import pymysql
import os


class Formulaire:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulaire")
        self.root.geometry("1920x1080+0+0")

        # champs du formulaire
        frame1 = Frame(self.root, bg="gray")
        frame1.place(x=600, y=200, width=700, height=500)
        
        title = Label(frame1, text="Créer un compte", font=("algerian", 20, "bold"), bg="grey", fg="orange").place(x=50, y=30)
        
        #nom et prenom
        aff_prenom = Label(frame1, text="Prenom", font=("times new roman",15,"bold"),bg="grey", fg="black").place(x=50, y=100)
        self.ecrit_prenom = Entry(frame1, font=("algerian"), bg="white")
        self.ecrit_prenom.place(x=50, y=130, width=250)

        aff_nom = Label(frame1, text="Nom", font=("times new roman",15,"bold"),bg="grey", fg="black").place(x=370, y=100)
        self.ecrit_nom = Entry(frame1, font=("algerian"), bg="white")
        self.ecrit_nom.place(x=370, y=130, width=250)
        
        
        #telphone et email
        aff_telephone = Label(frame1, text="Telephone", font=("times new roman",15,"bold"),bg="grey", fg="black").place(x=50, y=160)
        self.ecrit_telephone = Entry(frame1, font=("algerian"), bg="white")
        self.ecrit_telephone.place(x=50, y=190, width=250)

        aff_email = Label(frame1, text="Email", font=("times new roman",15,"bold"),bg="grey", fg="black").place(x=370, y=160)
        self.ecrit_email = Entry(frame1, font=("algerian"), bg="white")
        self.ecrit_email.place(x=370, y=190, width=250)


root = Tk()
obj = Formulaire(root)
root.mainloop()
