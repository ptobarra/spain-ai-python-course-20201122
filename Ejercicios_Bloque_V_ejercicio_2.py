from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Para poder esperar cuando crea conveniente
import time

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

    # Simulo una espera de 5 segundos
    time.sleep(5)

    # Usamos el método "close" para cerrar la página actual
    driver.close()
