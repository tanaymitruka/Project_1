import pickle
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox
import datetime as t
import os
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("1920x1080")
root.configure(bg="white")
root.title("ATTENDANCE")

img = Image.open(r"C:\Users\Happy\Desktop\Python\1.png")
size_image = img.resize((150, 50))
img_tk = ImageTk.PhotoImage(size_image)

lb = tk.Label(root, text="Attendance Register", font=("Times New Roman", 40), bg="LightBlue", fg="black", height=75, width=1600, compound="right", 
            image=img_tk, anchor = "e", padx = 200)
lb.pack(padx=10, pady=10, fill = "both", expand = True)

lb1 = tk.Label(root, text="TEACHER'S PORTAL", font=("Arial", 35), bg="red", fg="black", height=1, width=20)
lb1.pack(padx=10, pady=10)

lb2 = tk.Label(root, text="Username", font=("Arial", 40), bg="white", fg="black", height=2, width=20)
lb2.pack(pady=20)

username_entry = tk.Entry(root, bg="HoneyDew1", font=("Arial", 25), width=25)
username_entry.pack(pady=10)

lb3 = tk.Label(root, text="Password", font=("Arial", 40), bg="white", fg="black", height=2, width=20)
lb3.pack(pady=20)

password_entry = tk.Entry(root, bg="honeydew1", font=("Arial", 25), width=25, show='*')
password_entry.pack(pady=10)

today = t.date.today()
formatted = today.strftime("%d-%m-%Y")

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def send_email(to_email, status):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "betacstest69@gmail.com"
    smtp_password = "rtjm gptp ilea hvtm"

    from_email = smtp_username
    subject = "Attendance Notification"
    body = f"Your ward's attendance status is: {status}"

    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(message)
        print(f"Email sent successfully to {to_email}!")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")
    finally:
        server.quit()

def submit_attendance(students, class_file):
    file_exists = os.path.isfile(class_file)
    if file_exists:
        with open(class_file, 'r') as file:
            reader = csv.reader(file)
            rows = [row for row in reader]
    else:
        rows = [["Roll No", "NAME"]]
    if formatted not in rows[0]:
        rows[0].append(formatted)
    existing_data = {row[1]: row for row in rows[1:]}
    c = 0
    for name, attendance_var in students.items():
        c += 1
        status = attendance_var.get()
        if name in existing_data:
            existing_data[name].append(status)
        else:
            new_row = [c, name] + [''] * (len(rows[0]) - 3)
            new_row.append(status)
            existing_data[name] = new_row

        if status in ["A", "P"]:
            try:
                with open("Emails12D.dat", "rb") as f:
                    email_data = pickle.load(f)

                normalized_name = name.strip().lower()
                normalized_data = {k.strip().lower(): v for k, v in email_data.items()}

                if normalized_name in normalized_data:
                    message_body = f"Your ward {name} has been marked {'Absent' if status == 'A' else 'Present'} for {formatted}"
                    send_email(normalized_data[normalized_name], message_body)

            except FileNotFoundError:
                print("Email data file not found.")
            except Exception as e:
                print(f"An error occurred: {e}")
    messagebox.showinfo("Success", "Attendance Submitted!")

    with open(class_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(rows[0])
        for row in existing_data.values():
            writer.writerow(row)

def student_register(students, class_file):
    clear_window()
    lb_new = tk.Label(root, text="Student Register", font=("Arial", 40), bg="Olive", fg="black", height=2, width=130)
    lb_new.pack(padx=10, pady=10)
    
    for name in students:
        at_var = students[name]
        rad = tk.Radiobutton(root, text=name, font=('Arial', 20), value="P", variable=at_var, bg="white")
        rad.pack(pady=10)

    submit_button = tk.Button(root, text="SUBMIT", font=("Arial", 25), fg="Black", bg='SlateGray1', height=2, width=10,
                              command=lambda: submit_attendance(students, class_file))
    submit_button.pack(pady=5)

def Roopa():
    students = {"Tarun": tk.StringVar(value="A"), "Venkat": tk.StringVar(value="A"), "Tanay": tk.StringVar(value="A"), "Ashutosh": tk.StringVar(value="A"), 
                "Sukirthan": tk.StringVar(value="A"), "Sujan": tk.StringVar(value="A"), "Nivetha": tk.StringVar(value="A"), "Tejasjree": tk.StringVar(value="A"), 
                "Vardhine": tk.StringVar(value="A")}
    student_register(students, "12D.csv")

def Janaki():
    students = {"Hazna": tk.StringVar(value="A"), "Aayush": tk.StringVar(value="A"), "Mithil": tk.StringVar(value="A"), "Akshay": tk.StringVar(value="A"), 
                "Vishruth": tk.StringVar(value="A"), "Sona": tk.StringVar(value="A"), "Pranaav": tk.StringVar(value="A"), "Kanishkar": tk.StringVar(value="A"), 
                "Mahathi": tk.StringVar(value="A")}
    student_register(students, "12A.csv")

def Saju():
    students = {"Kaushik": tk.StringVar(value="A"), "Madhav": tk.StringVar(value="A"), "Sachin": tk.StringVar(value="A"), 
                "Vincy Judia": tk.StringVar(value="A"), "Kavya": tk.StringVar(value="A"), "Tharanya": tk.StringVar(value="A"), "Kanishkaa": tk.StringVar(value="A"), 
                "Avaneesh": tk.StringVar(value="A"), "Deeksha": tk.StringVar(value="A")}
    student_register(students, "12B.csv")

def Preethi():
    students = {"Deepak": tk.StringVar(value="A"), "Sanjeev": tk.StringVar(value="A"), "Shreyanth": tk.StringVar(value="A"), "Poovya": tk.StringVar(value="A"),
                "Aditya": tk.StringVar(value="A"), "Sharvesh": tk.StringVar(value="A"), "Nitish": tk.StringVar(value="A"), "Bhavya": tk.StringVar(value="A"), 
                "Ashwin": tk.StringVar(value="A")}
    student_register(students, "12C.csv")

def Lily():
    students = {"Jay": tk.StringVar(value="A"), "Ankush": tk.StringVar(value="A"), "Akshay": tk.StringVar(value="A"), "Jairam": tk.StringVar(value="A"), 
                "Rishi": tk.StringVar(value="A"), "Vignesh": tk.StringVar(value="A"), "Sanjay": tk.StringVar(value="A"), "Mogeedha": tk.StringVar(value="A"), 
                "Akshaya": tk.StringVar(value="A")}
    student_register(students, "12E.csv")

def submit():
    username = username_entry.get()
    password = password_entry.get()

    try:
        with open("Teachers.dat", "rb") as f:
            credentials = pickle.load(f)
            for i in credentials:
                if username == "Roopa" and password == (i[username] == "Roopa123"):
                    Roopa()
                    return
                elif username == "Janaki" and password == (i[username] == "Janaki123"):
                    Janaki()
                    return
                elif username == "Saju" and password == (i[username] == "Saju123"):
                    Saju()
                    return
                elif username == "Preethi" and password == (i[username] == "Preethi123"):
                    Preethi()
                    return
                elif username == "Lily" and password == (i[username] == "Lily123"):
                    Lily()
                    return
    except (EOFError, FileNotFoundError):
        pass
    
    messagebox.showerror("Error", "Invalid username or password")

submit_button2 = tk.Button(root, text="SUBMIT", font=("Arial", 25), fg="Black", bg='SlateGray1', height=2, width=10, command=submit)
submit_button2.pack(pady=5)

root.mainloop()