#parsea un archivo .csv para generar los script insert de un mysql, la tabla tiene el siguiente formato:
#CREATE TABLE History (nombre VARCHAR(100) NOT NULL, fecha_oper DATE NOT NULL, apertura DECIMAL (5,4), maximo DECIMAL (5,4), minimo DECIMAL (5,4), cierre DECIMAL (5,4));

file1 = open('../csv-script/BMA - Cotizaciones historicas.csv', 'r',encoding='utf-8')
Lines = file1.readlines()

sInsert = "INSERT INTO History (nombre, fecha_oper, apertura, maximo, minimo, cierre) VALUES ('BMA', '"


f = open ('lna.txt','w',encoding='utf-8')

for line in Lines:
    print (line)
    sTmp = ""
    #obtengo fecha
    iFirstTag = line.find(',')
    iSecondTag = line.find (',', iFirstTag+1)
    sTmp = sInsert + line [iFirstTag+1 : iSecondTag] + "',"
    print (line [iFirstTag+1 : iSecondTag])
    print (sTmp)

    #obtengo apertura
    iFirstTag = line.find(',', iSecondTag)
    iSecondTag = line.find (',', iFirstTag+1)
    sTmp = sTmp + line [iFirstTag+1 : iSecondTag] + ","
    print (line [iFirstTag+1 : iSecondTag])
    print (sTmp)

    #obtengo maximo
    iFirstTag = line.find(',', iSecondTag)
    iSecondTag = line.find (',', iFirstTag+1)
    sTmp = sTmp + line [iFirstTag+1 : iSecondTag] + ","
    print (line [iFirstTag+1 : iSecondTag])
    print (sTmp)

    #obtengo minimo
    iFirstTag = line.find(',', iSecondTag)
    iSecondTag = line.find (',', iFirstTag+1)
    sTmp = sTmp + line [iFirstTag+1 : iSecondTag] + ","
    print (line [iFirstTag+1 : iSecondTag])
    print (sTmp)

    #obtengo cierre
    iFirstTag = line.find(',', iSecondTag)
    iSecondTag = line.find (',', iFirstTag+1)
    sTmp = sTmp + line [iFirstTag+1 : iSecondTag] + ");"
    print (line [iFirstTag+1 : iSecondTag])
    print (sTmp)

    f.write(sTmp)
    f.write('\n')


f.close()

