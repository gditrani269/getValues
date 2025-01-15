
#api de prueba que publica en 8000 y se conecta a una DB en otro pod y muestra el resultado
# https://royportas.com/posts/cors-python/

#ejecutar con:
#python3.11 api-db.py

#pip install mysql-connector-python

#import urllib3
#import requests

import mysql.connector
import re
from http.server import BaseHTTPRequestHandler, HTTPServer
from json import dumps

from urllib.parse import urlparse, parse_qs


def lee_val_dolar ():

    return "lee_val_dolar"

def fPaginado ():
    dbConnect2 = {
        'host':'172.28.183.229',
    #    'host':'192.168.1.113',
        'user':'root',
        'password':'sasa1234',
    #    'database':'retest',
        'database':'options',
    }
    print ("funcion de paginado")
    conex = mysql.connector.connect(**dbConnect2)
    cursor = conex.cursor()
    sql = "select * FROM History limit 10 offset 20"
    results = {}
    data = []
    iIndex = 0
    cursor.execute(sql)
    for (sql) in cursor:
#        print ("\n", sql[0], sql[1], sql[2], sql[3], sql[4], sql[5])
        results [iIndex] = sql[0], str(sql[1]), float(sql[2]), float(sql[3]), float(sql[4]), float(sql[5])
#        print ("\nresults:" , results)
        iIndex = iIndex + 1

    data.append (results)
    print ("FIN otra prueba db")
    return data


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
      print ("-------------------INICIO------------------------------------")
      print ("SALIDA")
      print ("self: ", self)
      print ("self.path: ", self.path)
      print ("re.search ", re.search)
      if re.search('/sasa', self.path):
        print ("ca toy papa")

#      print (fPaginado())
      data = []
#      data['Valor Dolar'] = iDolar
      iDolar = 8
#      data.append ({'id': 0, 'dolar': iDolar})
      data = fPaginado()
      print (data)
      print ("SALIDA4")
      print ("-------------------FIN------------------------------------")
      self.send_dict_response(data)

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
httpd = HTTPServer(("0.0.0.0", 8000), RequestHandler)
print("Hosting server on port 8000")
httpd.serve_forever()