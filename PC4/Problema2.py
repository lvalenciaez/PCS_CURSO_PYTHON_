import random 
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    
    fuente =input('Ingrese el nombre de una fuente o presione enter para obtener una fuente aleatoria: ')
    fuentes_disponibles = figlet.getFonts()
    
    if not fuente:
        fuente=random.choice(fuentes_disponibles)

    if fuente not in fuentes_disponibles:
        print('Dicha fuente seleccionada no se encuentra en la lista de fuentes disponibles, se procederá a tomar una aleatoria')
        fuente = random.choice(fuentes_disponibles)

    figlet.setFont(font=fuente)

    var = input('Ingrese la palabra a transformar: ')
    print(figlet.renderText(var))

if __name__ =='__main__':
        main()

