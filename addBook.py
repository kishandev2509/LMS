from tkinter import *
from tkinter import messagebox
import sqlite3
from sqlite3 import Error

#creating window
class Add():
    def __init__(self,root):
        self.root = root
        self.root.iconbitmap(r'libico.ico')
        self.root.maxsize(500, 500)
        self.root.minsize(500, 500)
        self.root.title('Add Book')
        bid = StringVar()
        bname = StringVar()
        bauthor = StringVar()
        #verifying Input
        def b_q():
            if len(bid.get()) == 0 or len(bname.get()) == 0:
                messagebox.showerror("Error","Please Enter The Details")
            else:
                availiability = 1
                try:
                    self.conn = sqlite3.connect('library_administration.db')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("Insert into books values (?,?,?,?)",[bid.get(),bname.get(),bauthor.get(),availiability])
                    self.conn.commit()
                    messagebox.showinfo('Info', 'Succesfully Added')
                    self.root.destroy()
                except Error:
                    messagebox.showerror("Error","Check The Details")
        #creating input box and label
        Label(self.root, text='').pack()
        Label(self.root, text='Book Details', fg='red', font=('Arial', 25, 'bold')).pack()
        Label(self.root, text='').pack()
        Label(self.root, text='Book Id:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=130)
        Entry(self.root, textvariable=bid, width=30).place(x=230, y=132)
        Label(self.root, text='Book Name:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=180)
        Entry(self.root, textvariable=bname, width=30).place(x=230, y=182)
        Label(self.root, text='Book Author:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=230)
        Entry(self.root, textvariable=bauthor, width=30).place(x=230, y=232)
        Button(self.root, text="Submit", command=b_q).place(x=260, y=330)

if __name__ == "__main__":
    root = Tk()
    newobj = Add(root)
    root.mainloop()