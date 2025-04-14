import matplotlib.pyplot as plt
from database import get_connection

def add_score(subject, test_name, marks_obtained, total_marks):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO scores (subject, test_name, marks_obtained, total_marks) VALUES (?, ?, ?, ?)",
        (subject, test_name, marks_obtained, total_marks)
    )
    conn.commit()
    conn.close()

def get_scores():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT subject, test_name, marks_obtained, total_marks FROM scores")
    scores = cursor.fetchall()
    conn.close()
    return scores

def show_performance_chart():
    scores = get_scores()
    subjects = {}
    for subject, _, marks, total in scores:
        if subject not in subjects:
            subjects[subject] = [0, 0]
        subjects[subject][0] += marks
        subjects[subject][1] += total

    subject_names = list(subjects.keys())
    percentage = [(m[0] / m[1]) * 100 for m in subjects.values()]

    plt.bar(subject_names, percentage, color="#ffc2d1")
    plt.title("Your StudyBuddy Performance 📊")
    plt.ylabel("Percentage (%)")
    plt.ylim(0, 100)
    plt.show()
