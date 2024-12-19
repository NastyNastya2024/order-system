from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# Инициализация браузера
browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/Солнечная_система")

try:
    # Явное ожидание загрузки содержимого
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "mw-parser-output"))
    )

    # Поиск элемента с классом "mw-parser-output"
    content = browser.find_element(By.CLASS_NAME, "mw-parser-output")

    # Находим все параграфы внутри содержимого
    paragraphs = content.find_elements(By.TAG_NAME, "p")

    if paragraphs:
        print(f"Найдено параграфов: {len(paragraphs)}")

        # Выбираем случайный параграф
        random_paragraph = random.choice(paragraphs)
        text = random_paragraph.text.strip()

        if text:
            print("Случайный параграф текста:")
            print(text)

            # Поиск ссылок в этом параграфе
            links = random_paragraph.find_elements(By.TAG_NAME, "a")
            if links:
                random_link = random.choice(links).get_attribute("href")
                print(f"Переход по случайной ссылке: {random_link}")
                browser.get(random_link)
            else:
                print("Ссылки в выбранном параграфе не найдены.")
        else:
            print("Выбранный параграф пуст.")
    else:
        print("Параграфы в содержимом статьи не найдены.")
except Exception as e:
    print("Произошла ошибка:", e)
finally:
    # Закрытие браузера
    time.sleep(5)
    browser.quit()