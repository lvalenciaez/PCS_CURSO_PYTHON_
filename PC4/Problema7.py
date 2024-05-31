"""import requests
import sqlite3

def get_data():
    url"""

import requests
import sqlite3
from datetime import datetime, timedelta

def obtener_tipo_cambio(fecha):
    url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?fecha={fecha}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['compra'], data['venta']
    else:
        return None, None

def almacenar_datos_en_db(datos):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sunat_info (
            fecha TEXT,
            compra REAL,
            venta REAL
        )
    ''')
    cursor.executemany('''
        INSERT INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)
    ''', datos)
    conn.commit()
    conn.close()

def mostrar_contenido_tabla():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sunat_info')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

def main():
    
    fecha_inicio = datetime(2023, 1, 1)
    fecha_fin = datetime(2023, 12, 31)
    delta = timedelta(days=1)
    datos = []

    while fecha_inicio <= fecha_fin:
        fecha_str = fecha_inicio.strftime('%Y-%m-%d')
        compra, venta = obtener_tipo_cambio(fecha_str)
        if compra is not None and venta is not None:
            datos.append((fecha_str, compra, venta))
        fecha_inicio += delta

    
    almacenar_datos_en_db(datos)


    mostrar_contenido_tabla()

if __name__ == "__main__":
    main()
