# 🎓 Student Management System

**Task 1 (Easy) — Auspify Technologies Software Development Internship**

A full-stack web application to manage student records with complete
CRUD (Create, Read, Update, Delete) operations, built using
**Python, Flask, SQLite, HTML, CSS & JavaScript**.

---

## Features
- Add new student records (with validation)
-  View all students in a clean table
-  Update student details
-  Delete records (with confirmation dialog)
-  Search students by name, course or email
-  Dashboard with stats and recently added students
-  Fully responsive design
-  Flash messages for success/error feedback

## Technologies Used
| Layer      | Technology          |
|------------|---------------------|
| Backend    | Python 3 + Flask    |
| Database   | SQLite              |
| Frontend   | HTML5, CSS3, Jinja2 |
| Scripting  | JavaScript          |

## Project Structure
```
student-management-system/
├── app.py                 # Main Flask application (routes + DB logic)
├── requirements.txt       # Python dependencies
├── templates/             # HTML pages (Jinja2)
│   ├── base.html          # Layout: navbar + footer
│   ├── index.html         # Dashboard
│   ├── add_student.html   # Add student form
│   ├── students.html      # View all + search
│   └── edit_student.html  # Edit student form
└── static/
    ├── css/style.css      # Modern responsive styling
    └── js/main.js         # Confirm dialog + flash auto-dismiss
```

##  How to Run

1. **Install Flask** (one time only):
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Open in your browser:**
   ```
   http://127.0.0.1:5000
   ```

The database file `students.db` is created automatically on first run.

##  Testing Checklist
- [x] Add a student → appears in "All Students"
- [x] Try adding a duplicate email → error shown
- [x] Search by name/course/email → correct results
- [x] Edit a student → changes saved
- [x] Delete a student → confirm dialog works, record removed
- [x] Responsive on mobile screen sizes

---
Submitted for **Auspify Technologies Internship — Task 1**
#Auspify #AuspifyTechnologies #AuspifyInternship #AuspifyProjects

GIThub profile link: https://githib.com/primrosedev
