import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def login():
    # Replace this function with your actual login implementation
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Success", "Welcome to the Bitcoin App!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main application window
app = tk.Tk()
app.title("Bitcoin App")
app.geometry("550x350")  # Increased width and height

# Load and resize the icon
icon_path = "bitcoin.png"
icon = Image.open(icon_path)
icon = icon.resize((150, 150), Image.BICUBIC)
icon = ImageTk.PhotoImage(icon)
app.iconphoto(True, icon)

# Welcome message with the icon
welcome_label = tk.Label(app, text="Welcome to the Bitcoin App!", font=("Helvetica", 18))
welcome_label.pack(pady=5)
icon_label = tk.Label(app, image=icon)
icon_label.pack(pady=5)

# Username and password entry
username_label = tk.Label(app, text="Username:")
username_label.pack()
username_entry = tk.Entry(app)
username_entry.pack()

password_label = tk.Label(app, text="Password:")
password_label.pack()
password_entry = tk.Entry(app, show="*")
password_entry.pack()

# Login button
login_button = tk.Button(app, text="Login", command=login)
login_button.pack(pady=10)

# Run the main event loop
app.mainloop()
