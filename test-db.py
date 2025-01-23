
#ejecutar con:
#python3.11 test-db.py

#pip install mysql-connector-python
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
    'host':'172.23.218.221',
#    'host':'192.168.1.113',
    'user':'root',
    'password':'sasa1234',
#    'database':'retest',
    'database':'options',
 }

print ("Arranca")
conex = mysql.connector.connect(**dbConnect2)
print ("Arranca 2")
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
sql = "select * FROM History limit 2 offset 10"
cursor = conex.cursor()
cursor.execute(sql)
results = {}
iIndex = 0
for (sql) in cursor:
    print ("Tipo es: " , type(sql[0]))
    print ("Tipo es: " , type(sql[1]))
    print ("Tipo es: " , type(sql[2]))
    print (sql[0], sql[1], sql[2], sql[3], sql[4], sql[5])
    results [iIndex] = sql[0], str(sql[1]), float(sql[2]), float(sql[3]), float(sql[4]), float(sql[5])
    print ("\nresults:" , results)
        
    iIndex = iIndex + 1
#cursor3 = conex.cursor()


#fPaginado ()