#pip install mysql-connector-python
import mysql.connector

def dbConnect ():
    print ("dbConnect.dbConnect")
    dbConnect2 = {
        'host':'172.23.218.221',
    #    'host':'192.168.1.113',
        'user':'root',
        'password':'sasa1234',
    #    'database':'retest',
        'database':'options',
    } 
    print ("Intentando conectar a la DB:", dbConnect2)
    conex = ''
    try :

        conex = mysql.connector.connect(**dbConnect2)
        print ("Conexion exitosa")
    except:
        print ("fallo la conexion a la DB")
    print ("conex: ", conex)
    return conex

#------------ alta en tabla acciones ------
def NuevaAccion (conex):
    print ("dbConnect.NuevaAccion")
    bRta = True

    mycursor = conex.cursor()

    sql = "INSERT INTO acciones (nombre, url, cantidad) VALUES (%s, %s, %s)"
    val = ('ADGO', 'https://es.investing.com/equities/adecoagro-sa-ar-chart', 120)
    try:
        print ("rta DB:", mycursor.execute(sql, val))
    except (mysql.connector.Error) as e:
        print (e)
        bRta = False
    

    conex.commit()

    return bRta