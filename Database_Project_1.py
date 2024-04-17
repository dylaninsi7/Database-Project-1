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
