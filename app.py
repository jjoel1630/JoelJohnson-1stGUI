"""
CSP 108 - Joel Johnson
"""

import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

# Initialize a tk object
root = tk.Tk()

# Create a tk canvas
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# Load logo + place on screen
logo = Image.open('hurts.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# instructions
instructions = tk.Label(
    root, text="Select a PDF file on your computer to extract all its text", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)


# Allows user to open file from computer
def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[
                       ("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfReader(file)
        page = read_pdf.pages[0]
        page_content = page.extract_text()

        # text formatting
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        browse_text.set("Browse")

        resize_image = logo.resize((200, 200))
        logo_label = tk.Label(image=resize_image)
        logo_label.image = resize_image
        logo_label.grid(column=1, row=0)



# browse button for choosing file
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: open_file(
), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()
