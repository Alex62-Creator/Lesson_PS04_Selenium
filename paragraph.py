from selenium import webdriver
from selenium.webdriver.common.by import By #Библиотека с поиском элементов на сайте
import time

#Создаём объект браузера
browser = webdriver.Chrome()

#Сразу заходим на страницу солнечной системы
browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")

#Находим все параграфы (по тегу "р") на странице. Сохраняем в списке
paragraphs = browser.find_elements(By.TAG_NAME, "p")
print(paragraphs)

#Для перебора пишем цикл
for paragraph in paragraphs:
    print(paragraph.text)
    input()