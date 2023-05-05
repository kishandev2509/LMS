from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
from PIL import ImageTk,Image
import os,glob


class Search():
    def __init__(self,root):
        self.root = root
        self.root.title("Search Student")
        self.root.maxsize(1000,600)
        self.root.minsize(1000,600)
        self.root.iconbitmap(r'libico.ico')
        f = StringVar()
        g = StringVar()
        self.currentPath =  os.getcwd ()+"\\"
        l1=Label(self.root,text="Search Student",font=("Algerian",20,'bold')).place(x=290,y=20)
        l = Label(self.root, text="Search By", font=("Arial", 15, 'bold')).place(x=60, y=96)
        
        def writeTofile(data,filename):
            with open(filename,'wb') as file:
                file.write(data)

        def insert(data):
            self.issuedBookList.delete(*self.issuedBookList.get_children())
            # print(data)
            for row in data:
                self.issuedBookList.insert("","end",text = row[0], values = (row[1],row[2],row[3],row[4],row[6],row[7]))

        def openImage(path,width,height):
            img=Image.open(path)
            img=img.resize((width,height))
            img=ImageTk.PhotoImage(img,(width,height), master = self.root)
            return img

        def photo(pic):
            try:
                self.conn = sqlite3.connect('library_administration.db')
                self.mycursor = self.conn.cursor()
                self.mycursor.execute("Select * from students where reg_no = ?", [pic])
                pc = self.mycursor.fetchone()
                if pc[5] != '':
                    photoPath =self.currentPath+"Temp Images\\" + pc[1] + ".jpeg"
                    writeTofile(pc[5], photoPath)
                    self.photo = openImage(photoPath,512,512)
                    img = Label(self.root ,image=self.photo, width=150, height=150)
                    img.place(x=625, y=20)
                    filelist = glob.glob("Temp Images\*.jpeg")
                    for file in filelist:
                        os.remove(file)
                else:
                    self.photo = ImageTk.PhotoImage(Image.open("Temp Images\\48-512.png"), master = self.root)
                    Label(self.root, image=self.photo, width=150, height=150).place(x=625, y=20)
            except Error:
                messagebox.showerror("Error", "Something goes wrong")

#clicking the record will open the picture
        def select(a):
            curItem = self.issuedBookList.focus()
            selItem = self.issuedBookList.item(curItem)
            pic = str(selItem['text'])
            photo(pic)

        
        def viall():
            try:
                self.conn = sqlite3.connect('library_administration.db')
                self.mycursor = self.conn.cursor()
                self.mycursor.execute("Select * from students")
                pc = self.mycursor.fetchall()
                if pc:
                    insert(pc)
                else:
                    messagebox.showinfo("Oop's","No Data found", parent = self.root)
            except Error:
                messagebox.showerror("Error", "Something goes wrong")


        def ge():
            if (len(f.get())) == 0:
                messagebox.showinfo('Error', 'Enter the '+g.get(), parent = self.root)
            elif g.get() == 'Name':
                try:
                    self.conn = sqlite3.connect('library_administration.db')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from students where name like ?",['%'+f.get()+'%'])
                    pc = self.mycursor.fetchall()
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Oop's","Name not found")
                except Error:
                    messagebox.showerror("Error", "Something goes wrong")
            elif g.get() == 'ID':
                try:
                    self.conn = sqlite3.connect('library_administration.db')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from students where reg_no like ?", ['%' + f.get() + '%'])
                    pc = self.mycursor.fetchall()
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Oop's", "Id not found")
                except Error:
                    messagebox.showerror("Error", "Something goes wrong")


        b=Button(self.root,text="Find",width=15,font=("Arial",10,'bold'),command=ge).place(x=460,y=148)
        viall=Button(self.root,text="View All",width=15,font=("Arial",10,'bold'),command=viall).place(x=460,y=100)
        c=ttk.Combobox(self.root,textvariable=g,values=["Name","ID"],width=40,state="readonly")
        c.current(1)
        c.place(x = 180, y = 100)
        en = Entry(self.root,textvariable=f,width=43).place(x=180,y=155)
        la = Label(self.root, text="Enter", font=("Arial", 15, 'bold')).place(x=100, y=150)

        def handle(event):
            if self.issuedBookList.identify_region(event.x,event.y) == "separator":
                return "break"

        vframe = Frame(self.root,height=13)
        self.issuedBookList = ttk.Treeview(vframe, height=17, columns=('Name','Branch','Semester','Phone Number','No. Of Books Issued','Fine'))

        self.issuedBookList.heading("#0",text="Registration No")
        self.issuedBookList.heading("Name",text="Name")
        self.issuedBookList.heading("Branch",text="Branch")
        self.issuedBookList.heading("Semester",text="Semester")
        self.issuedBookList.heading("Phone Number",text="Phone Number")
        self.issuedBookList.heading("No. Of Books Issued",text="No. Of Books Issued")
        self.issuedBookList.heading("Fine",text="Fine")
        

        self.issuedBookList.column("#0", width=160, anchor='center')
        self.issuedBookList.column("Name", width=200, anchor='center')
        self.issuedBookList.column("Branch", width=95, anchor='center')
        self.issuedBookList.column("Semester", width=95, anchor='center')
        self.issuedBookList.column("Phone Number", width=135, anchor='center')
        self.issuedBookList.column("No. Of Books Issued", width=115, anchor='center')
        self.issuedBookList.column("Fine", width=100, anchor='center')

        
        self.vsb = ttk.Scrollbar(vframe,orient="vertical",command=self.issuedBookList.yview)
        self.issuedBookList.configure(yscrollcommand=self.vsb.set)

        self.issuedBookList.bind("<Button-1>", handle)
        self.issuedBookList.bind("<ButtonRelease-1>",select)
        # self.issuedBookList.place(x=40, y=200)
        self.issuedBookList.pack(side=LEFT,fill=Y)
        self.vsb.pack(side=RIGHT,fill=Y)
        vframe.place(x=40, y=200)
        # self.vsb.place(x=743,y=200,height=287)
        ttk.Style().configure("Treeview", font=('Times new Roman', 15))

if __name__ == "__main__":
    root = Tk()
    obj = Search(root)
    root.mainloop()