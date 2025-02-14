from selenium import webdriver
from selenium.webdriver.common.by import By #Библиотека с поиском элементов на сайте
import time
import random

#Создаём объект браузера
browser = webdriver.Chrome()

#Сразу заходим на страницу солнечной системы
browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")

#Создаем пустой список
hatnotes = []

#Находим все элементы с тегом "div"
for element in browser.find_elements(By.TAG_NAME, "div"):
    #Отбираем в список элементы с атрибутом "class" равным "hatnote navigation-not-searchable ts-main"
    cl = element.get_attribute("class")
    if cl == "hatnote navigation-not-searchable ts-main":
        hatnotes.append(element)

#Выводим список отобранных элементов
i = 0
for elem in hatnotes:
    name = elem.find_element(By.TAG_NAME, "a").get_attribute("title")
    print(f"{i+1} {name}")
    i += 1

input()

#Выбираем случайный элемент
hatnote = random.choice(hatnotes)

#Для получения ссылки мы должны найти на сайте тег "a" внутри тега "div"
link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")

#Переходим по ссылке
browser.get(link)
time.sleep(3)

