import tkinter as tk
from tkinter import simpledialog, messagebox
import mysql.connector

password = None

def get_password():
    global password
    if password is None:
        password = simpledialog.askstring("Password", "Enter your database password:", show='*')
    return password

def connect_to_database():
    try:
        global password
        if password is None:
            password = get_password()

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=password,
            database="student_grade"
        )
        return connection
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to connect to database: {error}")
        return None

    
def insert_student():
    student_id = student_id_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    email = email_entry.get()
    
    if not (student_id and first_name and last_name and email):
        messagebox.showerror("Error", "All fields are required.")
        return
    
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO students (StudentID, FirstName, LastName, Email) VALUES (%s, %s, %s, %s)", (student_id, first_name, last_name, email))
            connection.commit()
            messagebox.showinfo("Success", "Student record inserted successfully.")
            connection.close()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to insert student record: {error}")

def display_students():
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM students")
            students = cursor.fetchall()
            connection.close()
            messagebox.showinfo("Students", "\n".join([str(student) for student in students]))
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to fetch student records: {error}")

def update_student():
    student_id = student_id_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    email = email_entry.get()
    
    if not (student_id and first_name and last_name and email):
        messagebox.showerror("Error", "All fields are required.")
        return
    
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE students SET FirstName=%s, LastName=%s, Email=%s WHERE StudentID=%s", (first_name, last_name, email, student_id))
            connection.commit()
            messagebox.showinfo("Success", "Student record updated successfully.")
            connection.close()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to update student record: {error}")

def delete_student():
    student_id = student_id_entry.get()
    
    if not student_id:
        messagebox.showerror("Error", "Please enter a Student ID.")
        return
    
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM students WHERE StudentID=%s", (student_id,))
            connection.commit()
            messagebox.showinfo("Success", "Student record deleted successfully.")
            connection.close()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to delete student record: {error}")

def insert_grade():
    grade_id = grade_id_entry.get()
    grade = grade_entry.get()
    student_id = student_id_grade_entry.get()
    course_id = course_id_grade_entry.get()
    
    if not (grade_id and grade and student_id and course_id):
        messagebox.showerror("Error", "All fields are required.")
        return
    
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO grades (GradeID, Grade, StudentID, CourseID) VALUES (%s, %s, %s, %s)", (grade_id, grade, student_id, course_id))
            connection.commit()
            messagebox.showinfo("Success", "Grade record inserted successfully.")
            connection.close()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to insert grade record: {error}")

def display_grades():
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM grades")
            grades = cursor.fetchall()
            connection.close()
            messagebox.showinfo("Grades", "\n".join([str(grade) for grade in grades]))
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to fetch grade records: {error}")

def update_grade():
    grade_id = grade_id_entry.get()
    grade = grade_entry.get()
    student_id = student_id_grade_entry.get()
    course_id = course_id_grade_entry.get()
    
    if not (grade_id and grade and student_id and course_id):
        messagebox.showerror("Error", "All fields are required.")
        return
    
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE grades SET Grade=%s, StudentID=%s, CourseID=%s WHERE GradeID=%s", (grade, student_id, course_id, grade_id))
            connection.commit()
            messagebox.showinfo("Success", "Grade record updated successfully.")
            connection.close()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to update grade record: {error}")

def delete_grade():
    grade_id = grade_id_entry.get()
    
    if not grade_id:
        messagebox.showerror("Error", "Please enter a Grade ID.")
        return
    
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM grades WHERE GradeID=%s", (grade_id,))
            connection.commit()
            messagebox.showinfo("Success", "Grade record deleted successfully.")
            connection.close()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to delete grade record: {error}")

def insert_course():
    course_id = course_id_entry.get()
    course_name = course_name_entry.get()
    instructor = instructor_entry.get()
    semester = semester_entry.get()
    
    if not (course_id and course_name and instructor and semester):
        messagebox.showerror("Error", "All fields are required.")
        return
    
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO courses (CourseID, CourseName, Instructor, Semester) VALUES (%s, %s, %s, %s)", (course_id, course_name, instructor, semester))
            connection.commit()
            messagebox.showinfo("Success", "Course record inserted successfully.")
            connection.close()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to insert course record: {error}")

def display_courses():
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM courses")
            courses = cursor.fetchall()
            connection.close()
            messagebox.showinfo("Courses", "\n".join([str(course) for course in courses]))
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to fetch course records: {error}")

def update_course():
    course_id = course_id_entry.get()
    course_name = course_name_entry.get()
    instructor = instructor_entry.get()
    semester = semester_entry.get()
    
    if not (course_id and course_name and instructor and semester):
        messagebox.showerror("Error", "All fields are required.")
        return
    
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE courses SET CourseName=%s, Instructor=%s, Semester=%s WHERE CourseID=%s", (course_name, instructor, semester, course_id))
            connection.commit()
            messagebox.showinfo("Success", "Course record updated successfully.")
            connection.close()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to update course record: {error}")

def delete_course():
    course_id = course_id_entry.get()
    
    if not course_id:
        messagebox.showerror("Error", "Please enter a Course ID.")
        return
    
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM courses WHERE CourseID=%s", (course_id,))
            connection.commit()
            messagebox.showinfo("Success", "Course record deleted successfully.")
            connection.close()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to delete course record: {error}")

root = tk.Tk()
root.title("Student Database Application")

student_id_label = tk.Label(root, text="Student ID:")
student_id_label.grid(row=0, column=0, padx=10, pady=5)
student_id_entry = tk.Entry(root)
student_id_entry.grid(row=0, column=1, padx=10, pady=5)

first_name_label = tk.Label(root, text="First Name:")
first_name_label.grid(row=1, column=0, padx=10, pady=5)
first_name_entry = tk.Entry(root)
first_name_entry.grid(row=1, column=1, padx=10, pady=5)

last_name_label = tk.Label(root, text="Last Name:")
last_name_label.grid(row=2, column=0, padx=10, pady=5)
last_name_entry = tk.Entry(root)
last_name_entry.grid(row=2, column=1, padx=10, pady=5)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=3, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=3, column=1, padx=10, pady=5)

insert_student_button = tk.Button(root, text="Insert Student", command=insert_student)
insert_student_button.grid(row=4, column=0, padx=10, pady=5)

display_students_button = tk.Button(root, text="Display Students", command=display_students)
display_students_button.grid(row=4, column=1, padx=10, pady=5)

update_student_button = tk.Button(root, text="Update Student", command=update_student)
update_student_button.grid(row=5, column=0, padx=10, pady=5)

delete_student_button = tk.Button(root, text="Delete Student", command=delete_student)
delete_student_button.grid(row=5, column=1, padx=10, pady=5)
