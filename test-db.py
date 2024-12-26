import mysql.connector
print ("otra prueba db")

dbConnect2 = {
    'host':'192.168.1.113',
    'user':'root',
    'password':'sasa1234',
    'database':'test',
 }

conex = mysql.connector.connect(**dbConnect2)

cursor = conex.cursor()

sql = "select * from users"

cursor.execute(sql)

results = cursor.fetchall()

print(results)

for data in results:
    print(data)