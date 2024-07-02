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
        
        
        title = Label(login_fram, text="Connexion", font=("algerian",40,"bold"), bg="cyan",fg="black")
        title.pack(side=TOP, fill=X)
        
        
        lbl_email = Label(login_fram, text="Email", font=("times new roman",30,"bold"), bg="cyan").place(x=150, y=100, width=200)
        lbl_password = Label(login_fram, text="Password", font=("times new roman",30,"bold"), bg="cyan").place(x=150, y=200, width=200)
        
        
        self.txt_email = Entry(login_fram, font=("times new roman",20), bg="lightgray")
        self.txt_email.place(x=100, y=160, width=320)
        
        
        self.txt_password = Entry(login_fram, font=("times new roman",20),show="*", bg="lightgray")
        self.txt_password.place(x=100, y=270, width=320)
        
        creer_btn = Button(login_fram, text="Créer un nouveau compte", cursor="hand2", font=("times new roman",15),bd=0, bg="cyan", fg="green").place(x=30, y=320)
        
        oubli_btn = Button(login_fram, text="mot de passe oublié", cursor="hand2", font=("times new roman",15),bd=0, bg="cyan", fg="red").place(x=300, y=320)
        
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

        
        
        
        
        
            
        
    
    
    
root = Tk()
obj = Login(root)
root.mainloop()