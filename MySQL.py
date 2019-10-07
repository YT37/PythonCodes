import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost", user="root", passwd="Agasthya4572$:my", database="Test"
)

cursor = db.cursor()

# cursor.execute(
#     "CREATE TABLE Info (Name varchar(50) NOT NULL , Created datetime NOT NULL, Gender ENUM('M', 'F', 'O'),id int PRIMARY KEY NOT NULL AUTO_INCREMENT)"
# )


# cursor.execute(
#     "INSERT INTO Info (Name,Created,Gender) VALUES (%s,%s,%s)",
#     ("Krish", datetime.now(), "M"),
# )

# db.commit()

# cursor.execute("SELECT Id,Name FROM Info ORDER BY Id ASC")

# for x in cursor:
#     print(x)

# cursor.execute("ALTER TABLE Info ADD COLUMN Food VARCHAR(50) NOT NULL")
# cursor.execute("DESCRIBE Info")

# cursor.execute("ALTER TABLE Info CHANGE Name firstName VARCHAR(10)")
