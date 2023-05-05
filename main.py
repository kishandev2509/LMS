from tkinter import *
from tkinter import messagebox
import sqlite3, options, forgetPassowd, addUser, db


# creating window
class Lib():
    def __init__(self,root):
        self.root = root
        self.a = StringVar()
        self.b = StringVar()
        self.root.maxsize(1366, 768)
        self.root.minsize(1366, 768)
        self.root.state("zoomed")
        self.root.iconbitmap(r"libico.ico")
        self.root.title("Library Administration")
        self.canvas = Canvas(width=1366, height=768, bg="blue")
        self.canvas.pack()
        self.photo = PhotoImage(file="output-onlinejpgtools1.png")
        self.canvas.create_image(-20, -20, image=self.photo, anchor=NW)

        # verifying input

        def chex():
            if len(self.user_text.get()) < 0:
                messagebox.showinfo("Oop's", "Please Enter Your User Id")
            elif len(self.pass_text.get()) < 0:
                messagebox.showinfo("Oop's", "Please Enter Your Password")
            else:
                try:
                    self.conn = sqlite3.connect("library_administration.db")
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute(
                        "Select * from admin where id=? AND password =?",
                        [self.user_text.get(),
                         self.pass_text.get()],
                    )
                    self.pc = self.myCursor.fetchall()
                    self.myCursor.close()
                    self.conn.close()
                    if self.pc:
                        self.root.destroy()
                        newobj = Tk()
                        option = options.MainWin(newobj)
                    else:
                        messagebox.showinfo("Error", "Username and password not found")
                        self.user_text.delete(0, END)
                        self.pass_text.delete(0, END)
                except sqlite3.Error:
                    messagebox.showinfo("Error", "Something Goes Wrong,Try restarting")

        def fpass():
            newobj = Toplevel(root)
            fp = forgetPassowd.Fp(newobj)



        def check():
            try:
                conn = sqlite3.connect("library_administration.db")
                mycursor = conn.cursor()
                mycursor.execute("Select * from admin")
                z = mycursor.fetchone()
                mycursor.close()
                conn.close()
                if not z:
                    messagebox.showinfo("Error", "Please Register A user")
                    x = messagebox.askyesno("Confirm", "Do you want to register a user")
                    if x:
                        self.destroy()
                        add = addUser.Add()
                        add.mainloop(add)
                        # os.system('%s %s' % (py, 'Reg.py'))
                    else:
                        self.destroy()
                else:
                    self.label = Label(self.root, text="Admin Login", font=("Algerian", 35, "bold"))
                    self.label.place(x=530, y=30)
                    self.label1 = Label(self.root, text="User-Id", font=("Times New roman", 25, "bold"))
                    self.label1.place(x=450, y=200)
                    self.user_text = Entry(self.root, textvariable=self.a, width=45)
                    self.user_text.place(x=650, y=215)
                    self.label2 = Label(self.root, text="Password", font=("Times new roman", 25, "bold"))
                    self.label2.place(x=450, y=250)
                    self.pass_text = Entry(self.root, show="*", textvariable=self.b, width=45)
                    self.pass_text.place(x=650, y=265)
                    self.butt = Button(self.root, text="Login", font=10, width=15, command=chex).place(x=650, y=315)
                    self.butt2 = Button(self.root, text="Forgot Password", font=10, width=18, command=fpass).place(x=830, y=313)
            except sqlite3.Error:
                messagebox.showinfo("Error", "Something Goes Wrong")

        check()


if __name__ == "__main__":
    if not db.checkSetup():
        db.setup()
        newobj = Tk()
        fp = addUser.Add(newobj)
        newobj.mainloop()

    else:
        root = Tk()
        obj = Lib(root)
        root.mainloop()
