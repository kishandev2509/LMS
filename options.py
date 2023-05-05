from tkinter import *
from tkinter import messagebox
import sqlite3, returnBook, addBook, addStudent, removeStudent, removeBook, issueBook, searchBook, addUser, removeUser, clearFine, searchStudent
from sqlite3 import Error
from tkinter import ttk


#creating window
class MainWin():
    def __init__(self,root):
        self.root =root
        self.root.iconbitmap(r'libico.ico')
        self.root.configure(bg='light blue')
        self.root.maxsize(1366, 768)
        self.root.minsize(1366, 768)
        self.root.state('zoomed')
        self.root.title('Library Administration')
        self.a = StringVar()
        self.b = StringVar()
        self.mymenu = Menu(self.root)

#calling scripts
       
        def addStudents():
            newobj = Toplevel(self.root)
            add = addStudent.Add(newobj)

        def addBooks():
            newobj = Toplevel(self.root)
            add = addBook.Add(newobj)
            
        def addUsers():
            newobj = Toplevel(self.root)
            add = addUser.Add(newobj)

        def cfine():
            newobj = Toplevel(self.root)
            clear = clearFine.ClearFine(newobj)

        def issueBooks():
            newobj = Toplevel(self.root)
            issue = issueBook.Issue(newobj)

        def reissueBooks():
            messagebox.showinfo("Under Development", "This function will be avialabe in next update.\nThanks")
            # reissue = reissueBook.Reissue()
            # reissue.mainloop(reissue)

        def removeBooks():
            newobj = Toplevel(self.root)
            remove = removeBook.Remove(newobj)

        def removeStudents():
            newobj = Toplevel(self.root)
            remove = removeStudent.Remove(newobj)

        def removeUsers():
            newobj = Toplevel(self.root)
            remove = removeUser.Remove(newobj)

        def returnBooks():
            newobj = Toplevel(self.root)
            returnbook = returnBook.Return(newobj)

        def searchBooks():
            newobj = Toplevel(self.root)
            search = searchBook.Search(newobj)

        def searchStudents():
            newobj = Toplevel(self.root)
            search = searchStudent.Search(newobj)

        # def handle(event):
        #     if self.listTree.identify_region(event.x,event.y) == "separator":
        #         return "break"



        #creating table
        self.listTree = ttk.Treeview(self.root,height=13,columns=('SID','Name','Fine','Book Name','Issue Date'))
        self.vsb = ttk.Scrollbar(self.root,orient="vertical",command=self.listTree.yview)
        self.hsb = ttk.Scrollbar(self.root,orient="horizontal",command=self.listTree.xview)
        self.listTree.configure(yscrollcommand=self.vsb.set,xscrollcommand=self.hsb.set)
        self.listTree.heading("#0",text='Book ID',anchor = 'center')
        self.listTree.column("#0",width=105,minwidth=105,anchor='center')
        self.listTree.heading("#1", text='SID')
        self.listTree.column("#1",width=150,minwidth=150,anchor='center')
        self.listTree.heading("Name", text='Name')
        self.listTree.column("Name", width=200,minwidth=200,anchor='center')
        self.listTree.heading("Fine", text='Fine')
        self.listTree.column("Fine", width=100,minwidth=100,anchor='center')
        self.listTree.heading("Book Name", text='Book Name')
        self.listTree.column("Book Name", width=220, minwidth=220,anchor='center')
        self.listTree.heading("Issue Date", text='Issue Date')
        self.listTree.column("Issue Date", width=125, minwidth=125,anchor='center')
        # self.listTree.bind('<Button-1>',handle) if you don't want to expand column activat this and the above handle function
        self.listTree.place(x=40,y=400)
        self.vsb.place(x=943,y=400,height=287)
        self.hsb.place(x=41,y=687,width=902)
        ttk.Style().configure("Treeview",font=('Times new Roman',15))

        add = Menu(self.root, tearoff=False)
        add.add_command(label="Student", command=addStudents)
        add.add_command(label="Book", command=addBooks)

        remove = Menu(self.root, tearoff=False)
        remove.add_command(label="Student", command=removeStudents)
        remove.add_command(label="Book", command=removeBooks)

        adminTools = Menu(self.root, tearoff=False)
        adminTools.add_command(label = "Add User",command = addUsers)
        adminTools.add_command(label = "Remove User",command = removeUsers)
        adminTools.add_command(label = "Clear Fine",command = cfine)

        self.mymenu.add_cascade(label='Add', menu=add)
        self.mymenu.add_cascade(label='Remove', menu=remove)
        self.mymenu.add_cascade(label = 'Admin Tools', menu = adminTools)

        self.root.config(menu=self.mymenu)

        def ser():
            try:
                self.listTree.delete(*self.listTree.get_children())
                self.conn = sqlite3.connect('library_administration.db')
                self.myCursor = self.conn.cursor()
                self.change = int(self.a.get())
                self.myCursor.execute("Select issue.BID, issue.SID, students.name, students.Fine, books.Book_name, issue.Issue_date from books, students, issue where issue.BID = books.Book_Id and issue.SID = students.reg_no AND SID = ?",[self.change])
                self.pc = self.myCursor.fetchall()
                if self.pc:
                    for row in self.pc:
                        self.listTree.insert("",'end',text=row[0] ,values = (row[1],row[2],row[3],row[4],row[5]))
                else:
                    messagebox.showinfo("Error", "Either ID is wrong or The book is not yet issued on this ID")
                self.a.set("")
            except Error:
                messagebox.showerror("Error","Something Goes Wrong")
            except ValueError:
                messagebox.showerror("Error","Enter correct regetration number.")

        def ent():
            try:
                self.listTree.delete(*self.listTree.get_children())
                if len(self.b.get()) == 0:
                    messagebox.showerror("Error", "Please Enter a valid ID")
                    return
                self.conn = sqlite3.connect('library_administration.db')
                self.myCursor = self.conn.cursor()
                self.myCursor.execute("Select issue.BID, issue.SID, students.name, students.fine, books.Book_name, issue.Issue_date from books, students, issue where issue.BID = books.Book_Id and issue.SID = students.reg_no AND BID = ?",[self.b.get()])
                self.pc = self.myCursor.fetchall()
                if self.pc:
                    for row in self.pc:
                        self.listTree.insert("", 'end', text=row[0],values=(row[1], row[2], row[3], row[4], row[5]))
                else:
                    self.myCursor.execute("Select * from books where Book_Id = ?",[self.b.get()])
                    self.pc = self.myCursor.fetchall()
                    if len(self.pc) == 1:
                        messagebox.showinfo("Book Info", f"'{self.pc[0][1]}' book is not issued yet..!")
                    else:
                        messagebox.showerror("Error", "Please Enter a valid ID")
                self.b.set("")    
            except Error:
                messagebox.showerror("Error", "Something Goes Wrong")
        def vall():
            try:
                self.listTree.delete(*self.listTree.get_children())
                self.conn = sqlite3.connect('library_administration.db')
                self.myCursor = self.conn.cursor()
                self.myCursor.execute("Select issue.BID, issue.SID, students.name, students.fine, books.Book_name,issue.Issue_date from books , students ,issue WHERE issue.BID = books.Book_Id AND issue.SID = students.reg_no")
                self.pc = self.myCursor.fetchall()
                if self.pc:
                    for row in self.pc:
                        self.listTree.insert("", 'end', text=row[0],values=(row[1], row[2], row[3], row[4], row[5]))
                else:
                    messagebox.showinfo("Error", "Please Enter a valid ID")
            except Error:
                messagebox.showerror("Error", "Something Goes Wrong")

        #label and input box
        self.label3 = Label(self.root, text='Welcome To GPC\'s Library', bg='light blue', font=('Algerian', 45, 'bold'))
        self.label3.place(x=290, y=80)
        self.label4 = Label(self.root, text="Enter Student Id", bg='light blue', font=('Arial', 20, 'bold'))
        self.label4.place(x=100, y=200)
        self.e1 = Entry(self.root, textvariable=self.a, width=40).place(x=400, y=210)
        self.srt = Button(self.root, text='Search', width=15, font=('arial', 10),command = ser).place(x=700, y=206)
        self.label5 = Label(self.root, text='OR', bg='light blue', font=('arial', 16, 'bold')).place(x=170, y=235)
        self.label5 = Label(self.root, text="Enter Book Id", bg='light blue', font=('Arial', 20, 'bold'))
        self.label5.place(x=100, y=260)
        self.e2 = Entry(self.root, textvariable=self.b, width=40).place(x=400, y=270)
        self.brt = Button(self.root, text='Find', width=15, font=('arial', 10),command = ent).place(x=700, y=266)
        self.button = Button(self.root, text="All Issued Books", bg='light blue', font=('Arial', 15, 'bold'), command=vall).place(x=40, y=350)
        # self.button = Button(self, text='All Books', width=20, font=('Algerian', 20)).place(x=1000,y=150)
        self.button = Button(self.root, text='Search Student', width=20, font=('Algerian', 20), command=searchStudents).place(x=1000,y=250)
        self.button = Button(self.root, text='Search Book', width=20, font=('Algerian', 20), command=searchBooks).place(x=1000,y=350)
        self.brt = Button(self.root, text="Issue Book", width=20, font=('Algerian', 20), command=issueBooks).place(x=1000, y=450)
        self.brt = Button(self.root, text="Reissue Book", width=20, font=('Algerian', 20), command=reissueBooks).place(x=1000, y=550)
        self.brt = Button(self.root, text="Return Book", width=20, font=('Algerian', 20), command=returnBooks).place(x=1000, y=650)

if __name__ == "__main__":
    root  = Tk()
    obj = MainWin(root)
    root.mainloop()