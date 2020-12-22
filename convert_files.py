from docx2pdf import convert
from tkinter import *
from tkinter import ttk
from tkinter import filedialog





#function choose word file
def fileDialog():
    global filename
    filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
    (("word files", "*.docx"), ("all files", "*.*")))
    label = ttk.Label( text="")
    label.place(x=90,y=60)
    label.configure(text=filename)

#convert process
def convertFile():
    convert(r"{0}".format(filename),r"{0}".format(filename1))
    label2 = ttk.Label(text="")
    label2.grid(column=1, row=3)
    label2.configure(text="Convert Completed")

#Save it in pdf format
def save():
    global filename1
    filename1 = filedialog.asksaveasfilename(initialdir="/", title="Select A File", filetype=
    (("PDF files", "*.pdf"), ("all files", "*.*")))
    label2 = ttk.Label(text="")
    label2.place(x=400,y=60)
    label2.configure(text=filename1)



window=Tk()

#load the images

img = PhotoImage(file="./icons1/word.png")
img2 = PhotoImage(file="./icons1/pdf.png")
img3= PhotoImage(file="./icons1/word2pdf.png")
logo = Label(window, image =img3,width=650, height=400, bg="#FCFCFC")
logo.place(x=0,y=0)
window.title("Word2PDF")
window.geometry('650x400')
btn=Button(window, command=fileDialog, text = "Browse A File", bg="magenta2", fg="snow",image=img)
btn.place(x=130,y=2)
btn=Button(window,text="Save as", command=save, bg="aquamarine", fg="snow" , image=img2)
btn.place(x=450,y=2)
btn1=Button(window,text="convert", command=convertFile,width=50,fg="snow",bg="red")
btn1.place(x=120,y=360)
window.mainloop()
