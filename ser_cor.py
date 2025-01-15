
# https://royportas.com/posts/cors-python/
import urllib3
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
from json import dumps

def lee_val_dolar ():
    print ("iniciando lee_val_dolar")
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
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

#--------------------------------------------------------

""" The HTTP request handler """
class RequestHandler(BaseHTTPRequestHandler):

  def _send_cors_headers(self):
      """ Sets headers required for CORS """
      self.send_header("Access-Control-Allow-Origin", "*")
      self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
      self.send_header("Access-Control-Allow-Headers", "x-api-key,Content-Type")

  def send_dict_response(self, d):
      """ Sends a dictionary (JSON) back to the client """
      self.wfile.write(bytes(dumps(d), "utf8"))

  def do_OPTIONS(self):
      self.send_response(200)
      self._send_cors_headers()
      self.end_headers()

  def do_GET(self):
      self.send_response(200)
      self._send_cors_headers()
      self.end_headers()

      iDolar = lee_val_dolar ()
      print ("dolar: ", iDolar)
      iMola = 680
      iMsft = 500
      iBma = 3100
      iAdgo = 120
      iAlua = 1850
      iGgal = 560
      data = []
#      data['Valor Dolar'] = iDolar
      data.append ({'id': 0, 'dolar': iDolar})
#      data['Total Pesos'] = 0
    
#      data['Total Dolares'] = 0    
      iTotalDolares = 0
      iTotalPesos = 0
    #url = 'http://localhost:8080/health'
      url = 'https://es.investing.com/equities/adecoagro-sa-ar-chart'
#    sasa = lee_val (url)
      data = lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iAdgo, data, 'ADGO', 1)
#    iTotalPesos = iTotalPesos + sasa*iAdgo
#    iAdgoUsd = sasa*iAdgo/iDolar
#    iTotalDolares = iTotalDolares + iAdgoUsd
#    print (sasa*iAdgo, "en dolares:" ,  iAdgoUsd)
#    data['ADGO'] = str(iAdgoUsd)
      print ("data: ", data)

      url = 'https://es.investing.com/equities/molinos-agro-chart'
#    sasa = lee_val (url)
      data = lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iMola, data, 'MOLA', 2)
#    iTotalPesos = iTotalPesos + sasa*iMola
#    iMolaUsd = sasa*iMola/iDolar
#    iTotalDolares = iTotalDolares + iMolaUsd
#    print (sasa*iMola, "en dolares:" ,  iMolaUsd)
#    data['MOLA'] = str(iMolaUsd)

      url = 'https://es.investing.com/equities/aluar-chart'
#    sasa = lee_val (url)
      data = lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iAlua, data, 'ALUA', 3)
#    iTotalPesos = iTotalPesos + sasa*iAlua
#    iAluaUsd = sasa*iAlua/iDolar
#    iTotalDolares = iTotalDolares + iAluaUsd
#    print (sasa*iAlua, "en dolares:" ,  iAluaUsd)
#    data['ALUA'] = str(iAluaUsd)

      url = 'https://es.investing.com/equities/microsoft-corp-ar-chart'
#    sasa = lee_val (url)
      data = lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iMsft, data, 'MSFT', 4)
#    iTotalPesos = iTotalPesos + sasa*iMsft
#    iMsfUsd = sasa*iMsft/iDolar
#    iTotalDolares = iTotalDolares + iMsfUsd
#    print (sasa*iMsft, "en dolares:" ,  iMsfUsd)
#    data['MSFT'] = str(iMsfUsd)

      url = 'https://es.investing.com/equities/gp-fin-galicia-chart'
#    sasa = lee_val (url)
      data = lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iGgal, data, 'GGAL', 5)
#    iTotalPesos = iTotalPesos + sasa*iGgal
#    iGgalUsd = sasa*iGgal/iDolar
#    iTotalDolares = iTotalDolares + iGgalUsd
#    print (sasa*iGgal, "en dolares:" ,  iGgalUsd)
#    data['GGAL'] = str(iGgalUsd)

      url = 'https://es.investing.com/equities/macro-chart'
#    sasa = lee_val (url)
      data = lee_val_2 (url, iTotalPesos, iTotalDolares, iDolar, iBma, data, 'BMA', 6)
#    iTotalPesos = iTotalPesos + sasa*iBma
#    iBmaUsd = sasa*iBma/iDolar
#    iTotalDolares = iTotalDolares + iBmaUsd
#    print (sasa*iBma, "en dolares:" ,  iBmaUsd)
#    data['BMA'] = str(iBmaUsd)

#      print ("Total Pesos: ", iTotalPesos)
#      print ("Total Dolares: ", iTotalDolares)
#      sRta = "Total Pesos: " + str(iTotalPesos) + "Total Dolares: " + str(iTotalDolares)

      response = {}
      response = data
      self.send_dict_response(response)

  def do_POST(self):
      self.send_response(200)
      self._send_cors_headers()
      self.send_header("Content-Type", "application/json")
      self.end_headers()

      dataLength = int(self.headers["Content-Length"])
      data = self.rfile.read(dataLength)

      print(data)

      response = {}
      response["status"] = "OK"
      self.send_dict_response(response)


print("Starting server")
httpd = HTTPServer(("127.0.0.1", 8000), RequestHandler)
print("Hosting server on port 8000")
httpd.serve_forever()