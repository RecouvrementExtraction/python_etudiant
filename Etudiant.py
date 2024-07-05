from tkinter import *
from tkinter import ttk, messagebox
import pymysql
from pymysql import cursors





class Etudiant:
    def __init__(self, root) :
        self.root = root
        self.root.title("Inscription")
        self.root.geometry("1920x1080+0+0")
    

        #formulaire
        Gestion_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="cyan")
        Gestion_Frame.place(x=50, y=150, width=600, height=700)
        gestion_title = Label(Gestion_Frame, text="Information de l'Etudiant", font=("times new roman",30,"bold"), bg="cyan")
        gestion_title.place(x=50, y=50)
        
        
        #ID Etudiant
        idEtudiant = Label(Gestion_Frame, text="ID Etudiant", font=("times new roman",15), bg="cyan")
        idEtudiant.place(x=50, y=150)
        
        id_text = Entry(Gestion_Frame, font=("times new roman",15))
        id_text.place(x=220, y=150)
        
        #Nom Complet
        idnomcomplet = Label(Gestion_Frame, text="Nom Complet", font=("times new roman",15), bg="cyan")
        idnomcomplet.place(x=50, y=210)
        
        nom_text = Entry(Gestion_Frame, font=("times new roman",15))
        nom_text.place(x=220, y=210)
        
        #EMail Etudiant
        email_ = Label(Gestion_Frame, text="Email", font=("times new roman",15), bg="cyan")
        email_.place(x=50, y=270)
        
        email_text = Entry(Gestion_Frame, font=("times new roman",15))
        email_text.place(x=220, y=270)
        
        #sexe Etudiant
        sexe = Label(Gestion_Frame, text="sexe", font=("times new roman",15), bg="cyan")
        sexe.place(x=50, y=310)
        
        sexe_text = ttk.Combobox(Gestion_Frame, font=("times new roman",15), state="readonly")
        sexe_text["values"]=("Homme","Femme")
        sexe_text.place(x=220, y=310,width=205)
        sexe_text.current(0)
        
        #Contact Etudiant
        contact = Label(Gestion_Frame, text="Contact Etudiant", font=("times new roman",15), bg="cyan")
        contact.place(x=50, y=360)
        
        contact_text = Entry(Gestion_Frame, font=("times new roman",15))
        contact_text.place(x=220, y=360)
        
        #Date de naissance
        dateN = Label(Gestion_Frame, text="Date de naissance", font=("times new roman",15), bg="cyan")
        dateN.place(x=50, y=410)
        
        dateN_text = Entry(Gestion_Frame, font=("times new roman",15))
        dateN_text.place(x=220, y=410)
        
        #Adresse
        adresse = Label(Gestion_Frame, text="Adresse", font=("times new roman",15), bg="cyan")
        adresse.place(x=50, y=460)
        
        self.adresse_text = Text(Gestion_Frame, font=("times new roman",15))
        self.adresse_text.place(x=220, y=460, width=205, height=80)
        
        
        #Bouton Ajouter
        btn_ajouter = Button(Gestion_Frame, text="Ajouter", font=("times new roman",15), bd=5, relief=GROOVE, bg="green")
        btn_ajouter.place(x=10, y=600, width=100)
        
        #Bouton modifier
        btn_modifier = Button(Gestion_Frame, text="Modifier", font=("times new roman",15), bd=5, relief=GROOVE, bg="yellow")
        btn_modifier.place(x=150, y=600, width=100)
        
        #Bouton supprimer
        btn_supprimer = Button(Gestion_Frame, text="Supprimer", font=("times new roman",15), bd=5, relief=GROOVE, bg="red")
        btn_supprimer.place(x=300, y=600, width=100)
        
        #Bouton reinitialiser
        btn_reinitialiser = Button(Gestion_Frame, text="Reinitialiser", font=("times new roman",15), bd=5, relief=GROOVE, bg="gray")
        btn_reinitialiser.place(x=450, y=600, width=120)






root = Tk()
obj = Etudiant(root)
root.mainloop()