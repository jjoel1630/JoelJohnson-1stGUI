import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import pandas as pd

# Initialize Tkinter
root = tk.Tk()
root.title("PDF + XLSX Text Extractor")
root.resizable(True, True)

# Create a Tkinter window
canvas = tk.Canvas(root, width=500, height=300)
canvas.grid(columnspan=3, rowspan=3)

# Upload and resize logo
logo = Image.open('hurts.png')
logo = logo.resize((2208 // 4, 1242 // 4))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# Create Tkinter instructions logo
instructions = tk.Label(root, text="Select a PDF or XLSX file on your computer to extract all its text", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

# Function to browse and open files
def open_file(file_type):
	try:
		# Open the file the user selects, ensuring it is a PDF or XLSX
		browse_text.set("loading...")
		file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf"), ("Excel file", "*.xlsx")])

		# If the file is a PDF, open and extract the text from it, placing it in a text box
		if file_type == "pdf":
			read_pdf = PyPDF2.PdfFileReader(file)
			page = read_pdf.getPage(0)
			page_content = page.extractText()

			# Create text box to display the raw text
			text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
			text_box.insert(1.0, page_content)
			text_box.tag_configure("center", justify="center")
			text_box.tag_add("center", 1.0, "end")
			text_box.grid(column=1, row=3)

			browse_text.set("Browse")
		
		# If the file is a spreadsheet, open and extract the text from it, placing it in a text box
		elif file_type == "xlsx":
			try:
				# Create Pandas dataframe to read the data
				df = pd.read_excel(file)
	
				# Create text box to display the header of the data
				text_box = tk.Text(root, height=10, width=50, padx=15, pady=15) # added one text box
				text_box.grid(row=2,column=1,pady=10) # 
				text_box.delete('1.0',tk.END) # Delete previous data from position 0 till end
				text_box.insert(1.0, df.head()) # adding data to tex		
				text_box.tag_configure("center", justify="center")
				text_box.grid(column=1, row=3)

				browse_text.set("Browse")

			# In the case of an error, reset the screen and exit
			except Exception:
				browse_text.set("Browse")
				return None

		else:
			browse_text.set("Browse")
			return None

	except Exception:
		browse_text.set("Browse")
		return None

# Simple UI for a file type dropdown menu
file_type = tk.StringVar(root)
file_type.set("pdf")
file_type_menu = tk.OptionMenu(root, file_type, "pdf", "xlsx")
file_type_menu.grid(column=2, row=2)

# Basic Tkinter brows button that calls the open_file() method on click
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(file_type.get()), font="Raleway", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()
