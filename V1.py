import customtkinter as ctk

class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Blindtest Musical")
        self.geometry("500x550")
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.current_window = None
        self.show_login()
    
    def show_login(self):
        if self.current_window:
            self.current_window.destroy()
        self.current_window = LoginWindow(self)
    
    def show_register(self):
        if self.current_window:
            self.current_window.destroy()
        self.current_window = RegisterWindow(self)

class LoginWindow(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=ctk.BOTH, expand=True)

        self.label = ctk.CTkLabel(self, text="Connexion au Blindtest Musical", font=("Arial", 20))
        self.label.pack(pady=20)

        self.username_entry = ctk.CTkEntry(self, placeholder_text="Nom d'utilisateur")
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Mot de passe", show="*")
        self.password_entry.pack(pady=10)

        self.login_button = ctk.CTkButton(self, text="Se connecter", command=self.login)
        self.login_button.pack(pady=10)

        self.register_button = ctk.CTkButton(self, text="S'inscrire", command=self.master.show_register)
        self.register_button.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(f"Tentative de connexion : {username}")

class RegisterWindow(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=ctk.BOTH, expand=True)

        self.label = ctk.CTkLabel(self, text="Inscription au Blindtest Musical", font=("Arial", 20))
        self.label.pack(pady=20)

        self.firstname_entry = ctk.CTkEntry(self, placeholder_text="Prénom")
        self.firstname_entry.pack(pady=10)

        self.lastname_entry = ctk.CTkEntry(self, placeholder_text="Nom")
        self.lastname_entry.pack(pady=10)

        self.username_entry = ctk.CTkEntry(self, placeholder_text="Nom d'utilisateur")
        self.username_entry.pack(pady=10)

        self.email_entry = ctk.CTkEntry(self, placeholder_text="Adresse Mail")
        self.email_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Mot de passe", show="*")
        self.password_entry.pack(pady=10)

        self.confirm_password_entry = ctk.CTkEntry(self, placeholder_text="Confirmer Mot de passe", show="*")
        self.confirm_password_entry.pack(pady=10)

        self.register_button = ctk.CTkButton(self, text="S'inscrire", command=self.register)
        self.register_button.pack(pady=20)

        self.login_link = ctk.CTkButton(self, text="Déjà inscrit ? Se connecter", command=self.master.show_login)
        self.login_link.pack(pady=10)

    def register(self):
        firstname = self.firstname_entry.get()
        lastname = self.lastname_entry.get()
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password != confirm_password:
            print("Les mots de passe ne correspondent pas")
        else:
            print(f"Tentative d'inscription pour : {username}")

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()