def contar_lineas_codigo(ruta_archivo):
    try:
        
        if not ruta_archivo.endswith('.py'):
            print("El archivo debe tener la extensión .py.")
            return

        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        
        lineas_codigo = 0
        for linea in lineas:
            linea_strip = linea.strip()
            if linea_strip and not linea_strip.startswith('#'):
                lineas_codigo += 1

        print(f"El archivo {ruta_archivo} tiene {lineas_codigo} líneas de código.")
    
    except FileNotFoundError:
        print(f"El archivo en la ruta {ruta_archivo} no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def solicitar_ruta_archivo():
    return input("Ingrese la ruta del archivo .py: ")

def main():
    ruta_archivo = solicitar_ruta_archivo()
    contar_lineas_codigo(ruta_archivo)

if __name__ == "__main__":
    main()
