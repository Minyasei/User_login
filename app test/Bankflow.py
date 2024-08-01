import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import customtkinter

USER_FILE = "users.txt"

app = customtkinter.CTk()
app.title("BitFlow")
app.geometry("450x450")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
frame = customtkinter.CTkFrame(master = app)

#functions
def register_user(name, birthday, gender, username, password):
    with open(USER_FILE, mode='r') as file:
        for line in file:
            stored_username = line.strip().split(":")
            if stored_username == username:
                messagebox.showerror("Registration Failed", "Username already exists. Please choose a different username.", text_color="red")
                return False
#check
    with open(USER_FILE, mode='a') as file:
        file.write(f"{name}:{birthday}:{gender}:{username}:{password}\n")
    messagebox.showinfo("Registration Success", "User registered successfully!")
    return True

def login():
    username = username_entry.get()
    password = password_entry.get()

    with open("users.txt", mode='r') as file:
        for line in file:
            values = line.strip().split(':')
            stored_name = values[-5].capitalize()
            stored_username= values[-2]
            stored_password = values[-1]
            if stored_username == username and stored_password == password:
                messagebox.showinfo("Login Success", "Welcome to Bitflow :)")
                username_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                app.withdraw()
                open_main_menu(stored_name)
                return

    #failed
    messagebox.showerror("Login Failed", "Invalid username or password.")

def apply_dark_theme(widget):
    widget.configure(bg="black", fg="white")
def open_main_menu(name):
    global main_screen
    main_screen = tk.Toplevel(app)
    main_screen.title('Main Menu')
    main_screen.geometry('1280x800')
    main_screen.configure(bg='#EEE1FF')

    welcome_label =customtkinter.CTkLabel(main_screen, text=f"Welcome {name} \n\n" "Account Dashboard", text_color="black",font= ('Calibri', 12))
    welcome_label.pack()

def register():
    global register_screen


    register_screen = tk.Toplevel()
    register_screen.geometry("350x350")
    register_screen.title('Register')
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    #register labels
    customtkinter.CTkLabel(register_screen, text="  Please enter your details", text_color="black",font = ('Calibri',12)).grid(row=0, columnspan=2, sticky='w')

    customtkinter.CTkLabel(register_screen, text="  Name:", text_color="black",font = ('Calibri',12)).grid(row=2, columnspan=2, sticky='w')
    name_entry = customtkinter.CTkEntry(register_screen)
    name_entry.grid(row=2, columnspan=10, sticky='w', padx=100, pady=10)

    customtkinter.CTkLabel(register_screen, text="  Birthday:", text_color="black",font = ('Calibri',12)).grid(row=3, columnspan=2, sticky='w')
    bd_entry = DateEntry(register_screen, width=12, background='lightblue', foreground='white', date_pattern='mm/dd/yyyy')
    bd_entry.grid(row=3, columnspan=10, sticky='w', padx=100, pady=10)
    bd_entry.set_date(None)

    customtkinter.CTkLabel(register_screen, text="  Gender:", text_color="black",font = ('Calibri',12)).grid(row=4, columnspan=2, sticky='w')

    def submit():
        name = name_entry.get()
        birthday = bd_entry.get()
        gender = gender_var.get()
        username = username_entry.get()
        password = password_entry.get()

        notif = customtkinter.CTkLabel(register_screen, font=('Calibri', 12))
        notif.grid(row=8, columnspan=2, sticky='w', pady=5)

        if name == "" or birthday =="" or gender == "" or username == "" or password =="":
            notif.configure(text ="                               *Fill all fields to register", text_color='red')
            return

        with open(USER_FILE, mode='r') as file:
            for line in file:
                if ":" in line:
                    values = line.strip().split(':')
                    stored_username, stored_password = values[-2], values[-1]

                    if stored_username == username:
                        notif.configure(text="\n                                Account already exists.\n                                Choose a different username.", text_color="red")
                        return

        registration_successful = register_user(name, birthday, gender, username, password)

        #close registration
        if registration_successful:
            notif.configure(fg="green", text="                 Registration successful!")
            register_screen.after(1500, register_screen.destroy)

    submit_button = customtkinter.CTkButton(register_screen, text="Submit", command=submit)
    submit_button.grid(row=7, columnspan=10, sticky='w', padx=100)

    #options
    gender_var=tk.StringVar()
    gender_var.set("Other") #default

    tk.Radiobutton(register_screen, text="Female", font=('Calibri', 10), variable = gender_var, value= "F").grid(row=4, column=1, sticky='w',padx= 220, pady=10)
    tk.Radiobutton(register_screen, text="Male", font=('Calibri', 10), variable = gender_var, value= "M").grid(row=4, column=1, sticky='w',padx= 160, pady=10)
    tk.Radiobutton(register_screen, text="Other", font=('Calibri', 10), variable = gender_var, value= "-").grid(row=4, column=1, sticky='w', padx=100, pady=10)

    customtkinter.CTkLabel(register_screen, text="  Username:", text_color="black",font=('Calibri', 12)).grid(row=5, columnspan=2, sticky='w')
    username_entry = customtkinter.CTkEntry(register_screen)
    username_entry.grid(row=5, columnspan=10, sticky='w', padx=100, pady=10)

    customtkinter.CTkLabel(register_screen, text="  Password:", text_color="black",font = ('Calibri',12)).grid(row=6, columnspan=2, sticky='w')
    password_entry = customtkinter.CTkEntry(register_screen, show="*")
    password_entry.grid(row=6, columnspan=10, sticky='w', padx=100,pady=10)

# Load resize icon
icon_path = "bitvault_rev.png"
icon = Image.open(icon_path)
icon = icon.resize((150, 150), Image.BICUBIC)
icon = ImageTk.PhotoImage(icon)
app.iconphoto(True, icon)

# Welcome
welcome_label = customtkinter.CTkLabel(app, text="Welcome to the BitFlow!", font=("Helvetica", 18), text_color="#F9B52C")
welcome_label.pack(pady=5)
second_label = customtkinter.CTkLabel(app, text="Easy way to track", font=("Calibri",14), text_color="#2CF9C3")
second_label.pack()
icon_label = tk.Label(app, image=icon, bg="#242424")
icon_label.pack()

username_label = customtkinter.CTkLabel(app, text="Username:")
username_label.pack()
username_entry = customtkinter.CTkEntry(app)
username_entry.pack(pady=5)

password_label = customtkinter.CTkLabel(app, text="Password:")
password_label.pack()
password_entry = customtkinter.CTkEntry(app, show="*")
password_entry.pack(pady=5)

login_button = customtkinter.CTkButton(app, text="Login", command=login)
login_button.pack(pady=10)

register_button = customtkinter.CTkButton(app, text="Register", command=register)
register_button.pack(pady=0)

app.mainloop()
