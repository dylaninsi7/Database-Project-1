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

