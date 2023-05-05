from tkinter import *
from tkinter import messagebox
import sqlite3
from sqlite3 import Error


class Remove():
    def __init__(self,root):
        self.root = root
        self.root.iconbitmap(r'libico.ico')
        self.root.maxsize(470,250)
        self.root.minsize(470,250)
        self.root.title("Remove Student")
        a = StringVar()

        def iii():
            if len(a.get()) == 0:
                messagebox.showerror("Error", "Please Enter The Registration No.")
            else:
                c = messagebox.askyesno('Remove Book', 'Are You Sure You Want To Remove The Student')
                if c:
                    try:
                        self.conn = sqlite3.connect('library_administration.db')
                        self.mycursor = self.conn.cursor()
                        self.mycursor.execute("DELETE FROM students WHERE reg_no = ?", [a.get()])
                        messagebox.showinfo('Remove', 'Succesfully Removed')
                        self.conn.commit()
                        self.conn.close()
                        self.root.destroy()
                    except Error:
                        messagebox.showerror("Error", "Something Goes Wrong")

        self.lb = Label(self.root, text="Enter Registration No.", font=('Comic Scan Ms', 15, 'bold'))
        self.lb.place(x=30, y=70)
        self.e1 = Entry(self.root, textvariable=a, width=30).place(x=250, y=77)
        self.butt1234 = Button(self.root, text="Remove", width=20, command=iii).place(x=230, y=120)
if __name__ == "__main__":
    root = Tk()
    newobj = Remove(root)
    root.mainloop()
