from tkinter import *
import tkinter.filedialog
from resizer import *

root = Tk()
frame = Frame(root)
frame.pack(padx=20, pady=20)

def resizeClick():
    r = resizer()
    r.resize(eFolder.get(), float(eFactor.get()), frame)

def dialogClick():
    filePath = tkinter.filedialog.askdirectory()
    if filePath != "":
        eFolder.delete(0, len(eFolder.get()))
        eFolder.insert(0, filePath)

lFolder = Label(frame, text="Enter folder path")
lFolder.pack()

eFolder = Entry(frame, width=100)
eFolder.insert(0, "c:\\users\\ricwe\\pictures\\2023_07_03 Phone Cabin Visit\\Ranch\\")
eFolder.pack()

bFileDialog = Button(frame, text="find folder", padx=50, command=dialogClick)
bFileDialog.pack()

lFactor = Label(frame, text="Enter scale factor")
lFactor.pack()

eFactor = Entry(frame, width=10)
eFactor.insert(0, ".25")
eFactor.pack()

bResize = Button(frame, text="resize", padx=50, command=resizeClick)
bResize.pack()

root.mainloop()
