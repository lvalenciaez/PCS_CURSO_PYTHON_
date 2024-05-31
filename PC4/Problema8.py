import requests
import sqlite3
from datetime import datetime

def obtener_precio_bitcoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        usd = data['bpi']['USD']['rate_float']
        gbp = data['bpi']['GBP']['rate_float']
        eur = data['bpi']['EUR']['rate_float']
        return usd, gbp, eur
    else:
        return None, None, None

def obtener_tipo_cambio():
    fecha_hoy = datetime.now().strftime('%Y-%m-%d')
    url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?fecha={fecha_hoy}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['venta']
    else:
        return None

def crear_tabla_bitcoin():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bitcoin (
            fecha TEXT,
            usd REAL,
            gbp REAL,
            eur REAL,
            pen REAL
        )
    ''')
    conn.commit()
    conn.close()

def almacenar_precio_bitcoin(fecha, usd, gbp, eur, pen):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO bitcoin (fecha, usd, gbp, eur, pen) VALUES (?, ?, ?, ?, ?)
    ''', (fecha, usd, gbp, eur, pen))
    conn.commit()
    conn.close()

def consultar_precio_bitcoins():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT usd, gbp, eur, pen FROM bitcoin ORDER BY fecha DESC LIMIT 1')
    row = cursor.fetchone()
    if row:
        usd, gbp, eur, pen = row
        precio_10_bitcoins_pen = 10 * pen
        precio_10_bitcoins_eur = 10 * eur
        print(f"Precio de 10 bitcoins en PEN: {precio_10_bitcoins_pen:.2f}")
        print(f"Precio de 10 bitcoins en EUR: {precio_10_bitcoins_eur:.2f}")
    else:
        print("No hay datos disponibles.")
    conn.close()

def main():
    crear_tabla_bitcoin()
    
    usd, gbp, eur = obtener_precio_bitcoin()
    if usd is None or gbp is None or eur is None:
        print("No se pudieron obtener los precios del bitcoin.")
        return
    
    pen = obtener_tipo_cambio()
    if pen is None:
        print("No se pudo obtener el tipo de cambio de SUNAT.")
        return

    precio_bitcoin_pen = usd * pen
    
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    almacenar_precio_bitcoin(fecha, usd, gbp, eur, precio_bitcoin_pen)
    
    consultar_precio_bitcoins()

if __name__ == "__main__":
    main()
