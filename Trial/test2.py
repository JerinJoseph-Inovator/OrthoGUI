import tkinter as tk
from PIL import Image, ImageTk

def main():
    root = tk.Tk()
    root.title("Orthovision Login")

    # ----------------------------------------
    # Variables for coordinate offsets
    # ----------------------------------------
    a = 100
    b = 150

    # 1) LOAD THE BACKGROUND IMAGE
    bg_image = Image.open("bg_image01.jpg")
    w, h = bg_image.size
    # Make window match image size
    root.geometry(f"{w}x{h}")

    # Convert to PhotoImage
    bg_photo = ImageTk.PhotoImage(bg_image)

    # 2) CREATE A LABEL FOR THE BACKGROUND
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # 3) PLACE YOUR WIDGETS (LABELS, ENTRIES, BUTTONS) ON TOP
    #    Using x = a + (orig_x - 100), y = b + (orig_y - 100)

    # Title label
    title_label = tk.Label(
        root, text="Orthovision",
        font=("Arial", 30), fg="steelblue", bg="white"
    )
    # original x=600, y=30 => x = a + (600-100), y = b + (30-100)
    title_label.place(x=a + (600 - 100), y=b + (30 - 100))

    # Doctor / Patient buttons
    doctor_btn = tk.Button(
        root, text="Doctor",
        font=("Arial", 12), bg="navy", fg="white", width=8
    )
    # original x=600, y=70 => x = a + (600-100), y = b + (70-100)
    doctor_btn.place(x=a + (600 - 100), y=b + (70 - 100))

    patient_btn = tk.Button(
        root, text="Patient",
        font=("Arial", 12), bg="navy", fg="white", width=8
    )
    # original x=700, y=70 => x = a + (700-100), y = b + (70-100)
    patient_btn.place(x=a + (700 - 100), y=b + (70 - 100))

    # Email
    email_label = tk.Label(
        root, text="Email",
        font=("Arial", 12), bg="white"
    )
    # original x=600, y=120 => x = a + (600-100), y = b + (120-100)
    email_label.place(x=a + (600 - 100), y=b + (120 - 100))

    email_entry = tk.Entry(
        root, font=("Arial", 12), width=25, bd=2
    )
    # original x=600, y=145 => x = a + (600-100), y = b + (145-100)
    email_entry.place(x=a + (600 - 100), y=b + (145 - 100))

    # Password
    password_label = tk.Label(
        root, text="Password",
        font=("Arial", 12), bg="white"
    )
    # original x=600, y=185 => x = a + (600-100), y = b + (185-100)
    password_label.place(x=a + (600 - 100), y=b + (185 - 100))

    password_entry = tk.Entry(
        root, font=("Arial", 12), width=25, show="*", bd=2
    )
    # original x=600, y=210 => x = a + (600-100), y = b + (210-100)
    password_entry.place(x=a + (600 - 100), y=b + (210 - 100))

    # Login button
    login_btn = tk.Button(
        root, text="Login",
        font=("Arial", 12), bg="navy", fg="white", width=10
    )
    # original x=650, y=260 => x = a + (650-100), y = b + (260-100)
    login_btn.place(x=a + (650 - 100), y=b + (260 - 100))

    # Processing data
    processing_label = tk.Label(
        root, text="Processing data...",
        font=("Arial", 10), fg="steelblue", bg="white"
    )
    # original x=600, y=320 => x = a + (600-100), y = b + (320-100)
    processing_label.place(x=a + (600 - 100), y=b + (320 - 100))

    root.mainloop()

if __name__ == "__main__":
    main()
