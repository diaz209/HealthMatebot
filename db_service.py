import sqlite3

conn = sqlite3.connect("health_bot.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    water INTEGER DEFAULT 0,
    sleep REAL DEFAULT 0,
    exercise INTEGER DEFAULT 0
)
""")
conn.commit()

def update_user(user_id, water=None, sleep=None, exercise=None):
    cursor.execute("INSERT OR IGNORE INTO users(user_id) VALUES(?)", (user_id,))
    if water is not None:
        cursor.execute("UPDATE users SET water=? WHERE user_id=?", (water, user_id))
    if sleep is not None:
        cursor.execute("UPDATE users SET sleep=? WHERE user_id=?", (sleep, user_id))
    if exercise is not None:
        cursor.execute("UPDATE users SET exercise=? WHERE user_id=?", (exercise, user_id))
    conn.commit()

def get_user(user_id):
    cursor.execute("SELECT water, sleep, exercise FROM users WHERE user_id=?", (user_id,))
    return cursor.fetchone()
