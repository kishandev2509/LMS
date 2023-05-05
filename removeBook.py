from tkinter import *
from tkinter import messagebox
import sqlite3
from sqlite3 import Error

class Remove():
    def __init__(self,root):
        self.root = root
        self.root.iconbitmap(r'libico.ico')
        self.root.maxsize(500,250)
        self.root.minsize(500,250)
        self.root.title("Remove book")
        a = StringVar()

        def aaa():
            if len(a.get()) == 0:
                messagebox.showerror("Error","Please Enter The Book Id")
            else:
                c = messagebox.askyesno('Remove Book', 'Are You Sure You Want To Remove The Book')
                if c:
                    try:
                        self.conn = sqlite3.connect('library_administration.db')
                        self.mycursor = self.conn.cursor()
                        self.mycursor.execute("DELETE FROM books WHERE Book_Id = ?",[a.get()])
                        messagebox.showinfo('Remove', 'Succesfully Removed')
                        self.conn.commit()
                        self.conn.close()
                        self.root.destroy()
                    except Error:
                        messagebox.showerror("Error", "Something Goes Wrong")

        lb = Label(self.root, text="Enter Book Id", font=('Comic Scan Ms', 20, 'bold'))
        lb.place(x=30, y=70)
        e = Entry(self.root, textvariable=a, width=30).place(x=240, y=75)
        bt = Button(self.root, text="Remove", width=20, command=aaa).place(x=240, y=120)

if __name__ == "__main__":
    root = Tk()
    newobj = Remove(root)
    root.mainloop()