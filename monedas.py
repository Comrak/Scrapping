#se importa la biblioteca requests, que nos permitira hacer solicitudes HTTP
import requests
#se importa beatiful soup que nos permite hacer parseos de html 
from bs4 import BeautifulSoup
from decimal import Decimal
import locale
locale.setlocale( locale.LC_ALL, '' )
#Defino constantes y Variables
URL_PESOS_BLUE = "https://www.dolarhoy.com/cotizaciondolarblue"
URL_BOLIVAR = "https://larepublica.pe/mundo/venezuela/2021/01/20/dolartoday-precio-del-dolar-este-miercoles-20-de-enero-del-2021-en-venezuela-mdga/"
URL_BITCOIN = "https://coinmarketcap.com/currencies/bitcoin/"
PAGINA_PESOS_BLUE = requests.get(URL_PESOS_BLUE)
PAGINA_BOLIVARES = requests.get(URL_BOLIVAR)
PAGINA_BTC = requests.get(URL_BITCOIN)
SOPA_PESOS_BLUE = BeautifulSoup(PAGINA_PESOS_BLUE.content, "html.parser")
SOPA_BOLIVARES = BeautifulSoup(PAGINA_BOLIVARES.content, "html.parser")
SOPA_BTC = BeautifulSoup(PAGINA_BTC.content, "html.parser")

#Obtengo cuantos pesos vale un dolar
pesos_blue = SOPA_PESOS_BLUE.find(class_="value")
#Obtener cuantos bolivares vale un dolar es un puto dolo de cabeza por que dolar today son unos mamaguebos y ponen las putas cotizaciones como imagenes, pero lo saque de otro lado, hay que dividirlo entre 5 luego
tabla_cotizacion = SOPA_BOLIVARES.find(class_="table-responsive")
bolivares_dividir_cinco = tabla_cotizacion.find('td')
bolivares = (Decimal((bolivares_dividir_cinco.text).replace("Bs.","").replace(".","").replace(",",".")))/5
bolivares = (locale.currency(bolivares, grouping=True))
bolivares = str(bolivares).replace("€","")
#obtener cuantos dolares vale un BTC
btc_value = SOPA_BTC.find("div", class_="priceValue___11gHJ")

# ya que tengo todos los valores puedo hacer cosas
print(f"un dolar es igual a {pesos_blue.text} pesos")
print(f"un dolar es igual a Bs.{bolivares}bolivares")
print(f"un bitcoin es igual a {btc_value.text} dolares")


