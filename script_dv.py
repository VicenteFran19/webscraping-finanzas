import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

# Función para obtener el precio de una acción
def obtener_precio_accion(ticker):
    url = f'https://finance.yahoo.com/quote/{ticker}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    precio = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'}).text
    cambio = soup.find('fin-streamer', {'data-field': 'regularMarketChange'}).text
    cambio_porcentual = soup.find('fin-streamer', {'data-field': 'regularMarketChangePercent'}).text

    return {'Ticker': ticker, 'Precio': precio, 'Cambio': cambio, 'Cambio (%)': cambio_porcentual}

# Lista de acciones a analizar
acciones = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']

# Obtener los precios de las acciones
datos_acciones = []
for accion in acciones:
    datos_acciones.append(obtener_precio_accion(accion))

# Crear un DataFrame
df = pd.DataFrame(datos_acciones)

# Guardar en un archivo CSV
fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d')
nombre_archivo = f'precios_acciones_{fecha_actual}.csv'
df.to_csv(nombre_archivo, index=False)

print(f'Datos guardados en {nombre_archivo}')
