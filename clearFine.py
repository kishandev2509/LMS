from tkinter import *
from tkinter import messagebox
import sqlite3

#creating window
class ClearFine():
    def __init__(self,root):
        self.root = root
        self.root.iconbitmap(r'libico.ico')
        self.root.maxsize(500, 300)
        self.root.minsize(500, 300)
        self.root.title("Clear Fine")
        #creating variables
        a = StringVar()
        def clear():
            if len(a.get()) == 0:
                messagebox.showerror("Error","Please Enter The Id")
            elif a.get().isdigit():
                try:
                    self.conn = sqlite3.connect('library_administration.db')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("Select reg_no from students where reg_no = ?",[a.get()])
                    students = self.myCursor.fetchall()
                    if len(students) != 0:
                        self.myCursor.execute("Update students set Fine = 0 where reg_no = ?",[a.get()])
                        self.conn.commit()
                        self.conn.close()
                        messagebox.showinfo("Successful","All Fine Cleared")
                        self.root.destroy()
                    else:
                        messagebox.showinfo("Oops","The Id you entered is not found")
                except:
                    messagebox.showinfo("Oops","Something goes wrong")
            else:
                messagebox.showerror("Error","Please Check The Id")               
        Label(self.root,text="Enter Student Id", font = ('arial',15,'bold')).place(x=50,y=100)
        Entry(self.root,textvariable=a,width=40).place(x=230,y=105)
        Button(self.root, text='Clear Fine', width=20,command = clear).place(x=230, y=155)
if __name__ == "__main__":
    root = Tk()
    newobj = ClearFine(root)
    root.mainloop()