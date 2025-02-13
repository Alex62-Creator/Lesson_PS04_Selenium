from selenium import webdriver
import time

browser = webdriver.Chrome()                                        # Создаём объект браузера

browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")  # Заходим на сайт
browser.save_screenshot("dom.png")                                  # Делаем скриншот
time.sleep(5)

browser.get("https://ru.wikipedia.org/wiki/Selenium")               # Заходим на сайт
browser.save_screenshot("selenium.png")                             # Делаем скриншот
time.sleep(5)

browser.refresh()                                                   # Обновляем страницу

browser.quit()                                                      # Закрываем браузер

