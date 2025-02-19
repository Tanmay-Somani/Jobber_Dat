 
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.database import get_db_connection


def create_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS job_profiles (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE,
            skills TEXT,
            experience TEXT
        )
    """)
    
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    create_table()
    print("Database initialized successfully.")
