from tkinter import *
from tkinter import ttk, messagebox
import pymysql
from pymysql import cursors





class Etudiant:
    def __init__(self, root) :
        self.root = root
        self.root.title("Ajout Etudiant")
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
        
        
        #affichage 
        Details_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="cyan")
        Details_Frame.place(x=700, y=150, width=1100, height=700)
        
        Affiche_resulta = Label(Details_Frame, text="Recherche par", font=("times new roman", 30,"bold"), bg="cyan")
        Affiche_resulta.place(x=50, y=50)
        
        rech = ttk.Combobox(Details_Frame, font=("times new roman",20), state="readonly")
        rech["values"]=("nom","contact")
        rech.place(x=350, y=55, width=180, height=30)
        
        rech_txt = Entry(Details_Frame, font=("times new roman", 20), bd=5, relief=GROOVE)
        rech_txt.place(x=550,y=55, width=250, height=30)
        
        btn_rech = Button(Details_Frame, text="Rechercher", font=("times new roman",15), bd=10, bg="gray", relief=GROOVE)
        btn_rech.place(x=810, y=55, width=120, height=35)
        
        btn_afftou = Button(Details_Frame, text="Afficher Tous", font=("times new roman",15), bd=10, bg="gray", relief=GROOVE)
        btn_afftou.place(x=940, y=55, width=135, height=35)
        
        #Affichage
        result_Fram = Frame (Details_Frame, bd=5, relief=GROOVE, bg="cyan")
        result_Fram.place(x=10, y=110, width=1070, height=570)
        
        scroll_x = Scrollbar(result_Fram, orient=HORIZONTAL)
        scroll_y = Scrollbar(result_Fram, orient=VERTICAL)
        self.tabl_resul = ttk.Treeview(result_Fram, columns=("id","nom", "mail", "sexe", "contact", "dat","adresse"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        self.tabl_resul.heading("id", text="ID Etudiant")
        self.tabl_resul.heading("nom", text="Nom")
        self.tabl_resul.heading("mail", text="Mail")
        self.tabl_resul.heading("sexe", text="Sexe")
        self.tabl_resul.heading("contact", text="Contact")
        self.tabl_resul.heading("dat", text="Date Naissance")
        self.tabl_resul.heading("adresse", text="Adresse")
        
        
        self.tabl_resul["show"]="headings"
        
        self.tabl_resul.column("id", width = 100)
        self.tabl_resul.column("nom", width=150)
        self.tabl_resul.column("mail", width=150)
        self.tabl_resul.column("sexe", width=150)
        self.tabl_resul.column("contact", width=150)
        self.tabl_resul.column("dat", width=150)
        self.tabl_resul.column("adresse", width=200)
        
        self.tabl_resul.pack()
        
        self.tabl_resul.bind("<ButtonRelease-1")
        

    





root = Tk()
obj = Etudiant(root)
root.mainloop()