import sqlite3
from sqlite3 import Error
from tkinter import *
from tkinter import messagebox, ttk


#creating window
class Fp():
    def __init__(self,root):
        self.root = root
        self.root.iconbitmap(r'libico.ico')
        self.root.maxsize(500, 400)
        self.root.minsize(500, 400)
        self.root.title("Forget Password")
        #creating variables
        a = StringVar()
        b = StringVar()
        c = StringVar()
        d = StringVar()
        e = StringVar()
        #verifying input
        def ins():
            if (len(d.get())) < 8 or len(e.get()) < 8:
                # while True:
                #     if not re.search("[a-z]", d.get()):
                #         flag = -1
                #         break
                #     elif not re.search("[A-Z]", d.get()):
                #         flag = -1
                #         break
                #     elif not re.search("[0-9]", d.get()):
                #         flag = -1
                #         break
                #     elif not re.search("[_@$]", d.get()):
                #         flag = -1
                #         break
                #     elif re.search("\s", d.get()):
                #         flag = -1
                #         break
                #     else:
                #         flag = 0
                #         break
                # if len(d.get()) == 0:
                #     messagebox.showinfo("Error","Please Enter Your Password")
                # elif flag == -1:
                #     messagebox.showinfo("Error","Minimum 8 characters.\nThe alphabets must be between [a-z]\nAt least one alphabet should be of Upper Case [A-Z]\nAt least 1 number or digit between [0-9].\nAt least 1 character from [ _ or @ or $ ].")
                    messagebox.showinfo("Error","Minimum 8 characters are required.")
            elif d.get() != e.get():
                messagebox.showinfo("Error","New and retype password are not some")
            else:
                try:
                    self.conn = sqlite3.connect('library_administration.db')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("Update admin set password = ? where id = ?",[e.get(),a.get()])
                    self.conn.commit()
                    self.myCursor.close()
                    self.conn.close()
                    messagebox.showinfo("Confirm","Password Updated Successfuly")
                    self.destroy()
                except Error:
                    messagebox.showerror("Error","Something Goes Wrong")

        def check():
            if len(a.get()) < 5:
                messagebox.showinfo("Error","Please Enter User Id")
            elif len(b.get()) == 0:
                messagebox.showinfo("Error","Please Choose a question")
            elif len(c.get()) == 0:
                messagebox.showinfo("Error", "Please Enter a answer")
            else:
                try:
                    self.conn = sqlite3.connect('library_administration.db')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("Select id, secQuestion, secAnswer from admin where id = ? and secQuestion = ? and secAnswer = ?",[a.get(), b.get(), c.get()])
                    pc = self.myCursor.fetchone()
                    if not pc:
                        messagebox.showinfo("Error", "Something Wrong in the Details")
                    else:
                        Label(self.root, text="New Password", font=('arial', 15, 'bold')).place(x=40, y=220)
                        Entry(self.root, show = "*", textvariable=d, width=40).place(x=230, y=224)
                        Label(self.root, text="Retype Password", font=('arial', 15, 'bold')).place(x=40, y=270)
                        Entry(self.root, show = "*", textvariable=e, width=40).place(x=230, y=274)
                        Button(self.root, text="Submit", width=15, command=ins).place(x=230, y=324)
                except Error:
                    messagebox.showerror("Error","Something Goes Wrong")

        # label and input box
        Label(self.root, text="Enter User Id", font=('arial', 15, 'bold')).place(x=40, y=20)
        Label(self.root, text="Security Question",font=('arial', 15, 'bold')).place(x=40, y= 70)
        Label(self.root, text="Security Answer",font=('arial', 15, 'bold')).place(x=40, y= 120)
        Entry(self.root, textvariable=a, width=40).place(x=230, y=24)
        ttk.Combobox(self.root, textvariable = b,values=["What is your school name?", "What is your home name?","What is your Father name?", "What is your pet name?"], width=37,state="readonly").place(x=230, y=74)
        Entry(self.root, show = "*", textvariable=c, width=40).place(x=230, y=124)
        Button(self.root, text='Verify', width=15,command = check).place(x=230, y=170)

if __name__ == "__main__":
    root = Tk()
    newobj = Fp(root)
    root.mainloop()
