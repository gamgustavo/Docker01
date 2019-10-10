from typing import List, Dict
from flask import Flask
import mysql.connector
import json
import jwt
from flask import request
from flask import Response

app = Flask(__name__)
public_key = ''
f=open("public.key", "r")
if f.mode == 'r':
    public_key =f.read()


def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError as e:
    return False
  return True

def favorite_colors() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'knights'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM favorite_colors')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()
    return results


@app.route('/')
def index() -> str:
    return json.dumps({'favorite_colors': favorite_colors()})


@app.route('/post/complemento', methods=['POST'])
def post_complemento():
    if request.method == 'POST':
        if is_json(str(request.data)):
            return Response('Content-type must be application/json', status=401, mimetype='application/json')
        data = request.get_json()
        # validacion parametro nombre
        nombre = data.get('nombre')
        if not nombre:
            return  Response(json.dumps({'estado':'401','mensaje':'Parametro nombre faltante'}), status=401, mimetype='application/json')
        # validacion parametro correo
        correo = data.get('correo')
        if not correo:
            return  Response(json.dumps({'estado':'401','mensaje':'Parametro correo faltante'}), status=401, mimetype='application/json')
        # validacion parametro token
        token = data.get('token')
        if not token:
            return  Response(json.dumps({'estado':'401','mensaje':'Parametro token faltante'}), status=401, mimetype='application/json')
        try:
            jwt.decode(token,   verify=False)
        except:
            return Response(json.dumps({'estado':'401','mensaje':'token invalido'}), status=401, mimetype='application/json')
        try:
            jwt.decode(token,   verify=False)
        except jwt.ExpiredSignatureError:
            return Response(json.dumps({'estado':'401','mensaje':'Parametro Expiro Token'}), status=401, mimetype='application/json')
        # validacion parametro complemento
        complemento = data.get('complemento')
        if not complemento:
            return  Response(json.dumps({'estado':'401','mensaje':'Parametro complemento faltante'}), status=401, mimetype='application/json')
        return complemento 


@app.route('/post/caracteres', methods=['POST'])
def post_caracteres():
    if request.method == 'POST':
        if is_json(str(request.data)):
            return Response('Content-type must be application/json', status=401, mimetype='application/json')
        data = request.get_json()
        # validacion parametro nombre
        nombre = data.get('nombre')
        if not nombre:
            return  Response(json.dumps({'estado':'401','mensaje':'Parametro nombre faltante'}), status=401, mimetype='application/json')
        # validacion parametro correo
        correo = data.get('correo')
        if not correo:
            return  Response(json.dumps({'estado':'401','mensaje':'Parametro correo faltante'}), status=401, mimetype='application/json')
        # validacion parametro token
        token = data.get('token')
        if not token:
            return  Response(json.dumps({'estado':'401','mensaje':'Parametro token faltante'}), status=401, mimetype='application/json')
        try:
            jwt.decode(token,   verify=False)
        except:
            return Response(json.dumps({'estado':'401','mensaje':'token invalido'}), status=401, mimetype='application/json')
        try:
            jwt.decode(token,   verify=False)
        except jwt.ExpiredSignatureError:
            return Response(json.dumps({'estado':'401','mensaje':'Parametro Expiro Token'}), status=401, mimetype='application/json')
        # validacion parametro caracteres
        cadena = data.get('cadena')
        if not cadena:
            return  Response(json.dumps({'estado':'401','mensaje':'Parametro cadena faltante'}), status=401, mimetype='application/json')
        return cadena 


@app.route('/get/cadenaCaracteres', methods=['GET'])
def get_cadenaCaracteres():
    if request.method == 'GET':
        token = request.args.get('token')        
        if not token:
            return  Response(json.dumps({'estado':'401','mensaje':'Parametro token faltante'}), status=401, mimetype='application/json')
        try:
            jwt.decode(token,   verify=False)
        except:
            return Response(json.dumps({'estado':'401','mensaje':'token invalido'}), status=401, mimetype='application/json')
        try:
            jwt.decode(token,   verify=False)
        except jwt.ExpiredSignatureError:
            return Response(json.dumps({'estado':'401','mensaje':'Parametro Expiro Token'}), status=401, mimetype='application/json')
        ## Select todos los cadenaCaracteres

        return token


@app.route('/post/catalogo', methods=['POST'])
def post_catalogo():
    if request.method == 'POST':
        if is_json(str(request.data)):
            return Response('Content-type must be application/json', status=401, mimetype='application/json')
        data = request.get_json()
        # validacion parametro nombre
        nombre = data.get('nombre')
        if not nombre:
            return  Response(json.dumps({'estado':'401','mensaje':'Parametro nombre faltante'}), status=401, mimetype='application/json')
        # validacion parametro correo
        correo = data.get('correo')
        if not correo:
            return  Response(json.dumps({'estado':'401','mensaje':'Parametro correo faltante'}), status=401, mimetype='application/json')
        # validacion parametro token
        token = data.get('token')
        if not token:
            return  Response(json.dumps({'estado':'401','mensaje':'Parametro token faltante'}), status=401, mimetype='application/json')
        try:
            jwt.decode(token,   verify=False)
        except:
            return Response(json.dumps({'estado':'401','mensaje':'token invalido'}), status=401, mimetype='application/json')
        try:
            jwt.decode(token,   verify=False)
        except jwt.ExpiredSignatureError:
            return Response(json.dumps({'estado':'401','mensaje':'Parametro Expiro Token'}), status=401, mimetype='application/json')
        catalogo = data.get('catalogo')
        if not catalogo:
            return  Response(json.dumps({'estado':'401','mensaje':'Parametro catalogo faltante'}), status=401, mimetype='application/json')

        ## Agregar funcionamiento 
        return catalogo


@app.route('/get/catalogo', methods=['GET'])
def get_catalogo():
    if request.method == 'GET':
        token = request.args.get('token')        
        if not token:
            return  Response(json.dumps({'estado':'401','mensaje':'Parametro token faltante'}), status=401, mimetype='application/json')
        try:
            jwt.decode(token,   verify=False)
        except:
            return Response(json.dumps({'estado':'401','mensaje':'token invalido'}), status=401, mimetype='application/json')
        try:
            jwt.decode(token,   verify=False)
        except jwt.ExpiredSignatureError:
            return Response(json.dumps({'estado':'401','mensaje':'Parametro Expiro Token'}), status=401, mimetype='application/json')
        ## Select todos los catalogos

        return token

@app.route('/get/catalogo/<idComplemento>/<idCatalogo>', methods=['GET'])
def get_catalogo_param_param(idComplemento,idCatalogo):
    if request.method == 'GET':
        token = request.args.get('token')        
        if not token:
            return  Response(json.dumps({'estado':'401','mensaje':'Parametro token faltante'}), status=401, mimetype='application/json')
        try:
            jwt.decode(token,   verify=False)
        except:
            return Response(json.dumps({'estado':'401','mensaje':'token invalido'}), status=401, mimetype='application/json')
        try:
            jwt.decode(token,   verify=False)
        except jwt.ExpiredSignatureError:
            return Response(json.dumps({'estado':'401','mensaje':'Parametro Expiro Token'}), status=401, mimetype='application/json')

        ### Select para buscar dentro

        return idCatalogo

@app.route('/delete/catalogo/<idCatalogo>', methods=['DELETE'])
def delete_catalogo(idCatalogo):
    if request.method == 'DELETE':
        token = request.args.get('token')        
        if not token:
            return  Response(json.dumps({'estado':'401','mensaje':'Parametro token faltante'}), status=401, mimetype='application/json')
        try:
            jwt.decode(token,   verify=False)
        except:
            return Response(json.dumps({'estado':'401','mensaje':'token invalido'}), status=401, mimetype='application/json')
        try:
            jwt.decode(token,   verify=False)
        except jwt.ExpiredSignatureError:
            return Response(json.dumps({'estado':'401','mensaje':'Parametro Expiro Token'}), status=401, mimetype='application/json')
        ## agregar select Catalogo

        return idCatalogo



@app.route('/get/complemento/<idComplemento>', methods=['GET'])
def get_complemento(idComplemento):
    if request.method == 'GET':
        token = request.args.get('token')        
        if not token:
            return  Response(json.dumps({'estado':'401','mensaje':'Parametro token faltante'}), status=401, mimetype='application/json')
        try:
            jwt.decode(token,   verify=False)
        except:
            return Response(json.dumps({'estado':'401','mensaje':'token invalido'}), status=401, mimetype='application/json')
        try:
            jwt.decode(token,   verify=False)
        except jwt.ExpiredSignatureError:
            return Response(json.dumps({'estado':'401','mensaje':'Parametro Expiro Token'}), status=401, mimetype='application/json')

        ## agregar delete complemento

        return idComplemento

        


@app.route('/delete/complemento/<idComplemento>', methods=['DELETE'])
def delete_complemento(idComplemento):
    if request.method == 'DELETE':
        token = request.args.get('token')        
        if not token:
            return  Response(json.dumps({'estado':'401','mensaje':'Parametro token faltante'}), status=401, mimetype='application/json')
        try:
            jwt.decode(token,   verify=False)
        except:
            return Response(json.dumps({'estado':'401','mensaje':'token invalido'}), status=401, mimetype='application/json')
        try:
            jwt.decode(token,   verify=False)
        except jwt.ExpiredSignatureError:
            return Response(json.dumps({'estado':'401','mensaje':'Parametro Expiro Token'}), status=401, mimetype='application/json')
        ## agregar select complemento

        return idComplemento



@app.route('/get/complementos', methods=['GET'])
def get_complementos():
    if request.method == 'GET':
        token = request.args.get('token')
        if not token:
            return  Response(json.dumps({'estado':'401','mensaje':'Parametro token faltante'}), status=401, mimetype='application/json')
        #### validacion de token
        try:
            jwt.decode(token,   verify=False)
        except:
            return Response(json.dumps({'estado':'401','mensaje':'token invalido'}), status=401, mimetype='application/json')
        try:
            jwt.decode(token,   verify=False)
        except jwt.ExpiredSignatureError:
            return Response(json.dumps({'estado':'401','mensaje':'Parametro Expiro Token'}), status=401, mimetype='application/json')
        decoded = jwt.decode(token,  verify=False)
        #### realizar select
        return decoded






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)