"""import requests
import zipfile
import os 

def descargar_img(url, name):
    try: 
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        with open(name,'wb') as f:
            f.write(response.content)
            print(f'Imagen guardada como: {name}')
    except requests.RequestException as e :
        print(f'A ocurrido el siguiente error al momento de descargar la imagen: {e} ')

def crear_zip(name, nombre_zip):
    try:
        with zipfile.ZipFile(name, 'w') as zipf:
            zipf.write(name, os.path.basename(name))
        print(f"Archivo {nombre_zip} creado exitosamente.")
    except Exception as e:
        print(f"Error al crear el archivo zip: {e}")

def extraer_zip(nombre, carpeta_destino):
    try:
        with zipfile.ZipFile(nombre, 'r') as zipf:
            zipf.extractall(carpeta_destino)
        print(f"Archivo {nombre} extraído exitosamente en la carpeta {carpeta_destino}.")
    except Exception as e:
        print(f"Error al extraer el archivo zip: {e}")


url = 'https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
name_img = 'imagen_download.jpg'
name_zip = 'imagen.zip'
carp_destino = './Descargas'

descargar_img(url,name_img)
crear_zip(name_img,name_zip)
extraer_zip(name_zip,carp_destino)"""

import requests
import zipfile
import os

def descargar_imagen(url, nombre_archivo):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(nombre_archivo, 'wb') as file:
            file.write(response.content)
        print(f"Imagen descargada y guardada como {nombre_archivo}.")
    except requests.RequestException as e:
        print(f"Error al descargar la imagen: {e}")
        return False
    return True

def crear_zip(nombre_archivo, nombre_zip):
    try:
        with zipfile.ZipFile(nombre_zip, 'w') as zipf:
            zipf.write(nombre_archivo, os.path.basename(nombre_archivo))
        print(f"Archivo {nombre_zip} creado exitosamente.")
    except Exception as e:
        print(f"Error al crear el archivo zip: {e}")
        return False
    return True

def extraer_zip(nombre_zip, carpeta_destino):
    try:
        os.makedirs(carpeta_destino, exist_ok=True)
        with zipfile.ZipFile(nombre_zip, 'r') as zipf:
            zipf.extractall(carpeta_destino)
        print(f"Archivo {nombre_zip} extraído exitosamente en la carpeta {carpeta_destino}.")
    except Exception as e:
        print(f"Error al extraer el archivo zip: {e}")
        return False
    return True

# URL de la imagen
url_imagen = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
nombre_imagen = "imagen_descargada.jpg"
nombre_zip = "imagen.zip"
carpeta_destino = "./extraido"

# Descargar la imagen
if descargar_imagen(url_imagen, nombre_imagen):
    # Crear el archivo ZIP
    if crear_zip(nombre_imagen, nombre_zip):
        # Extraer el archivo ZIP
        extraer_zip(nombre_zip, carpeta_destino)

