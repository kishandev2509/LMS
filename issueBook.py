from tkinter import *
from tkinter import messagebox
import sqlite3

#creating window
class Issue():
    def __init__(self,root):
        self.root = root
        self.root.iconbitmap(r'libico.ico')
        self.root.title('Library Admisintration')
        self.root.maxsize(500, 500)
        self.root.minsize(500, 500)
        bid = StringVar()
        sid = StringVar()
        self.conn = sqlite3.connect('library_administration.db')
        self.mycursor = self.conn.cursor()
        self.issue = 0
        self.fine = 0

        def issuebook():
            self.issue = self.issue + 1
            self.mycursor.execute("INSERT INTO issue(BID,SID) VALUES (?,?)",[bid.get(), sid.get()])
            self.mycursor.execute("UPDATE books SET Availiability = 0 WHERE Book_Id = ?",[bid.get()])
            self.mycursor.execute("UPDATE students SET bissued = ? where reg_no = ?",[self.issue, sid.get()])
            self.conn.commit()
            self.conn.close()
            messagebox.showinfo('Save', 'Successfully Issued')
            self.root.destroy()
                
        #verifying input
        def issuebooks():
            if len(bid.get()) == 0 or len(sid.get()) == 0:
                messagebox.showinfo("Error","Please Enter The Id's")
            else:
                try:
                    self.mycursor.execute("Select Availiability from books where Book_Id = ?",[bid.get()])
                    temp = self.mycursor.fetchone()
                    try:
                        if temp[0] == 0:
                            messagebox.showinfo("Oop's","Book Already Issued")
                        else:
                            self.mycursor.execute("Select fine from students where reg_no = ?", [sid.get()])
                            self.fine = self.mycursor.fetchone()[0]
                            self.mycursor.execute("Select bissued from students where reg_no = ?", [sid.get()])
                            self.issue = self.mycursor.fetchone()[0]
                            if self.issue < 3:
                                if self.fine >= 100:
                                    messagebox.showerror('Oops', 'Cannot Issue.Please Pay the Fine')
                                elif self.fine == 0:
                                    issuebook()
                                elif self.fine > 0:
                                    Confirm = messagebox.askyesno('Confirm','Are you sure you want to issue.There is a fine')
                                    if Confirm:
                                        issuebook()
                                    else:
                                        messagebox.showinfo('Oops', 'Not Issued')
                            else:
                                messagebox.showerror("Can't Issue", "Maximum number of books aleady issued")
                    except:
                        messagebox.showinfo("Oop's", "Either BookID or StudentId Not Available")
                except:
                    messagebox.showerror("Error","Something Goes Wrong")
        
        #label and input box
        Label(self.root, text='Book Issuing', font=('Arial Black', 35)).place(x=100, y=40)
        Label(self.root, text='Book ID  :', font=('Arial', 15), fg='red').place(x=60, y=153)
        Entry(self.root, textvariable=bid, width=40).place(x=190, y=160)
        Label(self.root, text='Student ID  :', font=('Arial', 15), fg='red').place(x=60, y=193)
        Entry(self.root, textvariable=sid, width=40).place(x=190, y=200)
        Button(self.root, text="ISSUE", width=30, command=issuebooks).place(x=150, y=290)
if __name__ == "__main__":
    root = Tk()
    newobj = Issue(root)
    root.mainloop()