from fastapi import FastAPI, HTTPException
 
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.database import get_db_connection

app = FastAPI()

# Create Profile
@app.post("/profile/")
def create_profile(name: str, email: str, skills: str, experience: str):
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO job_profiles (name, email, skills, experience) VALUES (%s, %s, %s, %s)",
                       (name, email, skills, experience))
        connection.commit()
    except mysql.connector.IntegrityError:
        raise HTTPException(status_code=400, detail="Email already exists")
    finally:
        cursor.close()
        connection.close()

    return {"message": "Profile created successfully"}

# Get Profile by Email
@app.get("/profile/{email}")
def read_profile(email: str):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM job_profiles WHERE email = %s", (email,))
    profile = cursor.fetchone()

    cursor.close()
    connection.close()

    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")

    return profile
