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
users = [("Yug", "Yug"), ("Yug1", "Yug1"), ("Yug2", "Yug2")]
scores = [(45, 100), (30, 200), (25, 300)]

q1 = "CREATE TABLE Users (ID int PRIMARY KEY AUTO_INCREMENT,Name VARCHAR(50),Pwd VARCHAR(50))"

q2 = "CREATE TABLE Scores (UserID int PRIMARY KEY,FOREIGN KEY(UserID) REFERENCES Users(ID) ,Game1 int DEFAULT 0,Game2 int DEFAULT 0)"

q3 = "INSERT INTO Users (Name,Pwd) VALUES (%s,%s)"

q4 = "INSERT INTO Scores (UserID,Game1,Game2) VALUES (%s,%s,%s)"

# for x, y in enumerate(users):
#     cursor.execute(q3, y)
#     last = cursor.lastrowid
#     cursor.execute(q4, (last,) + scores[x])
# db.commit()

# cursor.execute("SELECT * FROM Scores")
# for x in cursor:
#     print(x)
