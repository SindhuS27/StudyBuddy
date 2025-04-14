from database import get_connection

def add_subject(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO subjects (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def get_subjects():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subjects")
    subjects = cursor.fetchall()
    conn.close()
    return subjects

def add_topic(subject_id, topic, status="Not Started"):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO topics (subject_id, topic, status) VALUES (?, ?, ?)",
                   (subject_id, topic, status))
    conn.commit()
    conn.close()

def update_topic_status(topic_id, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE topics SET status=? WHERE id=?", (status, topic_id))
    conn.commit()
    conn.close()

def get_topics_for_subject(subject_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM topics WHERE subject_id=?", (subject_id,))
    topics = cursor.fetchall()
    conn.close()
    return topics
