import requests
def get_price(): 
    try: 
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        response = requests.get(url)

        data = response.json()
        data_usd_price = data['bpi']['USD']['rate_float']
        return data_usd_price
    
    except requests.RequestException as e:
        print(f'Ha ocurrido un error al obtener los datos de: {e}')
        return None

def main():
    try:
        num=float(input('Ingrese la cantidad de Bitcoins que posee: '))
    
    except ValueError:
        print('El valor ingresado no es valido')
        return

    price_bitcoin = get_price()
    if price_bitcoin is not None:
        result = num * price_bitcoin
        print(f'El costo actual de {num} Bitcoins en USD es: ${result:,.4f}')

    else: 
        print('No se ha podido obtener el precio del Bitcoin, ha ocurrido un error')

if __name__ == "__main__":
    main()



