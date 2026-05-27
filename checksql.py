import mysql.connector

# Database Connection 
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2705",
        database="ticket_booking"
    )
    cursor = db.cursor()
    print("Connected to database!")
except:
    print("Database connection failed!")
    exit()
