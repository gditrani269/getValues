#pip install mysql-connector-python
import mysql.connector

import investing

def dbConnect ():
    print ("dbConnect.dbConnect")
    dbConnect2 = {
        'host':'172.24.117.241',
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
#recibe los parametros nombre de accion, url y cantidad de acciones para insertarlos en la tabla acciones.
def NuevaAccion (conex, sEspecie, sUrl, iCantidad):
    print ("dbConnect.NuevaAccion")
    bRta = True
    mycursor = conex.cursor()

    sql = "INSERT INTO acciones (nombre, url, cantidad) VALUES (%s, %s, %s)"
    #val = ('ADGO', 'https://es.investing.com/equities/adecoagro-sa-ar-chart', 120)
    val = (sEspecie, sUrl, iCantidad)
    try:
        print ("rta DB:", mycursor.execute(sql, val))
    except (mysql.connector.Error) as e:
        print (e)
        bRta = False

    conex.commit()
    return bRta

#---------- modificacion cantidad de acciones -----------------
#recibe: nombre de la accion y cantidad final de ese tipo de acciones para actualizar el campo cantidad de la tabla acciones
def UpdateCantidadAcciones (conex, sEspecie, iCantidad):
    print ("dbConnect.UpdateCantidadAcciones")
    bRta = True
    cursorUpdate = conex.cursor()

    sqlUpdate = "UPDATE acciones SET cantidad = " + str (iCantidad) + " WHERE nombre = '" + sEspecie + "'"
    print ("SQL:", sqlUpdate)
    cursorUpdate.execute (sqlUpdate)
    conex.commit()
    return bRta

#------ poner explicacion
def State (conex, iDolar):
    print ("dbConnect.State")
    bRta = True
    cursor = conex.cursor()

    sql = "select * from acciones"
    cursor = conex.cursor()
    cursor.execute(sql)
    results = {}
    iIndex = 0
    data = {}
    data['Valor Dolar'] = iDolar
    data['Total Pesos'] = 0
    
    data['Total Dolares'] = 0    
    iTotalDolares = 0
    iTotalPesos = 0
    for (sql) in cursor:
  #      print ("Tipo es: " , type(sql[0]))
 #       print ("Tipo es: " , type(sql[1]))
#        print ("Tipo es: " , type(sql[2]))
        print (sql[0], sql[1], sql[2], sql[3])

#        data = investing.lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iAdgo, data, 'ADGO')
        data = investing.lee_val_2 (sql[2], iTotalPesos, iTotalDolares, iDolar, sql[3], data, sql[1])
        print ("data: ", data)
 #       results [iIndex] = sql[0], str(sql[1]), float(sql[2]), float(sql[3]), float(sql[4]), float(sql[5])
  #      print ("\nresults:" , results)
            
        iIndex = iIndex + 1


#    sql = "select * from acciones"
 #   cursor.execute(sql)
  #  results = cursor.fetchall()
   # print(results)
    #for data in results:
     #   print(data)

    return data

def State_new (conex, iDolar):
    print ("dbConnect.State_new")
    iIndex = 0
    iTotalDolares = 0
    iTotalPesos = 0
    data = []
    cursor = conex.cursor()
    sql = "select * from acciones"
    cursor = conex.cursor()
    cursor.execute(sql)
    results = {}
    for (sql) in cursor:
#        print (sql[0], sql[1], sql[2], sql[3])
        iIndex = iIndex + 1
        results = investing.lee_val_new (sql[2], iDolar, sql[3], sql[1], iIndex)
#        print ("results - Saldo_pesos:", results.get ("Saldo_pesos"))
        iTotalDolares += results.get ("Saldo_dolares")
        iTotalPesos += results.get ("Saldo_pesos")
        data.append (results)

    data.append ({
        "id": 0,
        "dolar": iDolar,
        "Saldo_pesos": iTotalPesos,
        "Saldo_dolares": iTotalDolares
    })
    return (data)