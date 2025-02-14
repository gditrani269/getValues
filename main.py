# main.py
#ejecutar con:
#uvicorn main:app --host 0.0.0.0 --port 80  --reload
#pip3 install fastapi
#pip3 install "uvicorn[standard]" && \
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    data = investing.lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iAdgo, data, 'ADGO')
    print ("data: ", data)

    url = 'https://es.investing.com/equities/molinos-agro-chart'
    data = investing.lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iMola, data, 'MOLA')

    url = 'https://es.investing.com/equities/aluar-chart'
    data = investing.lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iAlua, data, 'ALUA')

    url = 'https://es.investing.com/equities/microsoft-corp-ar-chart'
    data = investing.lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iMsft, data, 'MSFT')

    url = 'https://es.investing.com/equities/gp-fin-galicia-chart'
    data = investing.lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iGgal, data, 'GGAL')

    url = 'https://es.investing.com/equities/macro-chart'
    data = investing.lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iBma, data, 'BMA')

    url = 'https://es.investing.com/equities/tran-gas-del-s'
    data = investing.lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, TGSU2, data, 'TGSU2')

    print ("Total Pesos: ", iTotalPesos)
    print ("Total Dolares: ", iTotalDolares)
    sRta = "Total Pesos: " + str(iTotalPesos) + "Total Dolares: " + str(iTotalDolares)
#    data['Total Pesos'] = str(iTotalPesos)
#    data['Total Dolares'] = str(iTotalDolares)


    return data #sRta

#endpoin de insert de tipo de accion nueva
#Ej: http://127.0.0.1:8081/alta/?especie=BMA&url=https://es.investing.com/equities/macro-chart&cantidad=3200
@app.get("/alta/")
async def read_item(especie: str, url: str, cantidad: int):
    sRta = "ok alta"
    print ("------------------------")
    bState = dbConnect.NuevaAccion (conex, especie, url, cantidad)
    if (bState == True): sRta = "ok"
    else: sRta = "Fault alta"
    return sRta

#endpoint de actualizacion de cantidad de un tipo de accion
#Ej: http://127.0.0.1:8081/update/?especie=BMA&cantidad=330
@app.get("/update/")
async def read_item(especie: str, cantidad: int):
    sRta = "ok update"
    print ("------------------------")
    bState = dbConnect.UpdateCantidadAcciones (conex, especie, cantidad)
    if (bState == True): sRta = "ok"
    else: sRta = "Fault update"
    return sRta

#endpoint que muestra el estado actual de todas las inversiones
#Ej: http://127.0.0.1:8081/state/
@app.get("/state/")
async def read_item():
    iDolar = mylibs.lee_val_dolar ()
    bRta = dbConnect.State (conex, iDolar)

    return bRta

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


@app.get("/nada")
def read_root():
    iDolar = mylibs.lee_val_dolar ()
    bRta = dbConnect.State_new (conex, iDolar)
    return (bRta)

@app.get("/history/{accion}")
async def read_item(accion: str):
    print ("Es el endpoint History")
    print ("------------------------")

    bRta = dbConnect.History (conex, accion)
    return (bRta)

print ("es una sarasa?")


if __name__ == '__main__':
    uvicorn.run(app, port=80, host='0.0.0.0')