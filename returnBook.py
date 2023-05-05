from tkinter import *
from tkinter import messagebox
from datetime import datetime,date
import sqlite3


class Return():
    def __init__(self,root):
        self.root = root
        self.root.iconbitmap(r'libico.ico')
        self.root.title("Return")
        self.root.maxsize(450,300)
        self.root.minsize(450, 300)
        bid = StringVar()
        self.fine = 0

        def days_between(d1, d2):
            if d2 == d1:
                return 0
            else:
                d1 = datetime.strptime(d1, "%Y-%m-%d")
                d2 = datetime.strptime(d2, "%Y-%m-%d")
                return abs((d2 - d1).days)

        def qui():
            self.conn = sqlite3.connect('library_administration.db')
            self.mycursor = self.conn.cursor()
            if len(bid.get()) == 0:
                messagebox.showerror("Error","Please Enter The Book Id")
            else:
                try:
                    self.mycursor.execute("SELECT SID from issue where BID = ?", [bid.get()])
                    sid = self.mycursor.fetchone()
                    if sid:
                        sid = sid[0]
                        self.mycursor.execute("SELECT bissued , fine FROM students WHERE reg_no = ?", [sid])
                        details = self.mycursor.fetchone()
                        print(details)
                        bisd = details[0]
                        fine = details[1]
                        bisd = bisd - 1
                        self.mycursor.execute("UPDATE students SET bissued = ? WHERE reg_no = ?",[bisd,sid])
                        self.mycursor.execute("Select Issue_date from issue where BID = ? ",[bid.get()])
                        idate = str(self.mycursor.fetchone()[0])
                        daysbtw = days_between(idate,str(date.today()))
                        if daysbtw > 5:
                            self.fine = (daysbtw - 5)*10
                        self.fine = self.fine + fine
                        self.mycursor.execute("UPDATE students SET fine = ? WHERE reg_no = ?",[self.fine,sid])
                        self.mycursor.execute("UPDATE books SET Availiability = 1 WHERE Book_Id = ?",[bid.get()])
                        self.mycursor.execute("DELETE FROM issue WHERE BID = ?", [bid.get()])
                        self.conn.commit()
                        self.conn.close()
                        messagebox.showinfo('Info', 'Succesfully Returned')
                        self.root.destroy()
                    else:
                        messagebox.showinfo("Oop's", "Book not yet issued")
                except sqlite3.Error:
                    messagebox.showerror("Error","Something Goes Wrong")
        Label(self.root, text='Return Book', fg='red',font=('arial', 35, 'bold')).pack()
        Label(self.root, text='Enter Book ID', font=('Comic Scan Ms', 15, 'bold')).place(x=30, y=120)
        Entry(self.root, textvariable=bid, width=40).place(x=180, y=124)
        Button(self.root, text="Return", width=25, command=qui).place(x=180, y=180)

if __name__ == "__main__":
    root = Tk()
    newobj = Return(root)
    root.mainloop()
