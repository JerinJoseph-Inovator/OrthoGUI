import tkinter as tk
from tkinter import Entry, Button, Label
from PIL import Image, ImageTk

# Create main window
root = tk.Tk()
root.title("Orthovision Login")
root.geometry("600x400")
root.configure(bg='white')

# Load and display background image
bg_image = Image.open("bg_image01.jpg")
bg_image = bg_image.resize((200, 300))  # Resize to fit
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(root, image=bg_photo, bg="white")
bg_label.place(x=50, y=50)

# Title label
title_label = Label(root, text="Orthovision", font=("Arial", 20), fg="steelblue", bg="white")
title_label.place(x=250, y=20)

# Role selection buttons
doctor_btn = Button(root, text="Doctor", font=("Arial", 12), bg="navy", fg="white", width=8)
doctor_btn.place(x=250, y=60)

patient_btn = Button(root, text="Patient", font=("Arial", 12), bg="navy", fg="white", width=8)
patient_btn.place(x=350, y=60)

# Email field
email_label = Label(root, text="Email", font=("Arial", 12), bg="white")
email_label.place(x=250, y=110)
email_entry = Entry(root, font=("Arial", 12), width=25, bd=2)
email_entry.place(x=250, y=135)

# Password field
password_label = Label(root, text="Password", font=("Arial", 12), bg="white")
password_label.place(x=250, y=170)
password_entry = Entry(root, font=("Arial", 12), width=25, show="*", bd=2)
password_entry.place(x=250, y=195)

# Login button
login_btn = Button(root, text="Login", font=("Arial", 12), bg="navy", fg="white", width=10)
login_btn.place(x=300, y=240)

# Processing text
processing_label = Label(root, text="Processing data...", font=("Arial", 10), fg="steelblue", bg="white")
processing_label.place(x=250, y=280)

root.mainloop()

