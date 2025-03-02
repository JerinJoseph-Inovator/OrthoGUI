import tkinter as tk
from PIL import Image, ImageTk

def on_login():
    """
    Handle login logic here.
    For now, it just prints a message.
    """
    print("Login button clicked")

def main():
    # Create the main application window
    root = tk.Tk()
    root.title("Orthovision")
    root.geometry("1280x890")  # Set a default window size (width x height)

    # Load the background image
    # Make sure you have "background.jpg" in the same folder or provide a full path
    bg_image = Image.open("bg_image01.jpg")
    # Optionally, resize the image to fit your window size if needed:
    # bg_image = bg_image.resize((600, 400), Image.ANTIALIAS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a label to display the background image
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create a frame for the foreground content (login elements)
    # We use a semi-transparent color by layering an RGBA image or using a solid color.
    # If you want real transparency, consider a separate label with partial alpha or just a light color.
    login_frame = tk.Frame(root, bg="white", padx=20, pady=20)
    login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Title label
    title_label = tk.Label(login_frame, text="Orthovision", font=("Arial", 18, "bold"), bg="white")
    title_label.pack(pady=10)

    # Doctor/Patient buttons
    btn_frame = tk.Frame(login_frame, bg="white")
    btn_frame.pack(pady=5)

    doctor_button = tk.Button(btn_frame, text="Doctor")
    doctor_button.pack(side=tk.LEFT, padx=5)

    patient_button = tk.Button(btn_frame, text="Patient")
    patient_button.pack(side=tk.LEFT, padx=5)

    # Email label and entry
    email_label = tk.Label(login_frame, text="Email", bg="white")
    email_label.pack(pady=(10, 0))
    email_entry = tk.Entry(login_frame)
    email_entry.pack()

    # Password label and entry
    password_label = tk.Label(login_frame, text="Password", bg="white")
    password_label.pack(pady=(10, 0))
    password_entry = tk.Entry(login_frame, show="*")
    password_entry.pack()

    # Login button
    login_button = tk.Button(login_frame, text="Login", command=on_login)
    login_button.pack(pady=10)

    # Optional "Processing data..." label in the corner
    processing_label = tk.Label(root, text="Processing data...", bg="black", fg="white")
    processing_label.place(x=20, y=20)

    root.mainloop()

if __name__ == "__main__":
    main()
