from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
from tkinter import ttk

#creating window
class Add():
    def __init__(self,root):
        self.root = root
        self.root.iconbitmap(r'libico.ico')
        self.root.maxsize(500,500)
        self.root.minsize(500,500)
        self.root.title('Add Student')
        self.sregno = StringVar()
        self.sname = StringVar()
        self.sbranch = StringVar()
        self.ssem = StringVar()
        self.sphoneno = StringVar()
        self.sdp = StringVar()
#uploading image
        def convertToBinaryData(filename):
            if filename == "":
                return filename
            with open(filename, 'rb') as file:
                blobData = file.read()
            return blobData
            
        def containsNumber(value):
            for character in value:
                if character.isdigit():
                    return True
            return False
            
        def fileDialog():
            filename = filedialog.askopenfilename(initialdir = "/",title = "Select A File",filetype = (("jpg","*.jpg"),("png","*.png"),("jpeg","*.jpeg"),("All Files","*.*")))
            self.sdp.set(filename)
#verifying input
        def asi():
            if len(self.sregno.get()) != 12:
                messagebox.showerror("Oop's", "Please Enter Registration Number Correctly")
            elif containsNumber(self.sname.get()) or len(self.sname.get()) < 1:
                messagebox.showerror("Oop's","Please Enter Student Name Correctly")
            elif len(self.sphoneno.get()) < 10 or len(self.sphoneno.get()) > 10:
                messagebox.showerror("Oop's", "Please Enter Your Student Phone Number Correctly")
            else:
                try:
                    self.conn = sqlite3.connect('library_administration.db')
                    self.myCursor = self.conn.cursor()
                    sqlquery = "Insert into students('reg_no','name','branch','sem','phone_no','dp') values (?,?,?,?,?,?)"
                    studentData = [self.sregno.get(),self.sname.get(),self.sbranch.get(),self.ssem.get(),self.sphoneno.get(),convertToBinaryData(self.sdp.get())]
                    pc = self.myCursor.execute(sqlquery,studentData)
                    self.conn.commit()
                    if pc:
                        messagebox.showinfo("Done","Student Inserted Successfully")
                        self.root.destroy()
                    else:
                        messagebox.showerror("Error","Couldn't Insert Data")
                    self.myCursor.close()
                    self.conn.close()
                except sqlite3.IntegrityError as er:
                    messagebox.showerror("Error","Regestration number should be unique")
                # except sqlite3.OperationalError:
                #     print("Oops! This was an operational error. Try again...")
                # except sqlite3.Error as er:
                #     print("sql error"+er)
                # except NameError:
                #     print("Name Error")
                # except ValueError:
                #     print("value error")
                # except IOError:
                #     print("No such file or directory")
                # except :
                #     messagebox.showerror("Error","Something goes wrong")

        # label and input box
        lblheading = Label(self.root, text='Student Details', fg='red', font=('Arial', 25, 'bold')).pack()
        lblregno = Label(self.root, text='Registraion No.', font=('Comic Scan Ms', 10, 'bold')).place(x=70, y=82)
        eregno = Entry(self.root, textvariable=self.sregno, width=30).place(x=200, y=84)
        lblname = Label(self.root, text='Student Name', font=('Comic Scan Ms', 10, 'bold')).place(x=70, y=130)
        ename = Entry(self.root, textvariable=self.sname, width=30).place(x=200, y=132)
        lblbranch = Label(self.root, text='Branch', font=('Comic Scan Ms', 10, 'bold')).place(x=70, y=180)
        cbbranch=ttk.Combobox(self.root,textvariable=self.sbranch,values=["CSE","ME","EE","CE","MLT","MOP"],width=27,state="readonly")
        cbbranch.current(0)
        cbbranch.place(x=200, y=182)
        lblsem = Label(self.root, text='Semester', font=('Comic Scan Ms', 10, 'bold')).place(x=70, y=230)
        cbsem=ttk.Combobox(self.root,textvariable=self.ssem,values=["1","2","3","4","5","6"],width=27,state="readonly")
        cbsem.current(0)
        cbsem.place(x=200, y=232)
        lblphoneno = Label(self.root, text='Phone Number', font=('Comic Scan Ms', 10, 'bold')).place(x=70, y=280)
        ephoneno = Entry(self.root, textvariable=self.sphoneno, width=30).place(x=200, y=282)
        lbldp = Label(self.root,text="Upload image", font=('Comic Scan Ms', 10, 'bold')).place(x=70,y=330)
        btndp=Button(self.root,text="Browse",width=7,command=fileDialog).place(x=400,y=328)
        btnsbmt = Button(self.root, text="Submit",width = 15,command=asi).place(x=230, y=390)
        edp = Entry(self.root,textvariable = self.sdp,width = 30).place(x=200,y=330)
if __name__ == "__main__":
    root = Tk()
    newobj = Add(root)
    root.mainloop()