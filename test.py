import requests
import json

# URL de tu API Flask
url = "http://127.0.0.1:5000/api/ws_leads"

# Crear un diccionario con datos de ejemplo (todos los campos establecidos como None)
lead_data = {
    "idTimeStamp": None,
    "IdUnico": None,
    "FECHA_ENTRADA": None,
    "duplicado": None,
    "cargado": None,
    "fecha_carga": None,
    "cod_proveedor": None,
    "id": None,
    "campana": None,
    "fecha_captacion": None,
    "nombre": None,
    "ape1": None,
    "ape2": None,
    "telefono": None,
    "telefonoMD5": None,
    "email": None,
    "acepta1": None,
    "acepta2": None,
    "acepta3": None,
    "num1": None,
    "num2": None,
    "num3": None,
    "dual1": None,
    "dual2": None,
    "dual3": None,
    "variable1": None,
    "variable2": None,
    "variable3": None,
    "memo": None,
    "fecha": None,
    "hora": None,
    "foto1": None,
    "foto2": None,
    "comercial": None,
    "centro": None,
    "codigo_postal": None,
    "direccion": None,
    "poblacion": None,
    "provincia": None,
    "nif": None
}

# Establecer el encabezado Content-Type como 'application/json'
headers = {'Content-Type': 'application/json'}

# Enviar la solicitud POST a la API con el encabezado correcto
response = requests.post(url, json=lead_data, headers=headers)

# Imprimir la respuesta
print("Respuesta de la API:")
print(f"Estado: {response.status_code}")
print("Contenido:")
print(response.json())
