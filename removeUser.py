from tkinter import *
from tkinter import messagebox
import sqlite3
from sqlite3 import Error

#creating widow
class Remove():
    def __init__(self,root):
        self.root = root
        self.root.iconbitmap(r'libico.ico')
        self.root.maxsize(400, 200)
        self.root.minsize(400, 200)
        self.root.title("Remove User")
        a = StringVar()
        def ent():
            if len(a.get()) < 5:
                messagebox.showinfo("Error","Please Enter A Valid Id")
            else:
                d = messagebox.askyesno("Confirm", "Are you sure you want to remove the user?")
                if d:
                    try:
                        self.conn = sqlite3.connect('library_administration.db')
                        self.myCursor = self.conn.cursor()
                        self.myCursor.execute("Delete from admin where id = ?",[a.get()])
                        temp = self.myCursor.fetchone()
                        if not temp:
                            messagebox.showinfo("Oop's","User Not Found")
                            a.set("")
                        else:
                            self.conn.commit()
                            self.myCursor.close()
                            self.conn.close()
                            messagebox.showinfo("Confirm","User Removed Successfully")
                            a.set("")
                    except:
                        messagebox.showerror("Error","Something goes wrong")
        Label(self.root, text = "Enter User Id: ",font=('Arial', 15, 'bold')).place(x = 20,y = 40)
        Entry(self.root,textvariable = a,width = 37).place(x = 160,y = 44)
        Button(self.root, text='Remove', width=15, font=('arial', 10),command = ent).place(x=200, y = 90)


if __name__ == "__main__":
    root = Tk()
    newobj = Remove(root)
    root.mainloop()