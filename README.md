# 📚 Library Management System

A **Desktop-based Library Management System** built using **Python 3** and **Tkinter GUI framework**, backed with **SQLite3 database** for seamless data storage and retrieval. This application is designed to manage a college/school library with functionality for book, student, and user management.

---

## 🗈️ Project Demo

> GUI-based app with multi-user support, role-based user management, and visually rich student records including profile images.

---

## 📂 Directory Structure

```
kishandev2509-lms/
├── main.py                # Entry point
├── db.py                  # DB setup and schema creation
├── *.py                   # Feature modules (issue, return, add, search etc.)
├── library_administration.db  # SQLite DB
└── README.md              # Project documentation
```

---

## 🚀 Features

### 📕 Book Management

* Add a book with ID, name, and author
* Issue book to students
* Return or reissue a book
* Remove a book
* Check availability

### 🎓 Student Management

* Add student with full details and profile picture
* Remove student records
* Search students by name or registration number
* Fine management based on return delays

### 👤 User/Admin Management

* Add/remove library administrators
* Secure login system with password reset via security questions
* Fine clearance module for administrators

### 🔍 Search Capabilities

* Search books by ID, name, or author
* Search students with dynamic filters

---

## 🛠️ Technologies Used

| Tool/Library  | Purpose                          |
| ------------- | -------------------------------- |
| Python 3      | Core programming language        |
| Tkinter       | GUI design                       |
| SQLite3       | Local lightweight database       |
| PIL / ImageTk | Profile image display (optional) |
| OS / Glob     | File and image management        |

---

## 💾 Installation & Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/kishandev2509/LMS.git
   cd LMS
   ```

2. **Install Requirements**
   No external packages needed if you're using standard Python installation with Tkinter and sqlite3 support.
   However, to ensure GUI image support, install PIL:

   ```bash
   pip install pillow
   ```

3. **Run the App**

   ```bash
   python main.py
   ```

4. **Important: Initial Setup**

   * On first run, you'll be prompted to register an admin user.
   * A `library_administration.db` file will be created to store data.

5. **Important Notes**

   * Create a folder named **`Temp Images`** in the project root.
   * Add a file named **`48-512.png`** to be used as default student image if no profile is uploaded.

---

<!-- 
## 📸 Screenshots (Optional)

> *Add GUI screenshots here to show the dashboard, add book/student dialogs, etc.*

--- -->

## 📝 Future Enhancements

* ✅ Reissue book with fine auto-adjustment (some parts under dev)
* 🔒 Role-based authentication (admin vs. operator)
* 🌐 Web-based interface (Django/Flask)

---

## 👨‍💻 Author

> **Kishan Dev**
> GitHub: [kishandev2509](https://github.com/kishandev2509)
> Email: [kishan.dev@example.com](mailto:kishan.dev@example.com)

---

<!-- ## 📃 License

This project is licensed under the [MIT License](LICENSE). -->
