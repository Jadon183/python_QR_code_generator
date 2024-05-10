import json
import tkinter as tk
from functools import partial
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk

img = ""
photoFileName = ""
resumeFileName = ""


def text_to_qr_generator(data):
    qr = qrcode.QRCode(
        version=2,  # Range from 1 to 40
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qrimg = qr.make_image(fill_color="black", back_color="white")
    qrimg.save("QRCode.png")


def qr_generator():
    data = {
        "Full name": full_name_input.get(),
        "Email ID": email_input.get(),
        "Mobile Number": mob_number_input.get(),
        "Organization": organization_input.get(),
        "Photo File Name": photoFileName,
        "Resume File Name": resumeFileName
    }
    if data["Full name"] == "" or data["Email ID"] == "" or data["Mobile Number"] == "" or \
            data["Organization"] == "" or data["Photo File Name"] == "" or data["Resume File Name"] == "":
        output.config(text="")
        img_lbl.config(image="")
        messagebox.showwarning("Warning", "{} Fields are Required!!!".format(
            ",".join([x for x in data if data[x] == ""])))
    else:
        text_to_qr_generator(data)
        data = json.dumps(data)
        print("Data is {}".format(data))
        qr_img = Image.open("QRCode.png")
        global img
        img = ImageTk.PhotoImage(qr_img)
        show_code()


def show_code():
    output.config(text="QR code Generated")
    img_lbl.config(image=img)


def browse_files(file_type):
    if file_type == "Photo":
        global photoFileName
        photoFileName = filedialog.askopenfilename(initialdir="/",
                                                   title="Select a File", filetypes=(("Image Files", "*.*"),
                                                                                     ))
        if photoFileName != "":
            photoButton.configure(text="Replace Photo")

    elif file_type == "Resume":
        global resumeFileName
        resumeFileName = filedialog.askopenfilename(initialdir="/",
                                                    title="Select a File", filetypes=(("All Files", "*.*"),
                                                                                      ))
        if resumeFileName != "":
            resumeButton.configure(text="Replace Resume")


master = tk.Tk()
master.geometry("500x500")
master.title("QR Generator")
master.configure(bg="#40E0D0")

frame1 = tk.Frame(master)
frame1.pack(pady=10)

tk.Label(frame1, text="Full name").grid(row=0, column=1)
full_name_input = tk.StringVar()
tk.Entry(frame1, textvariable=full_name_input).grid(row=0, column=2)

tk.Label(frame1, text="Email ID").grid(row=0, column=3)
email_input = tk.StringVar()
tk.Entry(frame1, textvariable=email_input).grid(row=0, column=4)

tk.Label(frame1, text="Mobile Number").grid(row=1, column=1)
mob_number_input = tk.StringVar()
tk.Entry(frame1, textvariable=mob_number_input).grid(row=1, column=2)

tk.Label(frame1, text="Organization").grid(row=1, column=3)
organization_input = tk.StringVar()
tk.Entry(frame1, textvariable=organization_input).grid(row=1, column=4)

tk.Label(frame1, text="Upload Photo").grid(row=2, column=1)
photoButton = tk.Button(frame1, text="Browse Photo", command=partial(browse_files, "Photo"))
photoButton.grid(row=2, column=2)

tk.Label(frame1, text="Upload Resume").grid(row=2, column=3)
resumeButton = tk.Button(frame1, text="Browse Resume", command=partial(browse_files, "Resume"))
resumeButton.grid(row=2, column=4)

frame2 = tk.Frame(master)
frame2.pack(pady=10)
tk.Button(frame2, text="Generate QR", width=15, command=qr_generator).grid(row=0, column=2)
tk.Button(frame2, text="Quit", width=15, command=master.quit).grid(row=0, column=3)

frame3 = tk.Frame(master)
frame3.pack(pady=10)
output = tk.Label(frame3, text="", bg="#40E0D0")
output.grid(row=3, column=2)
img_lbl = tk.Label(frame3, image="", bg="#40E0D0")
img_lbl.grid(row=4, column=2)

tk.mainloop()
