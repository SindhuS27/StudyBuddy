import time
import threading

def set_study_reminder(message="Time to study! 🎓", interval=3600):
    def reminder_loop():
        while True:
            time.sleep(interval)
            print("\n🔔 Reminder:", message)

    threading.Thread(target=reminder_loop, daemon=True).start()
