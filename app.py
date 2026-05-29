import mysql.connector
import time
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    while True:
        try:
            conn = mysql.connector.connect(
                host="db",
                user="root",
                password="root123",
                database="testdb"
            )
            return conn
        except:
            print("Waiting for database...")
            time.sleep(2)

@app.route('/')
def home():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255)
    )
    """)

    cursor.execute("INSERT INTO users (name) VALUES ('Docker User')")
    conn.commit()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    conn.close()

    return f"Database Connected Successfully! Data: {rows}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
