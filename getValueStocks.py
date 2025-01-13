#!/usr/bin/python
# -*- coding: utf-8 -*-
#para resolverf el problema de certificados usar:
#pip install pip-system-certs
# pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org pip-system-certs
#pip install flask
#pip install curl_cffi
from flask import Flask, render_template, flash, redirect, request, \
    jsonify


from datetime import datetime 
#incorpora la lib curl_cffi en lugar de la requests para ver de solucionar el tema de filtrado de Web Scraping
#import requests
from curl_cffi import requests
#import urllib3

import json
import os
# importo el cliente de kubernetes y los objetos de configuracion

def lee_val_dolar ():
    print ("iniciando lee_val_dolar")
#    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = requests.get("https://www.lanacion.com.ar/", verify=False)
    print ("res: " , res)
#    print ("post request.get")
#    print(res)
#    print(res.status_code)
#print(res.text)
#fastapi
    f = open ('lna.txt','w',encoding='utf-8')
    f.write(res.text)
    f.close()

# demonstrate readlines()
# Using readlines()
    file1 = open('lna.txt', 'r',encoding='utf-8')
    Lines = file1.readlines()
    iRta = 0
#    print ("Valor de " + url [url.rfind ('/')+1 :])

    for line in Lines:
        iFirstTag = line.find('Dólar blue')
#        print ("primer posicion: ", iFirstTag)
        iSecondTag = line.find ('Dólar blue', iFirstTag+1)
#        print ("segunda posiscion: ", iSecondTag)
        if (iSecondTag) > 0 :
#            print ("iFirstTag: " , iFirstTag)
#	    print(line.strip())
            iStartValue = line.find('>', iSecondTag)
#            print (iStartValue)
            iEndValue = line.find(',',iStartValue)
#            print (line[iStartValue+3 : iEndValue])
            iRta = int(float(line [iStartValue+3 : iEndValue].replace('.','')))
    return iRta

#--------------------------------------------------------
def lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iQuantity ,data, sEspecie):
    print ("INICIANDO: lee_val_2")
    campos = {}
    res = requests.get(url, 
                        impersonate="safari_ios")
    print ("res: " , res)
    f = open ('rta.txt','w',encoding='utf-8')
    f.write(res.text)
    f.close()
    file1 = open('rta.txt', 'r',encoding='utf-8')
    Lines = file1.readlines()
    iRta = 0
    for line in Lines:
        iFirstTag = line.find('instrument-price-last')
        if (iFirstTag) > 0 :
            iStartValue = line.find('>', iFirstTag)
            iEndValue = line.find(',',iStartValue)
            iAccionValue = int(float(line [iStartValue+1 : iEndValue].replace('.','')))
    data['Total Pesos'] = data['Total Pesos'] + iAccionValue * iQuantity
    iValueUsd = iAccionValue * iQuantity /iDolar
    data['Total Dolares'] = data['Total Dolares'] + iValueUsd
    campos ['cantidad'] = iQuantity
    campos ['dolares'] = iValueUsd
    campos ['pesos'] = iAccionValue * iQuantity
    campos ['valor accion'] = iAccionValue
    #data[sEspecie] = str(iValueUsd)
    data[sEspecie] = campos
#    data['Total Pesos'] = iTotalPesos
#    data['Total Dolares'] = iTotalDolares
    print ("DATA: ", data)
    return data

#--------------------------------------------------------

application = Flask(__name__)

### end swagger specific ###
@application.route('/health')
def health():
    """
    healthckeck para readiness
    del pod
    """
    return 'OK papa'
######ENDPOINT apps.openshift.io

@application.route('/getvalues')
def getvalues():
    """
    healthckeck para readiness
    del pod
    """
    print ("iniciando")
    
    iDolar = lee_val_dolar ()
    print ("dolar: ", iDolar)
    iMola = 680
    iMsft = 610
    iBma = 3200
    iAdgo = 120
    iAlua = 1850
    iGgal = 560
    data = {}
    data['Valor Dolar'] = iDolar
    data['Total Pesos'] = 0
    
    data['Total Dolares'] = 0    
    iTotalDolares = 0
    iTotalPesos = 0
    #url = 'http://localhost:8080/health'
    url = 'https://es.investing.com/equities/adecoagro-sa-ar-chart'
#    sasa = lee_val (url)
    data = lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iAdgo, data, 'ADGO')
#    iTotalPesos = iTotalPesos + sasa*iAdgo
#    iAdgoUsd = sasa*iAdgo/iDolar
#    iTotalDolares = iTotalDolares + iAdgoUsd
#    print (sasa*iAdgo, "en dolares:" ,  iAdgoUsd)
#    data['ADGO'] = str(iAdgoUsd)
    print ("data: ", data)

    url = 'https://es.investing.com/equities/molinos-agro-chart'
#    sasa = lee_val (url)
    data = lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iMola, data, 'MOLA')
#    iTotalPesos = iTotalPesos + sasa*iMola
#    iMolaUsd = sasa*iMola/iDolar
#    iTotalDolares = iTotalDolares + iMolaUsd
#    print (sasa*iMola, "en dolares:" ,  iMolaUsd)
#    data['MOLA'] = str(iMolaUsd)

    url = 'https://es.investing.com/equities/aluar-chart'
#    sasa = lee_val (url)
    data = lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iAlua, data, 'ALUA')
#    iTotalPesos = iTotalPesos + sasa*iAlua
#    iAluaUsd = sasa*iAlua/iDolar
#    iTotalDolares = iTotalDolares + iAluaUsd
#    print (sasa*iAlua, "en dolares:" ,  iAluaUsd)
#    data['ALUA'] = str(iAluaUsd)

    url = 'https://es.investing.com/equities/microsoft-corp-ar-chart'
#    sasa = lee_val (url)
    data = lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iMsft, data, 'MSFT')
#    iTotalPesos = iTotalPesos + sasa*iMsft
#    iMsfUsd = sasa*iMsft/iDolar
#    iTotalDolares = iTotalDolares + iMsfUsd
#    print (sasa*iMsft, "en dolares:" ,  iMsfUsd)
#    data['MSFT'] = str(iMsfUsd)

    url = 'https://es.investing.com/equities/gp-fin-galicia-chart'
#    sasa = lee_val (url)
    data = lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iGgal, data, 'GGAL')
#    iTotalPesos = iTotalPesos + sasa*iGgal
#    iGgalUsd = sasa*iGgal/iDolar
#    iTotalDolares = iTotalDolares + iGgalUsd
#    print (sasa*iGgal, "en dolares:" ,  iGgalUsd)
#    data['GGAL'] = str(iGgalUsd)

    url = 'https://es.investing.com/equities/macro-chart'
#    sasa = lee_val (url)
    data = lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iBma, data, 'BMA')
#    iTotalPesos = iTotalPesos + sasa*iBma
#    iBmaUsd = sasa*iBma/iDolar
#    iTotalDolares = iTotalDolares + iBmaUsd
#    print (sasa*iBma, "en dolares:" ,  iBmaUsd)
#    data['BMA'] = str(iBmaUsd)

    print ("Total Pesos: ", iTotalPesos)
    print ("Total Dolares: ", iTotalDolares)
    sRta = "Total Pesos: " + str(iTotalPesos) + "Total Dolares: " + str(iTotalDolares)
#    data['Total Pesos'] = str(iTotalPesos)
#    data['Total Dolares'] = str(iTotalDolares)


    return data #sRta

#------------------------------------------
@application.route('/')
def index():
    return render_template('index.html')
    
    # Flask development
if __name__ == '__main__':
   application.run(port = 8000, host = '0.0.0.0', debug = True)