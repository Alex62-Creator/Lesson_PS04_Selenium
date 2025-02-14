from selenium import webdriver
from selenium.webdriver.common.by import By     #Библиотека с поиском элементов на сайте
from selenium.webdriver import Keys     #Библиотека, которая позволяет вводить данные на сайт с клавиатуры
import time

#Функция перехода со страницы служебного поиска
def out_from_service_page():
    #Строим список из блоков "div"
    div_bloks = browser.find_elements(By.TAG_NAME, "div")
    #Ищем  блок "div" с аттрибутом "class" равным "mw-search-result-heading"
    for div in div_bloks:
        try:
            #Обходим исключения, если нет аттрибута "class" в блоке
            cl = div.get_attribute("class")
        except:
            continue
        if cl == "mw-search-result-heading":
            #Переходим на искомую страницу
            browser.get(div.find_element(By.TAG_NAME, "a").get_attribute("href"))

#Функция поиска внешних ссылок
def find_links():
    #Создаем список ссылок
    links = browser.find_elements(By.CSS_SELECTOR, '.mw-parser-output p a')

    #Выводим список ссылок
    i = 1
    for link in links:
        # Выводим, если внешняя ссылка
        if link.get_attribute('title'):
            print(i, link.get_attribute('title'))
            i += 1
        else:
            continue
    #Запрашиваем дальнейшее действие
    res = int(input("Введите номер интересующей вас статьи или\n"
                    "0 - возврат к главному меню "))
    if res == 0:
        return True
    #Если номер статьи правильный, переходим по ссылке
    elif res in range(len(links)+1):
        browser.get(links[res-1].get_attribute('href'))
    else:
        print("Неверный выбор")


#Функция просмотра страницы по параграфам
def read_paragraf():
    #Находим все параграфы (по тегу "р") на странице. Сохраняем в списке
    paragraphs = browser.find_elements(By.TAG_NAME, "p")

    #Читаем очередной параграф
    for paragraph in paragraphs:
        #Выводим, если параграф не пустой
        if paragraph.text:
            print(paragraph.text)
        else:
            continue
        #Запрашиваем дальнейшее действие
        res = input("Ввод - чтение следующего параграфа\n"
                    "0 - возврат к главному меню ")
        if res == '0':
            return True

#Создаём объект браузера
browser = webdriver.Chrome()

#Заходим на главную страницу Википедии
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

#Проверяем по заголовку, тот ли сайт открылся
try:
    assert "Википедия" in browser.title
except AssertionError:
    print("Проблемы с открытием Википедии. Попробуйте позже.")
    exit(0)

#Запрашиваем 1-ю тему
thema = input("Какой раздел Википедии вы хотите посмотреть? ")
#Находим окно поиска
search_box = browser.find_element(By.ID, "searchInput")
#Вводим текст в окно поиска
search_box.send_keys(thema)
#Переходим на нужную страницу
search_box.send_keys(Keys.RETURN)
#Переходим на искомую страницу, если попали на служебную
if 'page-Служебная_Поиск' in browser.find_element(By.TAG_NAME, "body").get_attribute("class"):
    out_from_service_page()

#Основной цикл
while True:
    var = input("1 - просмотр страницы\n"
                "2 - переход по по ссылке\n"
                "0 - завершение работы\n"
                "Сделайте выбор: ")

    if var == '0':
        print("Приятно было с вами поработать")
        break
    elif var == '1':
        #Вызываем функцию чтения
        read_paragraf()
    elif var == '2':
        # Вызываем функцию поиска ссылок
        find_links()
    else:
        print("Неверный выбор")

browser.quit()
