#parsea un archivo .csv para generar los script insert de un mysql, la tabla tiene el siguiente formato:
#CREATE TABLE History (nombre VARCHAR(100) NOT NULL, fecha_oper DATE NOT NULL, apertura DECIMAL (10,4), maximo DECIMAL (10,4), minimo DECIMAL (10,4), cierre DECIMAL (10,4));

#el archivo de historicos de RAVA tiene el siguiente formato:
#especie,fecha,apertura,maximo,minimo,cierre,volumen,timestamp
#BMA,1993-11-12,9.20458,9.57774,8.70703,9.20458,387681,753073200
#BMA,1993-11-15,9.20458,9.39116,9.20458,9.20458,276213,753332400

#y la salida genera un archivo con inserts por cada registro del .csv del tipo:
#INSERT INTO History (nombre, fecha_oper, apertura, maximo, minimo, cierre) VALUES ('BMA', '1993-11-12',9.20458,9.57774,8.70703,9.20458);


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

