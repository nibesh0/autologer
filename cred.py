import os
from enc import enc
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

key_folder = "key"

if not os.path.exists(key_folder):
    os.makedirs(key_folder)

def store_credentials():
    Uid = uid_entry.get()
    passwd = passwd_entry.get()

    if not Uid or not passwd:
        messagebox.showerror("Error", "Uid and Password fields cannot be blank.")
        return

    confirmation_text = f"Your ID: {Uid}\nYour Password: {passwd}\n\nDo you want to proceed?"
    confirmation = messagebox.askquestion("Confirmation", confirmation_text)
    
    if confirmation == "yes":
        key_filename = os.path.join(key_folder, "encryption_key.key")
        filename = os.path.join(key_folder, "credentials.enc")
        key = enc.generate_key()
        enc.store_key(key_filename, key)

        enc.store_credentials(filename, key_filename, Uid, passwd)

        retrieved_username, retrieved_password = enc.retrieve_credentials(filename, key_filename)

        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Credentials stored securely.\n")
        output_text.insert(tk.END, f"Retrieved Username: {retrieved_username}\n")
        output_text.insert(tk.END, f"Retrieved Password: {retrieved_password}\n")
        output_text.config(state=tk.DISABLED)

        root.unbind("<Return>")
        submit_button.pack_forget()

        exit_button = tk.Button(root, text="Exit", command=root.quit)
        exit_button.pack()
    else:
        passwd_entry.delete(0, "end")

root = tk.Tk()
root.title("AutoLoger")
root.configure(bg="black")
try:
    image_path = r"res\image.jpeg"
    img = Image.open(image_path)
    img = img.resize((200, 150))
    photo = ImageTk.PhotoImage(img)
except:
    print("err")
    photo = None




image_label = tk.Label(root, image=photo, bg="black")
image_label.pack()

label_text_color = "white"

uid_label = tk.Label(root, text="Uid:", fg=label_text_color, bg="black")
uid_label.pack()
uid_entry = tk.Entry(root, bg=label_text_color)
uid_entry.pack()

passwd_label = tk.Label(root, text="Password:", fg=label_text_color, bg="black")
passwd_label.pack()
passwd_entry = tk.Entry(root, show="*", bg=label_text_color)
passwd_entry.pack()

submit_button = tk.Button(root, text="Submit", command=store_credentials, bg=label_text_color)
submit_button.pack()

output_text = tk.Text(root, height=10, width=40, state=tk.DISABLED, bg="black", fg="white")
output_text.pack()

def on_enter_key(event):
    store_credentials()

root.bind("<Return>", on_enter_key)

root.mainloop()
