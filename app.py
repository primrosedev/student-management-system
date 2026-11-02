"""
Student Management System
Auspify Technologies - Software Development Internship (Task 1)
Built with: Python + Flask + SQLite
Author: primrose makonjo
"""

from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "auspify-secret-key-2026"  # needed for flash messages
DATABASE = "students.db"


# ---------------- DATABASE HELPERS ----------------
def get_db():
    """Create a database connection."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # lets us access columns by name
    return conn


def init_db():
    """Create the students table if it does not exist."""
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL,
            course TEXT NOT NULL,
            age INTEGER NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


# ---------------- ROUTES ----------------
@app.route("/")
def index():
    """Dashboard: show total students + latest 5 records."""
    conn = get_db()
    total = conn.execute("SELECT COUNT(*) FROM students").fetchone()[0]
    latest = conn.execute(
        "SELECT * FROM students ORDER BY id DESC LIMIT 5"
    ).fetchall()
    conn.close()
    return render_template("index.html", total=total, latest=latest)


@app.route("/add", methods=["GET", "POST"])
def add_student():
    """Add a new student record (CREATE)."""
    if request.method == "POST":
        name = request.form["name"].strip()
        email = request.form["email"].strip()
        phone = request.form["phone"].strip()
        course = request.form["course"].strip()
        age = request.form["age"].strip()

        # ---- Validation ----
        errors = []
        if not name:
            errors.append("Name is required.")
        if "@" not in email or "." not in email:
            errors.append("Please enter a valid email address.")
        if not phone.isdigit() or len(phone) < 7:
            errors.append("Phone number must contain digits only.")
        if not course:
            errors.append("Course is required.")
        if not age.isdigit() or not (5 <= int(age) <= 100):
            errors.append("Age must be a number between 5 and 100.")

        if errors:
            for e in errors:
                flash(e, "error")
            return redirect(url_for("add_student"))

        try:
            conn = get_db()
            conn.execute(
                "INSERT INTO students (name, email, phone, course, age, created_at)"
                " VALUES (?, ?, ?, ?, ?, ?)",
                (name, email, phone, course, age,
                 datetime.now().strftime("%Y-%m-%d %H:%M")),
            )
            conn.commit()
            conn.close()
            flash(f"Student '{name}' added successfully!", "success")
            return redirect(url_for("students"))
        except sqlite3.IntegrityError:
            flash("That email is already registered.", "error")
            return redirect(url_for("add_student"))

    return render_template("add_student.html")


@app.route("/students")
def students():
    """View all students with optional search (READ)."""
    q = request.args.get("q", "").strip()
    conn = get_db()
    if q:
        like = f"%{q}%"
        rows = conn.execute(
            "SELECT * FROM students WHERE name LIKE ? OR course LIKE ?"
            " OR email LIKE ? ORDER BY name",
            (like, like, like),
        ).fetchall()
    else:
        rows = conn.execute("SELECT * FROM students ORDER BY name").fetchall()
    conn.close()
    return render_template("students.html", students=rows, q=q)


@app.route("/edit/<int:student_id>", methods=["GET", "POST"])
def edit_student(student_id):
    """Update an existing student (UPDATE)."""
    conn = get_db()
    if request.method == "POST":
        name = request.form["name"].strip()
        email = request.form["email"].strip()
        phone = request.form["phone"].strip()
        course = request.form["course"].strip()
        age = request.form["age"].strip()

        if not name or not email or not course or not age:
            flash("Please fill in all required fields.", "error")
        else:
            try:
                conn.execute(
                    "UPDATE students SET name=?, email=?, phone=?,"
                    " course=?, age=? WHERE id=?",
                    (name, email, phone, course, age, student_id),
                )
                conn.commit()
                flash("Student updated successfully!", "success")
                return redirect(url_for("students"))
            except sqlite3.IntegrityError:
                flash("That email is already registered.", "error")

    student = conn.execute(
        "SELECT * FROM students WHERE id=?", (student_id,)
    ).fetchone()
    conn.close()
    if student is None:
        flash("Student not found.", "error")
        return redirect(url_for("students"))
    return render_template("edit_student.html", student=student)


@app.route("/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    """Delete a student record (DELETE)."""
    conn = get_db()
    conn.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    conn.close()
    flash("Student deleted successfully.", "success")
    return redirect(url_for("students"))


# ---------------- RUN ----------------
if __name__ == "__main__":
    init_db()
    app.run(debug=True)
