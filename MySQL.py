import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="root", passwd="Agasthya4572$:my", database="Test"
)

cursor = db.cursor()
