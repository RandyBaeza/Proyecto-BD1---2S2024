from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from ConectarBD import MssqlConnection

app = Flask(__name__)

app.secret_key = '0000'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login_empleado', methods=['POST'])
def login_empleado():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    try:
        db = MssqlConnection()
        usuario = db.login(username, password)
        if usuario[0][0] == 0 or usuario[0][0] == 1 :
            userId = usuario[0][1]
            admin = usuario[0][0]
            return jsonify({'success': True, 'userId': userId, 'admin': admin })
        else:
            return jsonify({'success': False, 'message': 'Nombre o contrasena incorrectos'}), 401
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
    
@app.route('/logout_empleado', methods=['POST'])
def logout_empleado():
    data = request.get_json()
    userId = data.get('userId')
    return jsonify({'success': True, 'userId': userId})

#@app.route('/index/<int:userId>/', defaults={'buscar': ''})
@app.route('/index/<int:userId>/<int:admin>')
def index(userId, admin):
    return render_template('index.html', userId=userId, admin=admin) 

@app.route('/listar_empleados/<int:userId>/<buscar>', methods=['GET'])
@app.route('/listar_empleados/<int:userId>/', defaults={'buscar': ''}, methods=['GET'])
def listar_empleados(userId, buscar):
    try:
        db = MssqlConnection()
        empleados = db.listarTarjetas(userId, buscar=str(buscar))
        if empleados == 50008:  # Error en la BD
            raise Exception("Lista de empleados no disponible")
        return jsonify(empleados)
    except Exception as e:
        print(f"Error al listar empleados: {e}")
        return jsonify({'error': str(e)}), 500  # Devuelve un código de error adecuado
    
@app.route('/consultar/<int:userId>/<int:idTF>/<string:TipoTC>')
def consultar(userId, idTF, TipoTC):
    return render_template('consultar.html', userId=userId, idTF=idTF, TipoTC=TipoTC)

@app.route('/consultarsub/<int:userId>/<int:idTF>/<string:TipoTC>')
def consultarsub(userId, idTF, TipoTC):
    return render_template('consultarsub.html', userId=userId, idTF=idTF, TipoTC=TipoTC)

@app.route('/listar_EC/<int:userId>/<int:idTF>/<string:TipoTCM>')
def consultarEC(userId, idTF, TipoTCM):
    try:
        db = MssqlConnection()
        empleados = db.consultarEC(idTF) 
        if empleados == 50008:  # Error en la BD
            raise Exception("Lista de empleados no disponible")
        return jsonify(empleados)
    except Exception as e:
        print(f"Error al listar empleados: {e}")
        return jsonify({'error': str(e)}), 500  # Devuelve un código de error adecuado

@app.route('/listar_SEC/<int:userId>/<int:idTF>/<string:TipoTCM>')
def consultarSEC(userId, idTF, TipoTCM):
    try:
        db = MssqlConnection()
        empleados = db.consultarSEC(idTF) 
        if empleados == 50008:  # Error en la BD
            raise Exception("Lista de empleados no disponible")
        return jsonify(empleados)
    except Exception as e:
        print(f"Error al listar empleados: {e}")
        return jsonify({'error': str(e)}), 500  # Devuelve un código de error adecuado



@app.route('/movimientos/<int:idEC>/<string:TipoTCM>')
def movimientos(idEC, TipoTCM):
    return render_template('movimientos.html', idEC=idEC, TipoTCM=TipoTCM) 

    

@app.route('/listar_movimientos/<int:idEC>/<string:TipoTCM>')
def listar_movimientos(idEC, TipoTCM):
    try:
        db = MssqlConnection()
        movimientos = db.listarMovimientos(idEC, TipoTCM)
        
        print(idEC, TipoTCM)
        # Si se encontraron movimientos, los retornamos
        if movimientos and len(movimientos) > 0:
            return jsonify({'success': True, 'movimientos': movimientos})
        else:
            # Si no hay movimientos, retornar success: false y un arreglo vacío
            return jsonify({'success': False, 'movimientos': []}), 200
    except Exception as e:
        print(f"Error al listar movimientos: {e}")
        return jsonify({'error': str(e)}), 500  # Devuelve un código de error adecuado



if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0')
