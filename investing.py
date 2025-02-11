from curl_cffi import requests
from os import remove

def lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iQuantity ,data, sEspecie):
    print ("INICIANDO: lee_val_2")
    campos = {}
    res = requests.get(url, impersonate="safari_ios", verify=False)
    print ("res: " , res)
    f = open ('rta.txt','w',encoding='utf-8')
    f.write(res.text)
    f.close()
    file1 = open('rta.txt', 'r',encoding='utf-8')
    Lines = file1.readlines()
    remove("rta.txt")
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

def lee_val_new (url, iDolar, iQuantity, sEspecie, iIndex):
    print ("INICIANDO: lee_val_new")
    campos = {}
    res = requests.get(url, impersonate="safari_ios", verify=False)
    print ("res: " , res)
    f = open ('rta.txt','w',encoding='utf-8')
    f.write(res.text)
    f.close()
    file1 = open('rta.txt', 'r',encoding='utf-8')
    Lines = file1.readlines()
    remove("rta.txt")
    for line in Lines:
        iFirstTag = line.find('instrument-price-last')
        if (iFirstTag) > 0 :
            iStartValue = line.find('>', iFirstTag)
            iEndValue = line.find(',',iStartValue)
            iAccionValue = int(float(line [iStartValue+1 : iEndValue].replace('.','')))

    campos = {
        "id": iIndex,
        "accion": sEspecie,
        "valor": iAccionValue,
        "Saldo_pesos": iAccionValue * iQuantity,
        "Saldo_dolares": iAccionValue * iQuantity / iDolar
    }
    return campos