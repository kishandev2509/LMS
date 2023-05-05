import sqlite3

def checkSetup():
    conn = sqlite3.connect('library_administration.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='admin'")
    result = cursor.fetchone()
    conn.close()
    if result is None:
        return False
    return True

def setup():
    conn = sqlite3.connect('library_administration.db')
    cursor = conn.cursor()
    create_admin_table = """
        CREATE TABLE IF NOT EXISTS admin (
            "id"	TEXT NOT NULL,
			"name"	TEXT NOT NULL,
			"password"	TEXT NOT NULL,
			"secQuestion"	TEXT NOT NULL,
			"secAnswer"	TEXT NOT NULL,
			"Phone"	INTEGER NOT NULL CHECK(10),
			"City"	TEXT NOT NULL
        );
    """
    create_books_table = """
        CREATE TABLE IF NOT EXISTS "books" (
            "Book_Id"	INTEGER NOT NULL UNIQUE,
            "Book_name"	TEXT NOT NULL,
            "Author"	TEXT NOT NULL,
            "Availiability"	BOOLEAN NOT NULL DEFAULT 1,
            PRIMARY KEY("Book_Id")
        );
    """
    create_issue_table = """
        CREATE TABLE IF NOT EXISTS "issue" (
            "BID"	INTEGER NOT NULL,
            "SID"	INTEGER NOT NULL,
            "Issue_date"	DATE NOT NULL DEFAULT CURRENT_DATE,
            FOREIGN KEY("BID") REFERENCES "books"("Book_Id"),
            FOREIGN KEY("SID") REFERENCES "students"("reg_no"),
            PRIMARY KEY("BID")
        );
    """
    create_students_table = """
        CREATE TABLE IF NOT EXISTS "students" (
            "reg_no"	INTEGER(12) NOT NULL UNIQUE,
            "name"	TEXT NOT NULL,
            "branch"	TEXT NOT NULL,
            "sem"	INTEGER NOT NULL,
            "phone_no"	INTEGER(10) NOT NULL,
            "dp"	BLOB,
            "bissued"	INTEGER NOT NULL DEFAULT 0,
            "fine"	INTEGER NOT NULL DEFAULT 0,
            UNIQUE("reg_no"),
            PRIMARY KEY("reg_no")
        );
    """
    
    cursor.execute(create_admin_table)
    cursor.execute(create_books_table)
    cursor.execute(create_issue_table)
    cursor.execute(create_students_table)
    conn.commit()
    conn.close()


def getConnection():
    return sqlite3.connect('library_administration.db')
