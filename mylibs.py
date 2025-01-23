from curl_cffi import requests

def lee_val_dolar ():
    print ("iniciando mylibs.lee_val_dolar")
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