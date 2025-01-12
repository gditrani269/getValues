import mysql.connector

def fPaginado ():
    print ("funcion de paginado")
    cursor = conex.cursor()
    sql = "select * FROM History limit 10 offset 10"
    cursor.execute(sql)
    results = cursor.fetchall ()
    print(results)
    print ("sgunda pagina")
    sql = "select * FROM History limit 10 offset 20"
    cursor.execute(sql)
    results = cursor.fetchall ()
    print(results)

print ("otra prueba db")

dbConnect2 = {
#    'host':'172.28.183.229',
    'host':'192.168.1.113',
    'user':'root',
    'password':'sasa1234',
#    'database':'retest',
    'database':'options',
 }

conex = mysql.connector.connect(**dbConnect2)

cursor = conex.cursor()

sql = "select * from History"

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

print ("------------------------")
sql = "select * FROM History limit 10 offset 10"
cursor = conex.cursor()
cursor.execute(sql)
for (sql) in cursor:
     print (sql[0], sql[1], sql[2], sql[3], sql[4], sql[5])
#cursor3 = conex.cursor()
results = cursor.fetchall ()
print(results)

fPaginado ()