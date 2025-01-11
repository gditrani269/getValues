
#api de prueba que publica en 8000 y se conecta a una DB en otro pod y muestra el resultado
# https://royportas.com/posts/cors-python/
import urllib3
import requests
import mysql.connector
from http.server import BaseHTTPRequestHandler, HTTPServer
from json import dumps

def lee_val_dolar ():

    return "lee_val_dolar"

def fPaginado ():
    dbConnect2 = {
    #    'host':'172.28.183.229',
        'host':'192.168.1.113',
        'user':'root',
        'password':'sasa1234',
    #    'database':'retest',
        'database':'options',
    }
    print ("funcion de paginado")
    conex = mysql.connector.connect(**dbConnect2)

    cursor = conex.cursor()
    sql = "select * FROM History limit 10 offset 10"
    cursor.execute(sql)
    results = cursor.fetchall ()
    print(results)
    print ("sgunda pagina")
    sql = "select * FROM History limit 10 offset 20"
    cursor.execute(sql)
    results = cursor.fetchall ()
    print(results)

    print ("otra prueba db")
    return results


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

      print ("SALIDA")
      print (fPaginado())
      response = []
      print ("SALIDA2")
      response.append (fPaginado())
      print ("SALIDA3")
      print (response)
      print ("SALIDA4")
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