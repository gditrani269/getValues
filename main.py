# main.py
#ejecutar con:
#uvicorn main:app --host 0.0.0.0 --port 80  --reload
#pip3 install fastapi
#pip3 install "uvicorn[standard]" && \
from fastapi import FastAPI
#pip install mysql-connector-python
import mysql.connector

import mylibs
import investing
import dbConnect

from curl_cffi import requests

from typing import Union

#dbConnect2 = {
#    'host':'172.23.218.221',
##    'host':'192.168.1.113',
#    'user':'root',
#    'password':'sasa1234',
##    'database':'retest',
#    'database':'options',
#} 
#conex = mysql.connector.connect(**dbConnect2)

print ("conectar con la DB")
conex = dbConnect.dbConnect ()
if (conex == ''):
    print ("FALLO la conexxion a la DB ")

def fListaDB ():
    cursor2 = conex.cursor()
    databases = ("show databases")
    cursor2.execute(databases)
    for (databases) in cursor2:
        print (databases[0])

app = FastAPI()
@app.get("/")
async def root():


    
    print ("Arranca")
#    conex = mysql.connector.connect(**dbConnect2)



    return {"greeting":"Hello world"}

@app.get("/items/{item_id}")
def read_item(item_id: int, a: Union[str, None] = None):
    return {"item_id": item_id, "qa": a}

#endpoint con parametro
@app.get("/items2/{item_id}")
async def read_item(item_id):
#    fListaDB ()
    #iDolar = lee_val_dolar ()
    iDolar = mylibs.lee_val_dolar ()

    iMola = 680
    iMsft = 610
    iBma = 3200
    iAdgo = 120
    iAlua = 1850
    iGgal = 560
    TGSU2 = 400
    data = {}
    data['Valor Dolar'] = iDolar
    data['Total Pesos'] = 0
    
    data['Total Dolares'] = 0    
    iTotalDolares = 0
    iTotalPesos = 0
    #url = 'http://localhost:8080/health'
    url = 'https://es.investing.com/equities/adecoagro-sa-ar-chart'
#    sasa = lee_val (url)
    data = investing.lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iAdgo, data, 'ADGO')

#    iTotalPesos = iTotalPesos + sasa*iAdgo
#    iAdgoUsd = sasa*iAdgo/iDolar
#    iTotalDolares = iTotalDolares + iAdgoUsd
#    print (sasa*iAdgo, "en dolares:" ,  iAdgoUsd)
#    data['ADGO'] = str(iAdgoUsd)
    print ("data: ", data)

    url = 'https://es.investing.com/equities/molinos-agro-chart'
#    sasa = lee_val (url)
    data = investing.lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iMola, data, 'MOLA')
#    iTotalPesos = iTotalPesos + sasa*iMola
#    iMolaUsd = sasa*iMola/iDolar
#    iTotalDolares = iTotalDolares + iMolaUsd
#    print (sasa*iMola, "en dolares:" ,  iMolaUsd)
#    data['MOLA'] = str(iMolaUsd)

    url = 'https://es.investing.com/equities/aluar-chart'
#    sasa = lee_val (url)
    data = investing.lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iAlua, data, 'ALUA')
#    iTotalPesos = iTotalPesos + sasa*iAlua
#    iAluaUsd = sasa*iAlua/iDolar
#    iTotalDolares = iTotalDolares + iAluaUsd
#    print (sasa*iAlua, "en dolares:" ,  iAluaUsd)
#    data['ALUA'] = str(iAluaUsd)

    url = 'https://es.investing.com/equities/microsoft-corp-ar-chart'
#    sasa = lee_val (url)
    data = investing.lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iMsft, data, 'MSFT')
#    iTotalPesos = iTotalPesos + sasa*iMsft
#    iMsfUsd = sasa*iMsft/iDolar
#    iTotalDolares = iTotalDolares + iMsfUsd
#    print (sasa*iMsft, "en dolares:" ,  iMsfUsd)
#    data['MSFT'] = str(iMsfUsd)

    url = 'https://es.investing.com/equities/gp-fin-galicia-chart'
#    sasa = lee_val (url)
    data = investing.lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iGgal, data, 'GGAL')
#    iTotalPesos = iTotalPesos + sasa*iGgal
#    iGgalUsd = sasa*iGgal/iDolar
#    iTotalDolares = iTotalDolares + iGgalUsd
#    print (sasa*iGgal, "en dolares:" ,  iGgalUsd)
#    data['GGAL'] = str(iGgalUsd)

    url = 'https://es.investing.com/equities/macro-chart'
#    sasa = lee_val (url)
    data = investing.lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iBma, data, 'BMA')
#    iTotalPesos = iTotalPesos + sasa*iBma
#    iBmaUsd = sasa*iBma/iDolar
#    iTotalDolares = iTotalDolares + iBmaUsd
#    print (sasa*iBma, "en dolares:" ,  iBmaUsd)
#    data['BMA'] = str(iBmaUsd)

    url = 'https://es.investing.com/equities/tran-gas-del-s'
#    sasa = lee_val (url)
    data = investing.lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, TGSU2, data, 'TGSU2')


    print ("Total Pesos: ", iTotalPesos)
    print ("Total Dolares: ", iTotalDolares)
    sRta = "Total Pesos: " + str(iTotalPesos) + "Total Dolares: " + str(iTotalDolares)
#    data['Total Pesos'] = str(iTotalPesos)
#    data['Total Dolares'] = str(iTotalDolares)


    return data #sRta


#endpoin de insert de tipo de accion nueva
#endpoint con tipo de parametro
@app.get("/alta/{item_id}")
async def read_item(item_id: str):
    sRta = "ok"
    print ("------------------------")
    bState = dbConnect.NuevaAccion (conex)
    if (bState == True): sRta = "ok"
    else: sRta = "Fault"
    return sRta

#endpoint con tipo de parametro
@app.get("/items3/{item_id}")
async def read_item(item_id: str):
    print ("------------------------")
    sql = "select * FROM History limit " + item_id + " offset 10"
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
    return {"item_id": item_id}

print ("es una sarasa?")


if __name__ == '__main__':
    uvicorn.run(app, port=80, host='0.0.0.0')