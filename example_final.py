import requests
from bs4 import BeautifulSoup
# url elegida
url = 'https://www.mercadolibre.com.ar/c/autos-motos-y-otros#menu=categories'
# request
response = requests.get(url)
print(type(response))
# obtener texto plano y dárselo a BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
print(type(soup))
# búsqueda por algo distinto, en este caso es la clase.
results = soup.find_all('img', class_="dynamic-carousel__img")
# se muestran por consola las url de las imágenes
for img in results:
    # Se utilizó la propiedad data-src en vez de src porque la misma no contiene una url directa a la imagen, en cambio data-src si.
    print(img['data-src'])