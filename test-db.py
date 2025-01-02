import mysql.connector
print ("otra prueba db")

dbConnect2 = {
    'host':'172.28.183.229',
    'user':'root',
    'password':'sasa1234',
    'database':'test',
 }

conex = mysql.connector.connect(**dbConnect2)

cursor = conex.cursor()

sql = "select * from acciones"

cursor.execute(sql)

results = cursor.fetchall()

print(results)

for data in results:
    print(data)


cursor2 = conex.cursor()
databases = ("show databases")
cursor2.execute(databases)
for (databases) in cursor2:
     print (databases[0])