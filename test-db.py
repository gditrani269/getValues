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
    'host':'172.28.183.229',
    'user':'root',
    'password':'sasa1234',
    'database':'retest',
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
#cursor3 = conex.cursor()
results = cursor.fetchall ()
print(results)

fPaginado ()