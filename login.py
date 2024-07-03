from tkinter import *
from tkinter import ttk, messagebox
import pymysql


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Connexion")
        self.root.geometry("1500x780+250+025")
        self.root.config(bg="white")
        self.root.focus_force()
        
        
        login_fram = Frame(self.root, bg="cyan")
        login_fram.place(x=500, y=130, width=500, height=500)
        
        
        title = Label(login_fram, text="Portail AKG", font=("algerian",40,"bold"), bg="cyan",fg="black")
        title.pack(side=TOP, fill=X)
        
        
        lbl_email = Label(login_fram, text="Email", font=("times new roman",30,"bold"), bg="cyan").place(x=150, y=100, width=200)
        lbl_password = Label(login_fram, text="Password", font=("times new roman",30,"bold"), bg="cyan").place(x=150, y=200, width=200)
        
        
        self.txt_email = Entry(login_fram, font=("times new roman",20), bg="lightgray")
        self.txt_email.place(x=100, y=160, width=320)
        
        
        self.txt_password = Entry(login_fram, font=("times new roman",20),show="*", bg="lightgray")
        self.txt_password.place(x=100, y=270, width=320)
        
        creer_btn = Button(login_fram, text="Créer un nouveau compte", cursor="hand2", font=("times new roman",15),bd=0, bg="cyan", fg="green").place(x=30, y=320)
        
        oubli_btn = Button(login_fram, text="mot de passe oublié", cursor="hand2", font=("times new roman",15),bd=0, bg="cyan", fg="red", command=self.password_oublie_fenetre).place(x=300, y=320)
        
        connect_btn = Button(login_fram, text="Connexion", cursor="hand2", font=("times new roman",15),bd=0, bg="lightgray", fg="blue", command=self.connexion).place(x=200, y=450)
        
        
        
    def connexion(self):
        if self.txt_email.get() == "" or self.txt_password.get() == "":
            messagebox.showerror("Erreur", "Veuillez saisir l'email et le mot de passe", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", passwd="", database="python_etudiant")
                cur = con.cursor()
                cur.execute("SELECT * FROM compte WHERE email=%s and password=%s", (self.txt_email.get(), self.txt_password.get()))
                row = cur.fetchone()

                if row is None:
                    messagebox.showerror("Erreur", "Email ou mot de passe invalide", parent=self.root)
                else:
                    messagebox.showinfo("Succès", "Bien Bonjour", parent=self.root)

            except pymysql.MySQLError as ex:
                messagebox.showerror("Erreur", f"Erreur de connexion : {str(ex)}", parent=self.root)
            finally:
                if con:
                    con.close()

        
        
        
    def password_oublie_fenetre(self):
        if self.txt_email.get() == "":
            messagebox.showerror("Erreur","veuillez renseigner votre Email", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", passwd="", database="python_etudiant")
                cur = con.cursor()
                cur.execute("SELECT * FROM compte WHERE email=%s", (self.txt_email.get(),))
                row = cur.fetchone()

                if row is None:
                    messagebox.showerror("Erreur", "Cet email n'existe pas", parent=self.root)
                else:
                    self.root2 = Toplevel()
                    self.root2.title("Mot de passe oublié")
                    self.root2.geometry("400x400+800+500")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    title = Label(self.root2, text="Mot de passe oublié", font=("times new roman", 20, "bold"), bg="red", fg="black")
                    title.pack(side=TOP, fill=X)

                    # Question
                    aff_question = Label(self.root2, text="Séléctionnez une question", font=("times new roman", 15, "bold"), bg="white", fg="black")
                    aff_question.place(x=70, y=50)
                    self.ecrit_question = ttk.Combobox(self.root2, font=("times new roman", 15), state="readonly")
                    self.ecrit_question["values"] = ("Select", "Ton surnom", "Lieu de naissance", "Meilleur ami", "Film préféré")
                    self.ecrit_question.place(x=70, y=100, width=250)
                    self.ecrit_question.current(0)

                    # Réponses
                    aff_repondre = Label(self.root2, text="Répondre", font=("times new roman", 15, "bold"), bg="white", fg="black")
                    aff_repondre.place(x=70, y=150)
                    self.ecrit_repondre = Entry(self.root2, font=("times new roman", 15), bg="white")
                    self.ecrit_repondre.place(x=70, y=200, width=250)

                    # Changer mot de passe
                    aff_nouvpass = Label(self.root2, text="Nouveau mot de passe", font=("times new roman", 15, "bold"), bg="white", fg="black")
                    aff_nouvpass.place(x=70, y=250)
                    self.ecrit_nouvpass = Entry(self.root2,show="*", font=("times new roman", 15), bg="white")
                    self.ecrit_nouvpass.place(x=70, y=300, width=250)

                    # Bouton changer mot de passe
                    changer_btn = Button(self.root2, text="Modifier", cursor="hand2", font=("times new roman", 15, "bold"), bg="lightgray", fg="green", command=self.passwd_oublie)
                    changer_btn.place(x=160, y=350)

            except Exception as ex:
                messagebox.showerror("Erreur", f"Erreur de connexion : {str(ex)}", parent=self.root)

        
            finally:
                if con:
                    con.close()
        
    
    


    def passwd_oublie(self):
        if self.ecrit_question.get()=="" or self.ecrit_repondre.get()=="" or self.ecrit_nouvpass.get()=="":
            messagebox.showerror("Erreur","Remplir tous les champs", parent=self.root2)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", passwd="", database="python_etudiant")
                cur = con.cursor()
                cur.execute("SELECT * FROM compte WHERE email=%s and question=%s and reponse=%s", (self.txt_email.get(), self.ecrit_question.get(), self.ecrit_repondre.get()))
                row = cur.fetchone()
                
                if row is None:
                    messagebox.showerror("Erreur", "vous n'avez pas reondu a la question séléctionnée", parent=self.root2)
                else:
                     cur.execute("UPDATE compte set  password=%s where email=%s", (self.ecrit_nouvpass.get(),self.txt_email.get(),))
                     con.commit()
                     messagebox.showinfo("Succès", "mot de passe modifié", parent=self.root2)
                
            except Exception as es:
                 messagebox.showerror("Erreur", f"Erreur de connexion : {str(es)}", parent=self.root)
                 
            finally:
                if con:
                    con.close()
                 
                 
            









root = Tk()
obj = Login(root)
root.mainloop()