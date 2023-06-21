import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()

w, h = 600, 300 #sirka a dlzka
canvas = tk.Canvas(root, width = w, height = h)
canvas.grid(columnspan=3, rowspan=3)

logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

instructions = tk.Label(root, text="Vyber PDF súbor", font="Raleway")
instructions.grid(columnspan=3, row=1)

def open_file():
  browse_text.set("načítavanie...")
  file = askopenfile(parent=root, mode="rb", title="Vyber súbor", filetypes=[("Pdf file","*.pdf")])
  if file:
      read_pdf = PyPDF2.PdfFileReader(file)
      page = read_pdf.getPage(0)
      page_content = page.extractText()
      h, w = 10, 50
      text_box = tk.Text(root, height=h, width=w, padx=15, pady=15)
      text_box.insert(1.0, page_content)
      text_box.tag_configure("center", justify="center")
      text_box.tag_add("center", 1.0, "end")
      text_box.grid(column=1, row=3)
      browse_text.set("Prehľadávať")

w, h = 10, 1 #sirka a dlzka tlacitka
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="black", fg="white", height=h, width=w)
browse_text.set("Prehľadávať")
browse_btn.grid(column=1, row=2)

w, h = 600, 250
canvas = tk.Canvas(root, width = w, height = h)
canvas.grid(columnspan=3)

tk.mainloop()
