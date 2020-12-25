from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':
    driver = webdriver.Chrome("/home/ptobarra/myGoogleDrive/6_intro_python_para_web/linux-chrome/chromedriver")

    # el metodo driver.get" navega a la pagina indicada mediante la URL
    driver.get("http://python.org")

    # WebDriver ofrece diferentes formas de encontrar elementos, como por ejemplo los metodos find_element_by_name
    elem = driver.find_element_by_name("q")

    # limpiamos el buscador
    elem.clear()

    # introducimos texto como si lo hiciesemos con el teclado
    elem.send_keys("pycon")

    # "pulsamos" enter
    elem.send_keys(Keys.RETURN)

    # si usamos "quit" cerramos todo el navegador, no solo la pagina actual
    # driver.close()
