# Para poder esperar cuando crea conveniente
import time

from typing import List

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

URL = "https://www.eltiempo.es"

if __name__ == '__main__':
    # Utilizo el objeto options y le añado el argumento '--start-maximized' para que chrome inicie con la ventana \
    # maximizada para que salga en la pagina la caja de búsqueda
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # Carga el driver correspondiente (Chrome, Firefox,...)
    driver = webdriver.Chrome("/home/ptobarra/myGoogleDrive/6_intro_python_para_web/linux-chrome/chromedriver",
                              options=options)

    # El método “driver.get” navega a la página indicada
    driver.get(URL)

    # Simulo una espera de 3 segundos
    time.sleep(3)

    # Elegimos el botón de "ACEPTAR" la información de cookies
    elem = driver.find_element_by_id('didomi-notice-agree-button')

    # Enviamos la tecla, como su pulsásemos "Return"
    elem.send_keys(Keys.RETURN)

    # Obtén la caja de búsqueda
    elem = driver.find_element_by_name("inputSearch")

    # Borra el texto de la caja de búsqueda
    elem.clear()

    # Introducimos texto como si lo hiciésemos con el teclado
    elem.send_keys("vigo")

    # “Pulsamos” enter
    elem.send_keys(Keys.RETURN)

    # Elegimos el boton de 'Vigo, Pontevedra'
    url2 = "https://www.eltiempo.es/vigo.html?q=vigo"
    elem = driver.find_element_by_xpath('//a[@href="' + url2 + '"]')

    # “Pulsamos” enter
    elem.send_keys(Keys.RETURN)

    # Simulo una espera de 3 segundos para que de tiempo a que se cargue a pagina
    time.sleep(3)

    # Obtengo los días
    days: List[WebElement] = \
        driver.find_elements_by_xpath("//div[contains(@class, 'm_table_weather_day_child m_table_weather_day_rain')]")

    # Bucle "for" para ir procesando cada uno de los días obtenidos
    for index, value in enumerate(days):
        if value.text:  # chequeamos si el string esta vacio
            lluvia: float = float(value.text[:-3])
            # Para cada día, identificar si llueve o no llueve
            if lluvia > 0.0:
                print('SÍ lloverá: {0} mm'.format(str(lluvia)))
            else:
                print('NO lloverá: {0} mm'.format(str(lluvia)))

    # Usamos el método "close" para cerrar la página actual
    driver.close()
