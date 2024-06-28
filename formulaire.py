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
        title = Label(frame1, text="Créer un compte pour AKG-Family", font=("algerian", 20, "bold"), bg="grey", fg="orange").place(x=90, y=30)
        
        
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
        
        
        #questions reponses
        aff_question = Label(frame1, text="Séléctionnez une question", font=("times new roman",15,"bold"),bg="grey", fg="black").place(x=50, y=220)
        self.ecrit_question =ttk.Combobox(frame1, font=("times new roman", 15), state="readonly")
        self.ecrit_question["values"] = ("Select","Ton surnom", "Lieu de naissance", "Meilleur ami", "Film préféré")
        self.ecrit_question.place(x=50, y=250, width=250)
        self.ecrit_question.current(0)

    
        aff_repondre = Label(frame1, text="Répondre", font=("times new roman",15,"bold"),bg="grey", fg="black").place(x=370, y=220)
        self.ecrit_repondre = Entry(frame1, font=("algerian"), bg="white")
        self.ecrit_repondre.place(x=370, y=250, width=250)


        #password & confirme password
        aff_password = Label(frame1, text="Password", font=("arial",15,"bold"),bg="grey", fg="black").place(x=50, y=280)
        self.ecrit_password = Entry(frame1,show="*", font=("algerian"), bg="white")
        self.ecrit_password.place(x=50, y=310, width=250)

        aff_confPassword = Label(frame1, text="Confirme Password", font=("arial",15,"bold"),bg="grey", fg="black").place(x=370, y=280)
        self.ecrit_confPassword = Entry(frame1,show="*", font=("algerian"), bg="white")
        self.ecrit_confPassword.place(x=370, y=310, width=250)


        #accepter les termes et conditions
        self.var_check = IntVar()
        chk = Checkbutton(frame1, text="J'accepte les termes et les conditions", font=("times new roman",12),bg="grey", variable=self.var_check, onvalue=1, offvalue=0, cursor="hand2").place(x=50,y=350)


        #boutons de validation de connexion
        btn1 = Button(frame1, text="Créer",font=("times new roman",15,"bold"), bg="cyan", fg="black",cursor="hand2", command=self.creer).place(x=250, y=430, width=250)
        
        btn2 = Button(frame1, text="Connexion",font=("times new roman",15,"bold"), bg="cyan", fg="black",cursor="hand2").place(x=550, y=60, width=140)



    def creer(self):
        if (self.ecrit_prenom.get() == "" or 
            self.ecrit_nom.get() == "" or 
            self.ecrit_email.get() == "" or 
            self.ecrit_question.get() == "" or 
            self.ecrit_repondre.get() == "" or 
            self.ecrit_telephone.get() == "" or 
            self.ecrit_password.get() == "" or 
            self.ecrit_confPassword.get() == ""):
            messagebox.showerror("Ne m'énerve pas", "Rempli tous les champs", parent=self.root)
        elif self.ecrit_password.get() != self.ecrit_confPassword.get():
            messagebox.showerror("Erreur", "Les mots de passe ne sont pas identiques", parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Important", "Veuillez accepter les termes et conditions", parent=self.root)
            
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", passwd="", database="python_etudiant")
                cur = con.cursor()
                cur.execute("SELECT * FROM compte WHERE email=%s", (self.ecrit_email.get(),))
                row = cur.fetchone()

                if row is not None:
                    messagebox.showerror("Erreur", "Cet email est déjà utilisé", parent=self.root)
                else:
                    cur.execute(
                        "INSERT INTO compte (prenom, nom, telephone, email, question, reponse, password) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (
                            self.ecrit_prenom.get(),
                            self.ecrit_nom.get(),
                            self.ecrit_telephone.get(),
                            self.ecrit_email.get(),
                            self.ecrit_question.get(),
                            self.ecrit_repondre.get(),
                            self.ecrit_password.get()
                        )
                    )
                    con.commit()
                    messagebox.showinfo("Succès", "Votre compte a été créé", parent=self.root)
                    self.reini()

            except Exception as es:
                messagebox.showerror("Erreur", f"Erreur lors de la connexion: {str(es)}", parent=self.root)

            finally:
                if con:
                    con.close()



    def reini(selfe):
        selfe.ecrit_prenom.delete(0, END)
        selfe.ecrit_nom.delete(0, END)
        selfe.ecrit_telephone.delete(0, END)
        selfe.ecrit_email.delete(0, END)
        selfe.ecrit_question.delete(0, END)
        selfe.ecrit_repondre.delete(0, END)
        selfe.ecrit_password.delete(0, END)
        selfe.var_check.set(0)









root = Tk()
obj = Formulaire(root)
root.mainloop()
