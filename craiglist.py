#se importa la biblioteca requests, que nos permitira hacer solicitudes HTTP
import requests
#se importa beatiful soup que nos permite hacer parseos de html 
from bs4 import BeautifulSoup

#definicion de variables 
URL = "https://buenosaires.craigslist.org/search/apa?query=Belgrano&availabilityMode=0&sale_date=todas+las+fechas"
#URL = "https://buenosaires.craigslist.org/d/apartments-housing-for-rent/search/apa"
pagina = requests.get(URL)
#uso beatifulsoup para hacer el parseo de HTML 
sopa = BeautifulSoup(pagina.content, "html.parser")
resultado = sopa.find(class_="rows")
elementos = resultado.find_all('li', class_="result-row")

#se itera por el array de elementos
for elemento in elementos:
    barrio = elemento.find(class_="result-hood")
    #tomo la etiqueta de precio de cada uno de los elementos
    precios = elemento.find(class_="result-price")
    #la presento como texto 
    precioTxt = precios.text
    #luego de unos pequeños replaces puedo hacer la conversion a entero
    precioNumb = int(precioTxt.replace(".","").replace("₱",""))
    #ahora puedo hacer mis propios parametros de busquedas
    if (precioNumb < 18000):
        url_elemento = elemento.find('a', class_="result-image gallery")
        print(f"este apt es una ganga, se encuentra en el barrio: {barrio.text}. \nTiene un precio de {precioTxt}\nLa URL de alquiler es:")
        try:
            print(url_elemento['href'])
        except:
            print("url no disponible")