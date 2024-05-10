import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

qr = ""
img = ""


def text_to_qr_generator(text):
    qr_code = qrcode.QRCode(
        version=3,  # Range from 1 to 40
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr_code.add_data(text)
    qr_code.make(fit=True)

    qrimg = qr_code.make_image(fill_color="black", back_color="white")
    qrimg.save("QRCode.png")


def qr_generator():
    text = user_input.get()
    if text != "":
        text_to_qr_generator(text)
        print("Text is {}".format(text))
        global qr, img
        qr = Image.open("QRCode.png")
        img = ImageTk.PhotoImage(qr)
    else:
        messagebox.showwarning("Warning", "All Fields are Required!!!")

    show_code()


def show_code():
    img_lbl.config(image=img)
    output.config(text="QR code of " + user_input.get())


master = tk.Tk()
master.geometry("800x800")
master.title("QR Generator")

lbl = tk.Label(master, text="Enter message or URL")
lbl.pack(pady=10)
user_input = tk.StringVar()
entry = tk.Entry(master, textvariable=user_input)
entry.pack(pady=10)

qrButton = tk.Button(master, text="Generate QR", width=15, command=qr_generator)
qrButton.pack(pady=10)

quitButton = tk.Button(master, text="Quit", width=15, command=master.quit)
quitButton.pack(pady=10)

img_lbl = tk.Label(master, image="")
img_lbl.pack()
output = tk.Label(master, text="")
output.pack()

tk.mainloop()
