import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "gustv",
    password = "Climb#18",
    database =  "projete2k25"
)

cursor = db.cursor(dictionary=True)

cursor.execute("SELECT alimentos FROM exames WHERE cliente_id = 1")
coisas = cursor.fetchall()

for i in coisas:
    print(i)