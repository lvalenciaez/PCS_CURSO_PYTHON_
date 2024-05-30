
def save_tabla():
    while True:
        try:

            num =int(input('Ingrese un número entre el 1 y 10: '))
            if 1 <= num <= 10:
                break
            else:
                print('El número debe estar entre 1 y 10. Inténtalo nuevamente!')

        except ValueError:
            print('El caracter ingresado no es válido. Ingrese un número entero')
    
    with open(f'./PC4/tabla-{num}.txt','w') as file: 
        for i in range(1,11):
            file.write(f'{num}x{i}={num*i}\n')

    print(f'la tabla de multiplicar de {num} se ha guardado en ./PC4/tabla-{num}.txt')

save_tabla()

def recover_file(num:int):
    try:
        ruta_archivo = f'./PC4/tabla-{num}.txt'
        data = open(ruta_archivo, 'r').read()
        print(data)
    except FileNotFoundError:
        print('Archivo no encontrado')
    pass
print('A continuación se mostrará la función de recuperar el archivo de la tabla anterior')
n = int(input('Ingrese un número comprendido entre 1 y 10: '))
recover_file(n)

def read_lines():
    while True:

        try:
            num = int(input('Ingrese un número comprendido del 1 al 10: '))
            if 1 <= num <=10:
                n=int(input('Ingrese un número comprendido entre el 1 y el 10: '))
                if 1 <= n <=10:
                    break
                else:
                    print('El número debe estar entre 1 y 10. Inténtalo nuevamente!')
            else:
                print('El número debe estar entre 1 y 10. Inténtalo nuevamente!')

        except ValueError:
            print('El caracter ingresado no es válido. Ingrese un número entero')

        except FileNotFoundError:
            print('El archivo no se encuentra disponible')

    with open(f'./PC4/tabla-{num}.txt','r') as file:
        lineas_file = file.readlines(n)
        print(lineas_file)

read_lines()
