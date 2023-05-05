from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from sqlite3 import Error
import sqlite3


#creating window
class Add():
    def __init__(self,root):
        self.root = root
        self.root.title("Library Administration")
        self.root.maxsize(1366, 768)
        self.root.minsize(1366, 768)
        self.root.state("zoomed")
        self.root.iconbitmap(r'libico.ico')
        self.root.configure(background="dark blue")
        
        #creating variables Please chech carefully
        z = StringVar()
        y = StringVar()
        x = StringVar()
        w = StringVar()
        v = StringVar()
        s = StringVar()
        r = StringVar()

        def insert():
            try:
                self.conn = sqlite3.connect('library_administration.db')
                self.myCursor = self.conn.cursor()
                c = self.myCursor.execute("Insert into admin values (?,?,?,?,?,?,?)",[z.get(), y.get(), x.get(), w.get(), v.get(), s.get(), r.get()])
                self.conn.commit()
                self.myCursor.close()
                self.conn.close()
                if c:
                    messagebox.showinfo("Confirm", "Data Inserted Successfully")
                    self.root.destroy()
            except Error:
                messagebox.showinfo("Error", "Something Goes Wrong")
        
        # verify input
        def verify():
            if(len(z.get())) < 5:
                messagebox.showinfo("Error","Enter User Id\nUser Id should be greater than 4 letters")
            elif (len(y.get())) < 3:
                messagebox.showinfo("Error", "Please Enter Your Full Name")
            elif (len(x.get())) < 8:
                # while True:
                #     if not re.search("[a-z]", x.get()):
                #         flag = -1
                #         break
                #     elif not re.search("[A-Z]", x.get()):
                #         flag = -1
                #         break
                #     elif not re.search("[0-9]", x.get()):
                #         flag = -1
                #         break
                #     elif not re.search("[_@$]", x.get()):
                #         flag = -1
                #         break
                #     elif re.search("\s", x.get()):
                #         flag = -1
                #         break
                #     else:
                #         flag = 0
                #         break
                # if len(x.get()) == 0:
                #     messagebox.showinfo("Error","Please Enter Your Password")
                # elif flag == -1:
                #     messagebox.showinfo("Error","Minimum 8 characters.\nThe alphabets must be between [a-z]\nAt least one alphabet should be of Upper Case [A-Z]\nAt least 1 number or digit between [0-9].\nAt least 1 character from [ _ or @ or $ ].")
                    messagebox.showinfo("Error","Minimum 8 characters are required")
            elif len(w.get()) == 0:
                messagebox.showinfo("Error","Please select a question")
            elif len(v.get()) == 0:
                messagebox.showinfo("Error","Please write an answer")
            elif len(s.get()) == 0 or len(s.get()) > 10 or len(s.get()) < 10:
                messagebox.showinfo("Error","Enter Valid Phone Number")
            # elif len(s.get()) == 10:
            #     if s.get().isdigit():
            #         cas = re.fullmatch("[6-9][0-9]{9}", s.get())
            #         if cas is None:
            #             messagebox.showinfo("Error","Check Your Phone Number")
            else:
                insert()
        
        #label and input
        lbl = Label(self.root,text="Library Management System",font=("Algerian",35,'bold'),fg="white",bg="dark blue").place(x=100,y=80)
        lbl = Label(self.root,text="Enter your details and click save",font=("Arial",20,'bold'),fg="white",bg="dark blue").place(x=450,y=650)
        dframe = Frame(self.root, width=650, height=400, bg="light blue").place(x=370, y=180)
        lbl = Label(self.root,text = "Library Information",font = ("Arial",13,"bold"),bg="light blue")
        lbl.place(x=600,y=220)
        lbl = Label(self.root, text="User ID", font=("Arial", 13, "bold"), bg="light blue")
        lbl.place(x=420, y=260)
        lbl = Label(self.root, text="User - Name", font=("Arial", 13, "bold"), bg="light blue")
        lbl.place(x=420, y=300)
        lbl = Label(self.root, text="User - Password", font=("Arial", 13, "bold"), bg="light blue")
        lbl.place(x=420, y=340)
        lbl = Label(self.root, text="Security Question", font=("Arial", 13, "bold"), bg="light blue")
        lbl.place(x=420, y=380)
        lbl = Label(self.root, text="Security Answer", font=("Arial", 13, "bold"), bg="light blue")
        lbl.place(x=420, y=420)
        lbl = Label(self.root, text="Phone", font=("Arial", 13, "bold"), bg="light blue")
        lbl.place(x=420, y=460)
        lbl = Label(self.root, text="City", font=("Arial", 13, "bold"), bg="light blue")
        lbl.place(x=760, y=460)
        Entry(self.root,textvariable=z,width=60).place(x=620,y=260)
        Entry(self.root, textvariable=y, width=60).place(x=620, y=300)
        Entry(self.root, show = '*',textvariable=x, width=60).place(x=620, y=340)
        ttk.Combobox(self.root, textvariable = w, values=["What is your school name?", "What is your home name?","What is your Father name?", "What is your pet name?"], width=57,state="readonly").place(x=620, y=380)
        Entry(self.root, show = '*',textvariable=v, width=60).place(x=620, y=420)
        Entry(self.root, textvariable=s, width=40).place(x=490, y=460)
        Entry(self.root, textvariable=r, width=30).place(x=805, y=460)
        Button(self.root, text="Save", width=10, font=("Arial", 13, "bold"), command=verify).place(x=560, y=520)
        Button(self.root, text="Cancel", width=10, font=("Arial", 13, "bold")).place(x=720, y=520)

if __name__ == "__main__":
    root = Tk()
    newobj = Add(root)
    root.mainloop()