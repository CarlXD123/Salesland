from flask import Flask, jsonify, request
from datetime import datetime
from cryptography.fernet import Fernet
import json
import traceback
from uuid import uuid4
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from models import WS_LEADS, WS_LEADS_DISOCIADOS, AUX_CAMPANAS, AUX_DISOCIAR, AUX_PROVEEDORES

# API FLASK
app = Flask(__name__)

# CONECTAR A LA BASE DE DATOS SQL SERVER
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:ingeniero789@DESKTOP-R9GQV7R/Salesland?driver=SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# La clave de encriptación (deberías manejar esto de forma segura en un entorno real)
clave_encriptacion = Fernet.generate_key()
cipher_suite = Fernet(clave_encriptacion)

# Función para encriptar datos
def encriptar_lead_data(data):
    json_data = json.dumps(data)
    encrypted_data = cipher_suite.encrypt(json_data.encode())
    return encrypted_data

# Función para desencriptar datos
def desencriptar_lead_data(encrypted_data):
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    json_data = json.loads(decrypted_data.decode())
    return json_data

def es_formato_fecha_valido(fecha_str):
    formato_esperado = "%Y-%m-%d %H:%M:%S.000"
    try:
        fecha_obj = datetime.strptime(fecha_str, formato_esperado)
        return True
    except ValueError:
        return False

# RUTAS
# api para hola mundo
@app.route('/api/hola', methods=['GET'])
def hola():
    return jsonify({'mensaje': 'Hola, mundo!'})


#Api ws_leads
# API para WS_LEADS
@app.route('/api/ws_leads', methods=['POST'])
def insertar_lead():
    try:
        # Obtén los datos del JSON de la solicitud
        datos_lead = request.json

        # Crea una instancia del modelo WS_LEADS
        nuevo_lead = WS_LEADS(**datos_lead)

        # Agrega el nuevo lead a la sesión y realiza la commit
        db.session.add(nuevo_lead)
        db.session.commit()

        return jsonify({'status': 'ok', 'message': 'Lead insertado correctamente'})

    except SQLAlchemyError as e:
        return jsonify({'status': 'error', 'message': str(e), 'traceback': traceback.format_exc()}), 500

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e), 'traceback': traceback.format_exc()}), 500


# api para procesar los leads
@app.route('/api/procesar_leads', methods=['POST'])
def procesar_leads():
    try:
        leads_pendientes = WS_LEADS.query.filter_by(procesado=False).all()

        for lead in leads_pendientes:
            # Lógica de encriptación (ajusta según tus necesidades)
            lead_data_encriptado = encriptar_lead_data(lead.to_dict())

            # Mover el lead a otra tabla (WS_LEADS_DISOCIADOS en este caso)
            nuevo_lead_disociado = WS_LEADS_DISOCIADOS(**lead_data_encriptado)
            db.session.add(nuevo_lead_disociado)
            db.session.commit()

            # Eliminar el lead original de la tabla WS_LEADS
            db.session.delete(lead)
            db.session.commit()

        return jsonify({'status': 'ok', 'message': 'Leads procesados correctamente'})

    except ValueError as ve:
        return jsonify({'status': 'error', 'message': str(ve)}), 400  # Bad Request

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
    

#Api aux_campanas
@app.route('/api/aux_campanas', methods=['POST'])
def recibir_campana():
    try:
        campana_data = request.json

        # Generar un UUID único para la columna IDENT
        campana_data['IDENT'] = str(uuid4())

        # Construir dinámicamente el objeto AUX_CAMPANAS
        campana_dict = {
            key: campana_data.get(key) if key in campana_data else None
            for key in AUX_CAMPANAS.__table__.columns.keys()
        }

        nuevo_campana = AUX_CAMPANAS(**campana_dict)

        db.session.add(nuevo_campana)
        db.session.commit()

        return jsonify({'status': 'ok', 'message': 'Campaña recibida y guardada correctamente'})

    except SQLAlchemyError as e:
        return jsonify({'status': 'error', 'message': str(e), 'traceback': traceback.format_exc()}), 500

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e), 'traceback': traceback.format_exc()}), 500


#Api aux_disociar
@app.route('/api/aux_disociar', methods=['POST'])
def insertar_registro():
    try:
        # Obtén los datos del JSON de la solicitud
        datos_registro = request.json

        # Crea una instancia del modelo AUX_DISOCIAR
        nuevo_registro = AUX_DISOCIAR(campo=datos_registro['campo'])

        # Agrega el nuevo registro a la sesión y realiza la commit
        db.session.add(nuevo_registro)
        db.session.commit()

        return jsonify({'status': 'ok', 'message': 'Registro insertado correctamente'})

    except SQLAlchemyError as e:
        return jsonify({'status': 'error', 'message': str(e), 'traceback': traceback.format_exc()}), 500

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e), 'traceback': traceback.format_exc()}), 500


# Ruta para insertar un nuevo proveedor en AUX_PROVEEDORES
@app.route('/api/aux_proveedores', methods=['POST'])
def insertar_proveedor():
    try:
        # Obtén los datos del JSON de la solicitud
        datos_proveedor = request.json

        # Crea una instancia del modelo AUX_PROVEEDORES
        nuevo_proveedor = AUX_PROVEEDORES(
            cod_proveedor=datos_proveedor['cod_proveedor'],
            proveedor=datos_proveedor['proveedor']
        )

        # Agrega el nuevo proveedor a la sesión y realiza la commit
        db.session.add(nuevo_proveedor)
        db.session.commit()

        return jsonify({'status': 'ok', 'message': 'Proveedor insertado correctamente'})

    except SQLAlchemyError as e:
        return jsonify({'status': 'error', 'message': str(e), 'traceback': traceback.format_exc()}), 500

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e), 'traceback': traceback.format_exc()}), 500



# INICIAR LA APP
if __name__ == '__main__':
    app.run(debug=True)
