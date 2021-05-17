import tkinter as tk
from tkinter.messagebox import * 
import PyPDF2
import os


def write_to_file(str):
    with open('pdf_text.txt','w') as file1:
        file1.writelines(str)
    awn = askyesno('confirm','Text Extracted and Writen\nProceed to Open file?')
    if awn == True:
        os.startfile('pdf_text.txt')
        e.delete(0,tk.END)
    else:
        showinfo('File Saved','File Has Been Saved, Please Check Later')

def convert():
    file_name = e.get()
    if file_name != '' and '.pdf' in file_name:
        try:
            pdf_file = open(file_name,'rb')
            pdf_read = PyPDF2.PdfFileReader(pdf_file)
            page = pdf_read.getPage(0)
            text = page.extractText()
            write_to_file(text)
            pdf_file.close()
        except:
            showerror('File Not Found','File not Found\nPlease Check')
    else:
        showerror('Wrong Data','Please check Info Entered')
        e.delete(0,tk.END)

root = tk.Tk()
root.title('PDF TEXT EXTRACTION')
root.geometry('500x380+550+280')

bg = tk.PhotoImage(file='pdf_bg.png')
bg_label = tk.Label(root,image=bg)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)

e = tk.Entry(root,font=('Times new roman',17))
e.place(x=40,y=150,width=250)
text='Enter File Name'
e.insert(tk.END,text)

extract = tk.Button(root,text='EXTRACT TEXT',command=convert)
extract.place(x=100,y=200)

root.mainloop()

