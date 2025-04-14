import tkinter as tk
from tkinter import messagebox
from styles import *
from tracker import *
from performance import *
from quotes import get_random_quote
from reminders import set_study_reminder
from database import setup_database

setup_database()
set_study_reminder(interval=7200)  # Every 2 hours

app = tk.Tk()
app.title("📚 StudyBuddy – Academic Assistant")
app.geometry("600x500")
app.configure(bg=BACKGROUND)

def show_quote():
    quote = get_random_quote()
    messagebox.showinfo("💬 Motivation", quote)

def add_subject_ui():
    name = entry_subject.get()
    if name:
        add_subject(name)
        entry_subject.delete(0, tk.END)
        messagebox.showinfo("Success", "Subject Added!")

def add_score_ui():
    add_score(entry_score_subject.get(), entry_test_name.get(),
              float(entry_marks.get()), float(entry_total.get()))
    messagebox.showinfo("Success", "Score Added!")

# GUI Elements
tk.Label(app, text="Enter Subject Name:", bg=BACKGROUND).pack()
entry_subject = tk.Entry(app)
entry_subject.pack()
tk.Button(app, text="Add Subject", command=add_subject_ui, bg=BUTTON_COLOR).pack(pady=5)

tk.Label(app, text="Add Score 📈", bg=BACKGROUND).pack(pady=10)
entry_score_subject = tk.Entry(app)
entry_score_subject.insert(0, "Subject Name")
entry_score_subject.pack()

entry_test_name = tk.Entry(app)
entry_test_name.insert(0, "Test Name")
entry_test_name.pack()

entry_marks = tk.Entry(app)
entry_marks.insert(0, "Marks Obtained")
entry_marks.pack()

entry_total = tk.Entry(app)
entry_total.insert(0, "Total Marks")
entry_total.pack()

tk.Button(app, text="Add Score", command=add_score_ui, bg=BUTTON_COLOR).pack(pady=5)
tk.Button(app, text="Show Performance Graph", command=show_performance_chart, bg=HIGHLIGHT).pack(pady=10)

tk.Button(app, text="🎀 Cheer Me Up!", command=show_quote, bg="#e6aace").pack(pady=10)

app.mainloop()
