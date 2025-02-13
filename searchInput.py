from selenium import webdriver
from selenium.webdriver import Keys #Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By #Библиотека с поиском элементов на сайте
import time

#Создаём объект браузера
browser = webdriver.Chrome()

#Заходим на главную страницу Википедии
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

#Проверяем по заголовку, тот ли сайт открылся
try:
    assert "Википедия" in browser.title
    time.sleep(5)
except AssertionError:
    print("Открыта не та страница")
    exit(0)

#Находим окно поиска
search_box = browser.find_element(By.ID, "searchInput")

#Прописываем ввод текста в поисковую строку. В кавычках тот текст, который нужно ввести
search_box.send_keys("Солнечная система")
time.sleep(5)

#Добавляем не только введение текста, но и его отправку
search_box.send_keys(Keys.RETURN)
time.sleep(5)

#Находим ссылку-текст. В кавычках искомый текст-ссылка
a = browser.find_element(By.LINK_TEXT, "Рассеянный диск")
#Добавляем клик/переход на элемент
a.click()
time.sleep(5)

browser.quit()