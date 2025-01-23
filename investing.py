from curl_cffi import requests

def lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iQuantity ,data, sEspecie, id):
    print ("INICIANDO: lee_val_2")
    campos = {}
    res = requests.get(url, 
                        headers={
                                    'Cookie': '__cf_bm=eRJ5DZoNfXN9BzXj3CPNvQ9uKxS8RQJAkpXKKtvpNyE-1732204634-1.0.1.1-T_ixq9emHgYhXpZocl2OEkIInKAY7Gue85n5vUNIpbMJAyE8ryfV4Fdwfu0D.U1TGpPGk3Cb2T8ZfbJMvQ_5TR2LNSzAWir8Q_JaAShKFQg; firstUdid=0; gcc=AR; gsc=B; smd=9df700a45e60c4519de82a459c584107-1732204001; udid=9df700a45e60c4519de82a459c584107; __cflb=0H28vFEFimnpowq71CdWzBFhnnYdQ9pspJoKbqEFS9r',
                                    'User-Agent': 'Mozilla/5.0'
                                }
                        , verify=None)
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
#    data['Total Pesos'] = data['Total Pesos'] + iAccionValue * iQuantity
    iValueUsd = round (iAccionValue * iQuantity /iDolar, 2)
#    data['Total Dolares'] = data['Total Dolares'] + iValueUsd
    campos ['id'] = id
    campos ['Cantidad'] = iQuantity
    campos ['Saldo_dolares'] = iValueUsd
    campos ['Saldo_pesos'] = iAccionValue * iQuantity
    campos ['valor'] = iAccionValue
    campos ['accion'] = sEspecie
    #data[sEspecie] = str(iValueUsd)
#    data[sEspecie] = campos
#    data['Total Pesos'] = iTotalPesos
#    data.append ({'id': 0, 'Total Pesos': iTotalPesos})
#    data['Total Dolares'] = iTotalDolares
    data.append (campos)
    print ("DATA: ", data)
#    print ("campos: ", campos)
    return data
