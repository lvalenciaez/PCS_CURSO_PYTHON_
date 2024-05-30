import requests

def almacenar(url):
    response = requests.get(url)
    data = response.json()
    print(data)

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
almacenar(url)

